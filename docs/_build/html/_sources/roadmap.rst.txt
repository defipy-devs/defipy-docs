.. _roadmap:

Roadmap & Changelog
======================

v2.1 (shipped 2026-05)
------------------------

The "State Twin Completion" cycle. Substrate becomes feature-complete:
chain reads compose with every primitive, the same way ``MockProvider``
recipes do.

* **V2 + V3 LiveProvider** — ``provider.snapshot("uniswap_v2:0xADDR")`` and ``provider.snapshot("uniswap_v3:0xADDR")`` build snapshots from real on-chain state. Block-pinned reads, decimal-adjusted reserves, ERC20 metadata via ``web3scout``.
* **Multicall3 batching** for V3 reads — single RPC round trip for ``slot0``, ``liquidity``, ``fee``, ``tickSpacing``, ``token0``, ``token1``, plus ``getCurrentBlockTimestamp``.
* **PoolSnapshot enrichment** — ``block_number``, ``timestamp``, ``chain_id`` as ``Optional[int]`` on the base class. ``LiveProvider`` populates from chain reads; ``MockProvider`` leaves them ``None``.
* **``LiveProvider.get_w3()`` escape hatch** — public substrate boundary for callers needing to sign transactions. DeFiPy stays read-only by design.
* **``PoolHealth`` ergonomics for V3** — ``fee_pips``, ``tvl_in_token1``, ``tick_current`` populated by ``CheckPoolHealth.apply()``.
* **``[chain]`` and ``[agentic]`` install extras** — chain reads and the canonical full-stack agentic install.
* **Fork-and-evaluate worked example** — ``python/examples/state_twin_fork_evaluate.py``. Walks through the pattern at `defipy.org/fork-evaluate <https://defipy.org/fork-evaluate/>`_.
* **686 tests** (11 skipped — opt-in live-RPC tests gated by ``DEFIPY_LIVE_RPC``).

See `defipy.org <https://defipy.org/>`_ for the canonical v2.1 surface.

v2.0 (shipped 2026-04)
-------------------------

Released 2026-04-23. See :ref:`whats_new_v2` for the full feature summary.

* ``defipy.tools`` — MCP tool schemas for 10 curated primitives
* ``defipy.twin`` — State Twin abstraction with MockProvider (4 recipes) and LiveProvider stub
* MCP server demo — verified live against Claude Desktop
* 629 tests, 125 new in v2.0
* Packaging fixes for all primitive sub-packages
* Zero breaking changes from v1.2.0

v2.2 (next)
-----------------

**LiveProvider for the remaining protocols.** Balancer and Stableswap LiveProvider implementations — same shape as V2/V3 in v2.1 but for the weighted-pool and stableswap invariants.

**V3 tick bitmap walking.** Pairs with the new ``AssessLiquidityDepth`` primitive — enables non-active-tick analyses on V3 LiveProvider twins. Active-liquidity primitives keep working unchanged.

**Multi-format tool schemas.** ``get_schemas("anthropic")`` and ``get_schemas("openai")`` — both derivable from the shipped MCP schemas with envelope-format wrappers. Reference examples in ``python/examples/``.

**Anvil fork integration tests.** Optional CI lane against a forked node for higher-confidence integration tests.

**Observability module.** ``defipy.observability`` replaces the v2.0 stderr-receipt pattern with a structured event sink and opt-in tracing. Composable with the MCP server's dispatch loop.

**web3scout web3 7.x support.** Track upstream — ``[chain]`` currently pins ``web3 < 7.0`` due to ``web3scout 0.2.0``'s reliance on ``eth_utils.abi.get_abi_input_types`` (web3 6 only).

**Primitive promotions.** Candidates for promotion from Python-API-only to MCP tool status, as protocol parity and dependency blockers clear:

* ``DetectFeeAnomaly`` — pending multi-protocol support
* ``CompareFeeTiers`` — pending MockProvider multi-fee-tier recipes
* ``EvaluateRebalance`` — pending multi-step reasoning ergonomics assessment

v2.3+ (planned)
-----------------

**Planning primitives category.** Non-mutating projections that answer "what should I do next?":

* ``PlanRebalance`` — project the cost/benefit of rebalancing a V3 position to a new tick range
* ``PlanZapIn`` — project a single-token deposit into an LP position
* ``PlanExit`` — project the cost of exiting a position at current state

**Protocol extensions.** Balancer and Stableswap support for primitives currently V2/V3-only:

* ``FindBreakEvenPrice`` — extend to Balancer weighted-pool invariant
* ``FindBreakEvenTime`` — extend to Balancer and Stableswap
* ``CalculateSlippage`` — extend to Balancer and Stableswap

**New primitives.**

* ``AssessLiquidityDepth`` — V3 tick-walking to assess concentrated liquidity depth around the active tick (pairs with v2.2 tick bitmap walking)
* ``DiscoverPools`` — pool discovery across protocols (stretch goal; overlaps with existing MCP ecosystem tools)

v3.0 (horizon)
-----------------

**defipy.org launch.** Public-facing site with documentation, blog, and community resources. ReadTheDocs continues as the SDK reference; defipy.org becomes the marketing and community surface.

**Theme migration.** ReadTheDocs theme upgrade from ``sphinx_rtd_theme`` to Furo or equivalent modern theme.

**Token considerations.** No token is planned. If a token ever ships, it will be after a stable business case exists — not before. This is a deliberate, cycle-tested discipline. See the project's infrastructure-first positioning: DeFiPy is substrate, not a product.

Changelog
-----------

The full changelog with per-release details is maintained in `CHANGELOG.md <https://github.com/defipy-devs/defipy/blob/main/CHANGELOG.md>`_ in the main repository.

* `v2.1.0 <https://github.com/defipy-devs/defipy/releases/tag/v2.1.0>`_ — 2026-05-07
* `v2.0.0 <https://github.com/defipy-devs/defipy/compare/v1.2.0...v2.0.0>`_ — 2026-04-23
* `v1.2.0 <https://github.com/defipy-devs/defipy/releases/tag/v1.2.0>`_ — 2026-04-18
