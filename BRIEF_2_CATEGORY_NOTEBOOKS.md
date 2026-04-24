# Brief 2 — Agentic Primitives Category Notebooks (Batch 4)

**Target repo:** `/Users/ian_moore/repos/defipy-docs`
**Branch:** `v2` (confirm with `git branch --show-current`)
**Scope:** Draft 9 Jupyter notebooks — one per agentic primitives category — with executable examples against MockProvider twins. Place them at `docs/agentic_primitives/notebooks/<category>.ipynb`. Each notebook follows the same structural template. After drafting, execute all cells in Jupyter so outputs are baked into the committed `.ipynb`.

**Source code reference:** All primitive classes live in `/Users/ian_moore/repos/defipy/python/prod/primitives/`. Read each primitive's source to get exact signatures, parameter names, and return types. Do not guess signatures — read the code.

**Result dataclass reference:** All result dataclasses live in `/Users/ian_moore/repos/defipy/python/prod/utils/data/`. Read each dataclass to get exact field names for the output-explanation cells.

**Twin reference:** `MockProvider` and `StateTwinBuilder` live in `/Users/ian_moore/repos/defipy/python/prod/twin/`. The four canonical recipes are:
- `eth_dai_v2` — Uniswap V2, 1000 ETH / 100000 DAI
- `eth_dai_v3` — Uniswap V3, 1000 ETH / 100000 DAI, full-range, fee=3000
- `eth_dai_balancer_50_50` — Balancer 2-asset, 50/50 weights, 1000 ETH / 100000 DAI
- `usdc_dai_stableswap_A10` — Stableswap 2-asset, 100000 USDC / 100000 DAI, A=10

Use the appropriate recipe for each primitive's protocol scope. V2/V3 primitives use `eth_dai_v2` or `eth_dai_v3`. Balancer primitives use `eth_dai_balancer_50_50`. Stableswap primitives use `usdc_dai_stableswap_A10`.

**Explicit non-goals:**
- Do not modify `index.rst`, `conf.py`, or any other docs infrastructure. Ian has already wired the toctree.
- Do not create `.py` percent-format source files. Draft `.ipynb` directly.
- Do not push. Ian will review locally.

---

## 0. Pre-flight

```bash
cd /Users/ian_moore/repos/defipy-docs
git branch --show-current    # expect: v2
```

Verify the target directory exists:

```bash
ls docs/agentic_primitives/notebooks/
```

Should show 9 stub `.ipynb` files (7 existing stubs + 2 recently created: `risk.ipynb` and `portfolio.ipynb`). This brief overwrites all 9 with real content.

Verify defipy v2.0 is importable:

```python
python -c "from defipy import AnalyzePosition; print('ok')"
python -c "from defipy.twin import MockProvider, StateTwinBuilder; print('ok')"
```

If either fails, `pip install -e /Users/ian_moore/repos/defipy` in the active venv.

---

## 1. Notebook template

Every category notebook follows this structure. Read this section completely before drafting any notebook.

### Cell structure

Each notebook contains these cells in order:

**Cell 1 — Title + category intro (markdown)**
```markdown
# <Category Name>

<2-3 sentences: what questions this category answers, how many primitives it contains, which protocols are covered.>

All primitives in the Agentic Primitives section follow the same contract: stateless construction, computation at `.apply()`, typed dataclass return.
```

**Cell 2 — Setup (code)**
```python
from defipy.twin import MockProvider, StateTwinBuilder

provider = MockProvider()
builder = StateTwinBuilder()

lp = builder.build(provider.snapshot("<appropriate_recipe>"))
```

Use the recipe that matches the category's primary protocol scope. For categories covering multiple protocols, build multiple twins.

**Cells 3..N — One subsection per primitive in the category**

For each primitive, include these cells:

**(a) Primitive header + signature (markdown)**
```markdown
## <PrimitiveName>

**Purpose.** <One sentence from the primitive's class docstring.>

**Signature.**

\```python
<PrimitiveName>(<constructor_args>).apply(<apply_args>) -> <ResultDataclass>
\```

<Any behavioral notes specific to this primitive — numeraire rules, protocol restrictions, threshold semantics, etc. Pull from the class docstring.>
```

