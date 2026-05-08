.. _agentic_overview:

Overview
====================

.. note::

   The canonical agentic-DeFi documentation lives at
   `defipy.org/agentic-overview <https://defipy.org/agentic-overview/>`_.
   This page is preserved as a stable URL for inbound references; the
   content has been updated for v2.1 factual accuracy but the canonical
   version is on defipy.org.

Large language models are good at reasoning about DeFi positions and poor at computing AMM math. DeFiPy v2 sits in that gap. The 21 analytics primitives shipped in v1 do the math; v2 exposes 10 of them as `Model Context Protocol <https://modelcontextprotocol.io>`_ tools, so an LLM can call them the same way a quant calls them from a notebook.

DeFiPy v2 is not an agent framework. It is substrate. There is no orchestration layer, no memory, no planner, no price-oracle service. The library ships three new modules on top of the v1.2.0 primitives:

* ``defipy.tools`` — emits MCP tool schemas for the 10 curated primitives
* ``defipy.twin`` — a state-source abstraction (MockProvider + LiveProvider both ship in v2.1; LiveProvider supports Uniswap V2 and V3)
* a reference MCP server at ``python/mcp/defipy_mcp_server.py`` that closes the end-to-end loop

The loop was verified live before release: a Claude Desktop session asked *"check the health of the eth_dai_v2 pool,"* the MCP server dispatched ``CheckPoolHealth`` against a MockProvider-built twin, the primitive ran, the result came back, and Claude correctly inferred the pool's state and proactively suggested ``DetectRugSignals`` as a follow-up. No composition primitive was needed — the curation principle (leaf primitives only, let composition happen LLM-side) held in production.

**What this section covers**

* :ref:`tool_schemas` — how ``defipy.tools`` turns a primitive into an MCP tool definition
* :ref:`binding_to_claude` — wiring the shipped MCP server into Claude Desktop and Claude Code
* :ref:`binding_to_other_llms` — the same primitives, other tool-calling interfaces (v2.1)
* :ref:`mcp_demo` — a walkthrough of the reference MCP server, including the full request/response trace from the verified session

The substrate separation is deliberate. A DeFi analytics primitive that happens to be callable by an LLM is stable; an agent framework that happens to call analytics primitives is not. v2 commits to the first posture.

.. note::

   The 10 primitives curated as MCP tools are a subset of the 21 shipped. Every shipped primitive is importable, documented, and tested — the curation is about what makes a good LLM tool, not what's "real." See :ref:`agentic_categories` for the full catalog.
