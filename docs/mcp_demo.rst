.. _mcp_demo:

MCP Server Demo Walkthrough
=============================

The reference MCP server at ``python/mcp/defipy_mcp_server.py`` closes the end-to-end agentic loop: receive a tool call, build a twin, run the primitive, serialize the dataclass result, return it. This page walks through the verified-live session from the v2.0 release.

Four canonical pools are pre-configured via MockProvider; every tool call builds a fresh synthetic twin, runs the primitive, and returns a typed dataclass result.

**Available pool recipes**

.. list-table::
   :header-rows: 1
   :widths: 35 25 40

   * - Recipe
     - Protocol
     - Reserves
   * - ``eth_dai_v2``
     - Uniswap V2
     - 1000 ETH / 100000 DAI
   * - ``eth_dai_v3``
     - Uniswap V3
     - 1000 ETH / 100000 DAI, full-range, fee=3000
   * - ``eth_dai_balancer_50_50``
     - Balancer 2-asset
     - 1000 ETH / 100000 DAI, 50/50 weights
   * - ``usdc_dai_stableswap_A10``
     - Stableswap 2-asset
     - 100000 USDC / 100000 DAI, A=10

Each tool is restricted to the recipes it's compatible with. ``AnalyzeBalancerPosition`` against ``eth_dai_v2`` returns a structured error.

**Running standalone**

.. code-block:: bash

    python python/mcp/defipy_mcp_server.py

The server reads MCP stdio frames on stdin and writes responses on stdout. One line of structured JSON per invocation goes to stderr for observability. Use this for smoke-testing; real use happens through an MCP client.

**The verified-live trace**

The session that validated the v2.0 ship:

* **User message:** *Check the health of the eth_dai_v2 pool.*
* **Claude's tool selection:** ``CheckPoolHealth`` with ``pool_id="eth_dai_v2"``.

**MCP server trace (one line to stderr):**

.. code-block:: json

    {"ts": "2026-04-23T...", "tool": "CheckPoolHealth",
     "pool_id": "eth_dai_v2", "args": {},
     "status": "ok", "duration_ms": 0.31}

**Server-side sequence:**

1. Look up the ``eth_dai_v2`` recipe via ``MockProvider``
2. Build a fresh twin via ``StateTwinBuilder``
3. Instantiate ``CheckPoolHealth()``
4. Call ``.apply(lp=twin)``
5. Serialize the returned ``PoolHealth`` dataclass to JSON
6. Return the JSON to Claude

**Returned dataclass (abbreviated):**

.. code-block:: python

    PoolHealth(
        version="V2",
        token0_name="ETH", token1_name="DAI",
        spot_price=100.0,
        reserve0=1000.0, reserve1=100000.0,
        total_liquidity=10000.0,
        tvl_in_token0=2000.0,
        num_swaps=0,
        num_lps=1, top_lp_share_pct=100.0,
        has_activity=False,
        ...
    )

**Claude's response:** rendered the pool state into prose. Correctly inferred the *"single LP + zero activity = MockProvider initial state"* pattern. Proactively offered ``DetectRugSignals`` as the follow-up for formal risk classification. All numbers matched the recipe exactly.

**What this demonstrates**

The curation principle held. Claude composed ``CheckPoolHealth → (mentions) DetectRugSignals`` based solely on the tool descriptions — no composition primitive in the curated set, no explicit orchestration layer. The LLM did the composing.

The numeraire discipline held. Claude presented TVL in ETH-equivalent (2000 ETH at spot price 100 = 1000 ETH + 100000/100), not USD. This is because the primitive's own dataclass field is ``tvl_in_token0``, which the LLM read and interpreted correctly. The primitives' discipline about what they expose shaped the agent's reasoning quality.

The substrate worked as designed. A DeFi analytics primitive that happens to be callable by an LLM is stable; the v2.0 ship proved this empirically.

.. note::

   The MCP server's 10 tools are a curated subset of the 21 primitives shipped in DeFiPy. See :ref:`tool_schemas` for the curation rationale and :ref:`agentic_categories` for the full primitive catalog.
