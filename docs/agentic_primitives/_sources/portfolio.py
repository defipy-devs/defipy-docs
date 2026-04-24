# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Portfolio
#
# The Portfolio category answers questions about LP positions *in aggregate* rather than individually. It contains one primitive — `AggregatePortfolio` — which dispatches across all four supported protocols (V2, V3, Balancer, Stableswap) and sums per-position results in a shared first-token numeraire.
#
# This category is the library's first **composition primitive**: it wraps the per-protocol `Analyze*Position` primitives (from the [Position Analysis](position_analysis.ipynb) category) rather than computing new math. The rationale for a portfolio-level wrapper is ergonomic — a quant or an agent asking *"what's my total IL across all my positions?"* shouldn't have to re-run the per-position math themselves.
#
# All primitives in the Agentic Primitives section follow the same contract: stateless construction, computation at `.apply()`, typed dataclass return. See [The Primitive Contract](../primitive_contract.rst) for the invariants.

# %% [markdown]
# ## AggregatePortfolio
#
# **Purpose.** Aggregate N LP positions into a single portfolio-level view. Dispatches per-position to the appropriate `Analyze*Position` primitive, extracts common scalars (net_pnl, il_percentage, fee_income), and sums them in a shared first-token numeraire.
#
# **Signature.**
#
# ```python
# AggregatePortfolio().apply(positions: list[PortfolioPosition]) -> PortfolioAnalysis
# ```
#
# **Numeraire discipline.** All positions in a single call must share a common first-token symbol. For V2/V3 this is `lp.token0`; for Balancer/Stableswap it's the first token in the pool's insertion order. A portfolio mixing ETH/DAI (V2), ETH/DAI (V3), and ETH/DAI (Balancer 50/50) works cleanly — all have `ETH` as token0. Mixing ETH/DAI and USDC/DAI does not — the "total" would conflate ETH-units and USDC-units, and `AggregatePortfolio` raises at `.apply()` rather than silently producing misleading sums.

# %% [markdown]
# ### Setup
#
# Build three twins from MockProvider recipes that share ETH as their first token. We'll use these for a cross-protocol portfolio example.

# %%
from defipy.twin import MockProvider, StateTwinBuilder

provider = MockProvider()
builder = StateTwinBuilder()

lp_v2 = builder.build(provider.snapshot("eth_dai_v2"))
lp_v3 = builder.build(provider.snapshot("eth_dai_v3"))
lp_balancer = builder.build(provider.snapshot("eth_dai_balancer_50_50"))

print(f"V2 pool:       {lp_v2.token0}/{lp_v2.token1}")
print(f"V3 pool:       {lp_v3.token0}/{lp_v3.token1}")
print(f"Balancer pool: {list(lp_balancer.tkn_reserves.keys())}")

# %% [markdown]
# ### Example: aggregate three positions across V2, V3, and Balancer
#
# Each `PortfolioPosition` wraps the same inputs its per-protocol analyzer would take — LP amount, entry token amounts — plus an optional display name and holding period.

# %%
from defipy import AggregatePortfolio
from defipy.utils.data import PortfolioPosition

positions = [
    PortfolioPosition(
        lp = lp_v2,
        lp_init_amt = 10000.0,
        entry_x_amt = 1000.0,
        entry_y_amt = 100000.0,
        holding_period_days = 30.0,
        name = "ETH/DAI V2",
    ),
    PortfolioPosition(
        lp = lp_v3,
        lp_init_amt = 10000.0,
        entry_x_amt = 1000.0,
        entry_y_amt = 100000.0,
        holding_period_days = 30.0,
        name = "ETH/DAI V3",
    ),
    PortfolioPosition(
        lp = lp_balancer,
        lp_init_amt = 100.0,
        entry_x_amt = 1000.0,
        entry_y_amt = 100000.0,
        holding_period_days = 30.0,
        name = "ETH/DAI Balancer 50/50",
    ),
]

result = AggregatePortfolio().apply(positions)