**(b) Example (code)**
```python
from defipy import <PrimitiveName>

result = <PrimitiveName>(<constructor_args>).apply(<lp>, <args>)
```

Use concrete, realistic parameter values. Use the twin built in the Setup cell. Keep examples minimal — 3-8 lines of code.

**(c) Output inspection (code)**
```python
print(f"<field1>: {result.<field1>}")
print(f"<field2>: {result.<field2>}")
# ... key fields from the result dataclass
```

Print the 3-5 most important fields. Don't print every field — just the ones that answer the category's core question.

**(d) Output explanation (markdown)** — optional, only if the field semantics aren't obvious from the name.

**Cell N+1 — Protocol coverage table (markdown)**
```markdown
## Protocol coverage

| Protocol | Supported | Notes |
|---|---|---|
| Uniswap V2 | ✅ / ❌ / ⚠️ | <notes> |
| Uniswap V3 | ✅ / ❌ / ⚠️ | <notes> |
| Balancer | ✅ / ❌ / ⚠️ | <notes> |
| Stableswap | ✅ / ❌ / ⚠️ | <notes> |
```

Determine coverage by reading which protocols each primitive's `.apply()` supports. V2/V3 primitives that dispatch on `lp.version` cover both. Balancer/Stableswap primitives are protocol-specific.

**Cell N+2 — MCP exposure note (markdown)**
```markdown
## MCP tool exposure

<State which primitives in this category are in the curated 10 MCP tools, and which are not. The 10 curated tools are: AnalyzePosition, AnalyzeBalancerPosition, AnalyzeStableswapPosition, AssessDepegRisk, CalculateSlippage, CheckPoolHealth, DetectRugSignals, SimulateBalancerPriceMove, SimulatePriceMove, SimulateStableswapPriceMove.>
```

### Voice and tone

- Technical-practitioner direct. Declarative sentences. No marketing. No hype.
- Follow the Quick Start pattern from `docs/quick/index.rst` — Purpose / Signature / Example / Output.
- Code examples should be minimal and runnable. A reader should be able to copy-paste into a Python session and get the same output.
- Bold paragraph labels (`**Purpose.**`, `**Signature.**`) for structure within a primitive's subsection. H2 (`##`) for primitive names. H1 (`#`) for the category title only.

---

## 2. The 9 notebooks — category-by-category specifications

### 2a. `position_analysis.ipynb` — Position Analysis

**Primitives (3):**
- `AnalyzePosition` — V2/V3 position decomposition (IL, fees, net PnL, diagnosis)
- `AnalyzeBalancerPosition` — Balancer weighted-pool position analysis
- `AnalyzeStableswapPosition` — Stableswap position analysis (handles unreachable-alpha)

**Setup:** Build twins for `eth_dai_v2`, `eth_dai_balancer_50_50`, and `usdc_dai_stableswap_A10`.

**Example parameters:**
- `AnalyzePosition`: `lp_init_amt=10000.0, entry_x_amt=1000.0, entry_y_amt=100000.0, holding_period_days=30.0`
- `AnalyzeBalancerPosition`: `lp_init_amt=100.0, entry_x_amt=1000.0, entry_y_amt=100000.0, holding_period_days=30.0`
- `AnalyzeStableswapPosition`: `lp_init_amt=100.0, entry_amounts=[100000.0, 100000.0], holding_period_days=30.0`

**Key output fields to print:**
- `AnalyzePosition`: `current_value`, `hold_value`, `il_percentage`, `fee_income`, `net_pnl`, `diagnosis`
- `AnalyzeBalancerPosition`: `current_value`, `hold_value`, `il_percentage`, `net_pnl`, `weight_base`, `weight_opp`
- `AnalyzeStableswapPosition`: `current_value`, `hold_value`, `il_percentage`, `net_pnl`, `A`, `alpha`

