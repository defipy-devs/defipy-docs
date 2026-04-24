.. _whats_new_v2:

What's new in v2.0
====================

DeFiPy v2.0 makes the library's 21 analytics primitives **agent-ready** without coupling DeFiPy to any specific LLM framework. Three new modules ship on top of the primitives already present in v1.2.0. The library itself remains pure analytics — zero LLM dependencies, zero network calls at core.

**Agentic Primitives — the v2 foundation**

The 21 stateless, typed analytics primitives are the core of v2. Each one follows a three-line contract — stateless construction, computation at ``.apply()``, typed dataclass return — making them callable identically from a notebook or from an LLM via MCP. They cover 9 categories of DeFi analytics:

* **Position Analysis** — decompose LP positions into IL, fee income, net PnL across V2, V3, Balancer, and Stableswap
* **Price Scenarios** — project position value at hypothetical price changes
* **Pool Health** — snapshot pool-level metrics: TVL, LP concentration, fee activity, rug signals
* **Risk** — V3 tick-range status, stableswap depeg exposure
* **Optimization** — optimal deposit splits, rebalance evaluation, tick-range comparison
* **Comparison** — fee-tier comparison, cross-protocol comparison
* **Execution** — slippage calculation, MEV detection
* **Portfolio** — aggregate multi-position portfolios with numeraire enforcement
* **Break-Even** — find the price or holding period where fees compensate IL

10 of the 21 are curated as MCP tools for LLM consumption; all 21 are importable, documented, and tested. See the :ref:`Agentic Primitives Overview <agentic_categories>` for the full availability grid, primitive descriptions, and executable notebook examples for every category.

**defipy.tools**

Self-describing schemas for the 10 curated leaf primitives in `Model Context Protocol <https://modelcontextprotocol.io>`_ (MCP) format. ``get_schemas("mcp")`` returns the schema list; ``TOOL_REGISTRY`` exposes the underlying ``ToolSpec`` entries for programmatic use. Anthropic tool-use and OpenAI function-calling formats are deferred to v2.1 — both are derivable from MCP schemas with small wrappers. See :ref:`tool_schemas` for the full module reference.

**defipy.twin**

The State Twin abstraction. ``StateTwinProvider`` defines the ``snapshot(pool_id) → PoolSnapshot`` contract. ``MockProvider`` ships four canonical synthetic recipes (``eth_dai_v2``, ``eth_dai_v3``, ``eth_dai_balancer_50_50``, ``usdc_dai_stableswap_A10``). ``LiveProvider`` ships as a stub with a stable constructor — functional implementation lands in v2.1. See :ref:`twin_concept` for the full treatment.

**MCP server demo**

A reference stdio-transport server at ``python/mcp/defipy_mcp_server.py`` exposes DeFiPy's 10 curated tools to Claude Desktop, Claude Code, or any MCP client. Per-call receipts log as single-line JSON to stderr. See :ref:`binding_to_claude` for setup and :ref:`mcp_demo` for a verified-live walkthrough.

**Test coverage**

629 tests passing. 125 new tests added in v2.0 (52 for ``defipy.tools``, 47 for ``defipy.twin``, 3 packaging smoke tests, 23 MCP server dispatch tests).

**Packaging fixes**

``setup.py`` fully enumerates all sub-packages. v1.2.0 was missing six primitive sub-packages (``comparison``, ``execution``, ``optimization``, ``pool_health``, ``portfolio``, ``risk``) plus two ``analytics.*`` sub-packages — fresh PyPI installs of v1.2.0 were broken on import for several primitives. v2.0 fixes all of it and adds ``test_packaging.py`` as a continuous guard.

**No breaking changes**

All 21 primitives ship with identical behavior to v1.2.0. No breaking changes to primitive signatures, return dataclasses, or composition patterns. Core install (``pip install defipy``) remains dependency-free of chain libraries and LLM libraries. The ``[mcp]`` extra is the only new dependency surface.

**What's deferred to v2.1+**

* ``LiveProvider`` implementation (ABC + stub ship in v2.0; on-chain snapshot construction is v2.1)
* ``defipy.observability`` module (stderr receipts are the v2.0 observability surface; structured event sink with opt-in tracing is v2.1)
* Anthropic tool-use and OpenAI function-calling schema formats
* Planning primitives category (``PlanRebalance``, ``PlanZapIn``, ``PlanExit``)
* Balancer + Stableswap extensions to ``FindBreakEvenPrice``, ``FindBreakEvenTime``, ``CalculateSlippage``
* ``AssessLiquidityDepth`` (V3 tick-walking) and ``DiscoverPools``

See :ref:`roadmap` for the full v2.1+ timeline.
