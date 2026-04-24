.. _roadmap:

Roadmap & Changelog
======================

v2.0 (shipped)
-----------------

Released 2026-04-23. See :ref:`whats_new_v2` for the full feature summary.

* ``defipy.tools`` — MCP tool schemas for 10 curated primitives
* ``defipy.twin`` — State Twin abstraction with MockProvider (4 recipes) and LiveProvider stub
* MCP server demo — verified live against Claude Desktop
* 629 tests, 125 new in v2.0
* Packaging fixes for all primitive sub-packages
* Zero breaking changes from v1.2.0

v2.1 (next)
-----------------

**LiveProvider implementation.** On-chain snapshot construction for V2 and V3 pools first (most common protocols). Balancer and Stableswap LiveProviders follow. ``LiveProvider(rpc_url)`` constructor is already stable in v2.0; v2.1 makes ``snapshot()`` functional.

**Multi-format tool schemas.** ``get_schemas("anthropic")`` and ``get_schemas("openai")`` — both derivable from the shipped MCP schemas with envelope-format wrappers. Reference examples in ``python/examples/``.

**Observability module.** ``defipy.observability`` replaces the v2.0 stderr-receipt pattern with a structured event sink and opt-in tracing. Composable with the MCP server's dispatch loop.

**Primitive promotions.** Candidates for promotion from Python-API-only to MCP tool status, as protocol parity and dependency blockers clear:

* ``DetectFeeAnomaly`` — pending multi-protocol support
* ``CompareFeeTiers`` — pending MockProvider multi-fee-tier recipes
* ``EvaluateRebalance`` — pending multi-step reasoning ergonomics assessment

v2.2+ (planned)
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

* ``AssessLiquidityDepth`` — V3 tick-walking to assess concentrated liquidity depth around the active tick
* ``DiscoverPools`` — pool discovery across protocols (stretch goal; overlaps with existing MCP ecosystem tools)

v3.0 (horizon)
-----------------

**defipy.org launch.** Public-facing site with documentation, blog, and community resources. ReadTheDocs continues as the SDK reference; defipy.org becomes the marketing and community surface.

**Theme migration.** ReadTheDocs theme upgrade from ``sphinx_rtd_theme`` to Furo or equivalent modern theme.

**Token considerations.** No token is planned. If a token ever ships, it will be after a stable business case exists — not before. This is a deliberate, cycle-tested discipline. See the project's infrastructure-first positioning: DeFiPy is substrate, not a product.

Changelog
-----------

The full changelog with per-release details is maintained in `CHANGELOG.md <https://github.com/defipy-devs/defipy/blob/main/CHANGELOG.md>`_ in the main repository.

* `v2.0.0 <https://github.com/defipy-devs/defipy/compare/v1.2.0...v2.0.0>`_ — 2026-04-23
* `v1.2.0 <https://github.com/defipy-devs/defipy/releases/tag/v1.2.0>`_ — 2026-04-18
