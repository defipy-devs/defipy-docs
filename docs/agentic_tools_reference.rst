.. _agentic_tools_reference:

defipy.tools
====================

``defipy.tools`` turns analytics primitives into MCP tool definitions. It emits JSON schemas, maintains the registry of what's exposed, and nothing else. Dispatch logic and pool resolution live in the MCP server (see :ref:`mcp_demo`).

**Key exports**

* ``ToolSpec`` — frozen dataclass describing one primitive as a tool: name, description, primitive class, JSON input schema, signature parameters
* ``TOOL_REGISTRY`` — dict mapping tool name to ``ToolSpec``. Source of truth for which primitives are exposed.
* ``get_schemas(format="mcp")`` — returns the full list of MCP tool-definition dicts
* ``list_tool_names()`` — returns the sorted list of registered tool names

**The 10 curated tools (v2.0)**

.. list-table::
   :header-rows: 1
   :widths: 35 35 30

   * - Tool
     - Category
     - Protocol scope
   * - ``AnalyzePosition``
     - Position Analysis
     - V2, V3
   * - ``AnalyzeBalancerPosition``
     - Position Analysis
     - Balancer
   * - ``AnalyzeStableswapPosition``
     - Position Analysis
     - Stableswap
   * - ``SimulatePriceMove``
     - Price Scenarios
     - V2, V3
   * - ``SimulateBalancerPriceMove``
     - Price Scenarios
     - Balancer
   * - ``SimulateStableswapPriceMove``
     - Price Scenarios
     - Stableswap
   * - ``CheckPoolHealth``
     - Pool Health
     - V2, V3
   * - ``DetectRugSignals``
     - Pool Health
     - V2, V3
   * - ``CalculateSlippage``
     - Execution
     - V2, V3
   * - ``AssessDepegRisk``
     - Risk
     - Stableswap

**Usage**

.. code-block:: python

    import json
    from defipy.tools import get_schemas, list_tool_names, TOOL_REGISTRY

    # List the 10 curated tools
    print(list_tool_names())

    # Get the full MCP schemas
    schemas = get_schemas(format="mcp")

    # Inspect one tool's schema
    check_pool_health = next(s for s in schemas if s["name"] == "CheckPoolHealth")
    print(json.dumps(check_pool_health, indent=2))

    # Access the registry directly
    spec = TOOL_REGISTRY["CheckPoolHealth"]
    print(spec.description)
    print(spec.input_schema)

**Curation principles**

Three principles drove the v2.0 tool set:

* **Leaf primitives over composition.** ``AnalyzePosition`` ships as a tool; ``AggregatePortfolio`` does not. An LLM composing ``AnalyzePosition`` three times is a better ergonomic fit than a single tool demanding a structured multi-position payload.
* **Protocol parity or graceful degradation.** Tools that work across all four AMM families were preferred over tools that force the LLM to understand per-protocol scope limits.
* **Direct question-to-answer mapping.** Each tool answers a user-visible question in one call. Tools requiring multi-step reasoning (``EvaluateRebalance``, ``CompareProtocols``) are deferred to v2.1+.

**Dispatch boundary**

Dispatch parameters — ``lp``, ``token_in``, ``depeg_token`` — are absent from every tool's ``input_schema``. These are supplied by the MCP server from the user's chosen pool, not by the LLM. ``DISPATCH_SUPPLIED_PARAMS`` is the frozenset that captures this boundary; schema drift tests reference it directly.

**Format support**

v2.0 supports ``"mcp"`` only. ``get_schemas("anthropic")`` and ``get_schemas("openai")`` raise ``NotImplementedError`` with a v2.1 message. Both formats are derivable from MCP schemas with small envelope wrappers. See :ref:`binding_to_other_llms`.

For the full tool-schema walkthrough, see :ref:`tool_schemas`. For the curation roadmap, see :ref:`roadmap`.