**Protocol coverage:** V2 ✅, V3 ✅ (via AnalyzePosition), Balancer ✅ (via AnalyzeBalancerPosition), Stableswap ⚠️ (via AnalyzeStableswapPosition; unreachable-alpha regime yields None for some fields)

**MCP:** All three are in the curated 10.

---

### 2b. `price_scenarios.ipynb` — Price Scenarios

**Primitives (3):**
- `SimulatePriceMove` — V2/V3 position value at a hypothetical price change
- `SimulateBalancerPriceMove` — Balancer weighted-pool price-move projection
- `SimulateStableswapPriceMove` — Stableswap price-move projection

**Setup:** Build twins for `eth_dai_v2`, `eth_dai_balancer_50_50`, and `usdc_dai_stableswap_A10`.

**Example parameters:**
- `SimulatePriceMove`: `lp_init_amt=10000.0, entry_x_amt=1000.0, entry_y_amt=100000.0, price_move_pct=-30.0` (simulate ETH dropping 30%)
- `SimulateBalancerPriceMove`: `lp_init_amt=100.0, entry_x_amt=1000.0, entry_y_amt=100000.0, price_move_pct=-30.0`
- `SimulateStableswapPriceMove`: `lp_init_amt=100.0, entry_amounts=[100000.0, 100000.0], price_move_pct=-5.0` (stableswap: smaller move is more realistic)

**Key output fields:** `projected_value`, `projected_hold_value`, `projected_il_percentage`, `projected_net_pnl`

Read each primitive's source for exact parameter names — they may differ slightly across protocols (e.g., `price_move_pct` vs `price_change_pct`). Use the exact parameter name from the source.

**Protocol coverage:** V2 ✅, V3 ✅, Balancer ✅, Stableswap ✅

**MCP:** `SimulatePriceMove`, `SimulateBalancerPriceMove`, `SimulateStableswapPriceMove` are all in the curated 10.

---

### 2c. `pool_health.ipynb` — Pool Health

**Primitives (3):**
- `CheckPoolHealth` — pool-level health snapshot (TVL, reserves, LP concentration, fee activity)
- `DetectRugSignals` — threshold-based rug-pull signal detector (composes over CheckPoolHealth)
- `DetectFeeAnomaly` — detect unusual fee patterns

**Setup:** Build twin for `eth_dai_v2`.

**Example parameters:**
- `CheckPoolHealth`: `lp` only (default `recent_window=20`)
- `DetectRugSignals`: `lp` only (default thresholds). Also show one example with custom thresholds: `lp_concentration_threshold=0.95, tvl_floor=5.0`
- `DetectFeeAnomaly`: read the source for exact signature — constructor may take `threshold_bps`. Use appropriate defaults.

**Key output fields:**
- `CheckPoolHealth`: `spot_price`, `reserve0`, `reserve1`, `tvl_in_token0`, `num_swaps`, `num_lps`, `top_lp_share_pct`, `has_activity`
- `DetectRugSignals`: `risk_level`, `signals_detected`, `tvl_suspiciously_low`, `single_sided_concentration`, `inactive_with_liquidity`, `details`
- `DetectFeeAnomaly`: read the source for field names

**Protocol coverage:** V2 ✅, V3 ✅ (partial — some V2-only metrics are None on V3), Balancer ❌, Stableswap ❌

**MCP:** `CheckPoolHealth` and `DetectRugSignals` are in the curated 10. `DetectFeeAnomaly` is not.

---

### 2d. `risk.ipynb` — Risk

**Primitives (2):**
- `CheckTickRangeStatus` — V3-only: is the position's tick range still active?
- `AssessDepegRisk` — Stableswap-only: quantify exposure to a stablecoin depeg

**Setup:** Build twins for `eth_dai_v3` (for CheckTickRangeStatus) and `usdc_dai_stableswap_A10` (for AssessDepegRisk).

**Example parameters:**
- `CheckTickRangeStatus`: read the source for exact signature — needs tick range params
- `AssessDepegRisk`: read the source for exact signature — needs depeg scenario params

**Key output fields:** Read each primitive's result dataclass.

**Protocol coverage:** V2 ❌, V3 ✅ (CheckTickRangeStatus only), Balancer ❌, Stableswap ✅ (AssessDepegRisk only)