# %% [markdown]
# ### The PortfolioAnalysis result
#
# `PortfolioAnalysis` carries portfolio-wide scalars plus per-position detail. Scalars sum in the numeraire enforced at `.apply()` — ETH in this case.

# %%
print(f"Numeraire:           {result.numeraire}")
print(f"Total value:         {result.total_value:.4f} {result.numeraire}")
print(f"Total hold value:    {result.total_hold_value:.4f} {result.numeraire}")
print(f"Total net PnL:       {result.total_net_pnl:.4f} {result.numeraire}")
print(f"Total fees:          {result.total_fees:.4f} {result.numeraire}")
print()
print("PnL ranking (worst first):")
for name in result.pnl_ranking:
    print(f"  - {name}")
print()
print("Shared-exposure warnings:")
for note in result.shared_exposure_warnings:
    print(f"  - {note}")

# %% [markdown]
# ### Per-position detail
#
# Every position's full `Analyze*Position` result is preserved on `result.positions[i].analysis` — callers who want protocol-specific detail after the aggregation can pull it without re-running.

# %%
for summary in result.positions:
    print(f"{summary.name} ({summary.protocol})")
    print(f"  net_pnl:       {summary.net_pnl:.4f}")
    print(f"  il_percentage: {summary.il_percentage:.4f}")
    print(f"  fee_income:    {summary.fee_income:.4f}")
    print(f"  tokens:        {summary.tokens}")
    print()

# %% [markdown]
# ### Numeraire enforcement in action
#
# A portfolio mixing incompatible numeraires raises — no silent unit-conflation.

# %%
lp_stableswap = builder.build(provider.snapshot("usdc_dai_stableswap_A10"))

bad_positions = [
    PortfolioPosition(
        lp = lp_v2,
        lp_init_amt = 10000.0,
        entry_x_amt = 1000.0,
        entry_y_amt = 100000.0,
        name = "ETH/DAI V2",
    ),
    PortfolioPosition(
        lp = lp_stableswap,
        lp_init_amt = 100.0,
        entry_amounts = [1000.0, 1000.0],
        name = "USDC/DAI Stableswap",
    ),
]

try:
    AggregatePortfolio().apply(bad_positions)
except ValueError as e:
    print(f"ValueError raised as expected:\n  {e}")

# %% [markdown]
# ## Protocol coverage
#
# | Protocol | Supported | Notes |
# |---|---|---|
# | Uniswap V2 | ✅ | Full support via `AnalyzePosition` |
# | Uniswap V3 | ✅ | Full support via `AnalyzePosition`; respects tick range |
# | Balancer | ✅ | Dispatch via `AnalyzeBalancerPosition`; fee income is 0 in v1 |
# | Stableswap | ⚠️ | Dispatch via `AnalyzeStableswapPosition`; unreachable-alpha positions contribute 0 to totals and are flagged in `shared_exposure_warnings` |
#
# See the [Risk](risk.ipynb) category for `AssessDepegRisk`, the complement to stableswap portfolio aggregation.

# %% [markdown]
# ## MCP exposure
#
# `AggregatePortfolio` is **not** exposed as an MCP tool in v2.0. The curation principle (leaf primitives only; let composition happen LLM-side) keeps `AggregatePortfolio` as a Python-API primitive rather than a tool — an LLM aggregating three positions can simply call `AnalyzePosition` three times and sum the results itself. See [Tool Schemas](../../agentic_tool_schemas.rst) for the curation rationale.
#
# This is the reason the Portfolio category contains just this one primitive: it's the *composition wrapper* for the [Position Analysis](position_analysis.ipynb) leaves. Most categories have 2-3 leaf primitives; Portfolio has one composition primitive that wraps them.

# %% [markdown]
# ## See also
#
# - [Position Analysis](position_analysis.ipynb) — the per-protocol `Analyze*Position` leaves that `AggregatePortfolio` dispatches to
# - [Result Dataclasses](../agentic_result_dataclasses.rst) — full field reference for `PortfolioAnalysis`, `PositionSummary`, `PortfolioPosition`
# - [The Primitive Contract](../primitive_contract.rst) — the stateless / `.apply()` / typed-dataclass contract all primitives honor