**MCP:** `AssessDepegRisk` is in the curated 10. `CheckTickRangeStatus` is not.

**Special note:** These two primitives are protocol-specific by design — they answer questions that only make sense for one protocol. The notebook should explain this in the intro rather than presenting it as a gap.

---

### 2e. `optimization.ipynb` — Optimization

**Primitives (3):**
- `OptimalDepositSplit` — compute the optimal token split for a single-sided deposit
- `EvaluateRebalance` — evaluate whether rebalancing a position is worth the cost
- `EvaluateTickRanges` — V3-only: compare candidate tick ranges for a position

**Setup:** Build twins for `eth_dai_v2` and `eth_dai_v3`.

**Example parameters:** Read each primitive's source for exact signatures.

**Key output fields:** Read each primitive's result dataclass.

**Protocol coverage:** V2 ✅ (OptimalDepositSplit, EvaluateRebalance), V3 ✅ (all three), Balancer ❌, Stableswap ❌

**MCP:** None of these are in the curated 10. The notebook should explain why: these primitives require multi-step reasoning that's better composed LLM-side.

---

### 2f. `comparison.ipynb` — Comparison

**Primitives (2):**
- `CompareFeeTiers` — compare fee tier options for a V3 position
- `CompareProtocols` — cross-protocol comparison of the same token pair

**Setup:** Build twins for `eth_dai_v2`, `eth_dai_v3`, `eth_dai_balancer_50_50`.

**Example parameters:** Read each primitive's source for exact signatures.

**Key output fields:** Read each primitive's result dataclass.

**Protocol coverage:** V2 ✅ (CompareProtocols), V3 ✅ (both), Balancer ✅ (CompareProtocols), Stableswap ✅ (CompareProtocols)

**MCP:** Neither is in the curated 10.

---

### 2g. `execution.ipynb` — Execution

**Primitives (2):**
- `CalculateSlippage` — compute slippage and price impact for a proposed swap
- `DetectMEV` — detect potential MEV exposure for a swap

**Setup:** Build twin for `eth_dai_v2`.

**Example parameters:** Read each primitive's source for exact signatures. Both need swap-related params (token_in, amount, etc.).

**Key output fields:** Read each primitive's result dataclass.

**Protocol coverage:** V2 ✅, V3 ✅, Balancer ❌, Stableswap ❌

**MCP:** `CalculateSlippage` is in the curated 10. `DetectMEV` is not.

---

### 2h. `portfolio.ipynb` — Portfolio

**Primitives (1):**
- `AggregatePortfolio` — aggregate N LP positions into a single portfolio view

**Setup:** Build twins for `eth_dai_v2`, `eth_dai_v3`, `eth_dai_balancer_50_50`. Import `PortfolioPosition` from `defipy.utils.data`.

**Example parameters:**
- Three `PortfolioPosition` objects wrapping the three twins with `lp_init_amt`, `entry_x_amt`, `entry_y_amt`, `holding_period_days=30.0`, named labels.
- Show the numeraire enforcement by also building `usdc_dai_stableswap_A10` and trying a mixed-numeraire call that raises `ValueError`.

**Key output fields:** `numeraire`, `total_value`, `total_hold_value`, `total_net_pnl`, `total_fees`, `pnl_ranking`, `shared_exposure_warnings`. Also iterate `result.positions` to print per-position summaries.

**Protocol coverage:** V2 ✅, V3 ✅, Balancer ✅, Stableswap ⚠️ (unreachable-alpha contributes 0)

**MCP:** Not in the curated 10. Composition primitive — explain the curation rationale (leaf primitives only).

**Reference implementation:** A detailed Portfolio notebook was drafted earlier in this session. The content is available in `/Users/ian_moore/repos/defipy-docs/docs/agentic_primitives/primitives_notebooks/_sources/portfolio.py` as a percent-format source file. Use it as the primary reference for this notebook's structure and content. Adapt the cross-links for the current file layout (sibling notebooks are at same level, RST pages are at `../../<page>.html`).

---

### 2i. `break_even.ipynb` — Break-Even

**Primitives (2):**
- `FindBreakEvenPrice` — find the price at which IL equals fee income
- `FindBreakEvenTime` — find the holding period at which fee income compensates IL

**Setup:** Build twin for `eth_dai_v2`.

**Example parameters:** Read each primitive's source for exact signatures.

**Key output fields:** Read each primitive's result dataclass.

**Protocol coverage:** V2 ✅, V3 ✅, Balancer ❌, Stableswap ❌

**MCP:** Neither is in the curated 10.

---

## 3. Execution

After drafting all 9 notebooks:

```bash
cd /Users/ian_moore/repos/defipy-docs

# Execute all notebooks to bake outputs
for nb in docs/agentic_primitives/notebooks/*.ipynb; do
    echo "Executing: $nb"
    jupyter nbconvert --to notebook --execute --inplace "$nb"
done
```

If any notebook fails to execute, fix the code cell and retry. Common failure modes:
- Wrong parameter name (read the source again)
- Missing import (check the primitive's module path)
- Recipe incompatible with primitive (use the right MockProvider recipe)

After execution, verify each notebook has cell outputs:

```bash
for nb in docs/agentic_primitives/notebooks/*.ipynb; do
    echo "$nb: $(python3 -c "import json; nb=json.load(open('$nb')); print(sum(1 for c in nb['cells'] if c.get('outputs')))")" outputs
done
```

---

## 4. Build verification

```bash
cd /Users/ian_moore/repos/defipy-docs/docs
sphinx-build -b html . _build/html 2>&1 | tee /tmp/build_batch4.log
```

Verify:
- All 9 notebooks render as HTML pages under `_build/html/agentic_primitives/notebooks/`
- Each page shows executed code cells with outputs
- No `toctree contains reference to nonexisting document` errors
- Sidebar shows all 9 categories under Agentic Primitives

Open a few rendered pages in a browser and confirm:
- Code cells render with syntax highlighting
- Output cells show printed results
- Markdown cells render with proper formatting (tables, bold, code blocks)
- Cross-links between notebooks resolve (click a "See also" link)

---

## 5. Commit

```bash
git add docs/agentic_primitives/notebooks/*.ipynb
git add docs/agentic_primitives/index.rst
git commit -m "feat(docs): draft 9 agentic primitives category notebooks

One notebook per category, covering all 21 primitives:
- Position Analysis (3): AnalyzePosition, AnalyzeBalancerPosition, AnalyzeStableswapPosition
- Price Scenarios (3): SimulatePriceMove, SimulateBalancerPriceMove, SimulateStableswapPriceMove
- Pool Health (3): CheckPoolHealth, DetectRugSignals, DetectFeeAnomaly
- Risk (2): CheckTickRangeStatus, AssessDepegRisk
- Optimization (3): OptimalDepositSplit, EvaluateRebalance, EvaluateTickRanges
- Comparison (2): CompareFeeTiers, CompareProtocols
- Execution (2): CalculateSlippage, DetectMEV
- Portfolio (1): AggregatePortfolio
- Break-Even (2): FindBreakEvenPrice, FindBreakEvenTime

Each notebook follows the template: category intro, per-primitive
signature + example + output, protocol coverage table, MCP exposure
note. All cells executed with MockProvider twins."
```

Do not push. Ian will review locally.

---

## 6. Deliverables summary

Produce a summary with:

1. Confirmation that all 9 notebooks execute cleanly
2. Confirmation that `sphinx-build` succeeds and all 9 render as HTML
3. List of any primitives whose signatures differed from the brief's specification (expected — the brief says "read the source" for several primitives)
4. List of any execution failures encountered and how they were resolved
5. Count of total primitives documented (should be 21)
6. Flag for Ian to review locally before push

If a primitive's source reveals a signature that doesn't match the brief's example parameters, use the source as the authority — the brief's examples are approximations; the code is truth.

---

*End of Brief 2. Brief 3 (autodoc wiring + RTD deploy) follows after Ian's local review of the rendered notebooks.*
