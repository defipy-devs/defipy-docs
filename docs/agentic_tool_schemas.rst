.. _tool_schemas:

Tool Schemas (defipy.tools)
============================

``defipy.tools`` is the module that turns analytics primitives into MCP tool definitions. Its job is narrow: emit JSON schemas, maintain the registry of what's exposed, and nothing else. There is no dispatch logic, no pool resolution, and no LLM-specific adapter code here — that all lives in the MCP server (see :ref:`mcp_demo`).

**Key Classes**

* **Class**: ``defipy.tools.ToolSpec``

    * **Purpose**: Frozen dataclass describing one primitive as a tool: its name, its description, the primitive class, the JSON input schema, and the signature parameters the LLM supplies.
    * **Usage**: Read-only; users don't construct these directly. The registry exposes them.
    * **Fields**: ``name``, ``description``, ``primitive_cls``, ``input_schema``, ``signature_params``

**Module Operations**

* **Function**: ``defipy.tools.get_schemas(format: str = "mcp") -> list[dict]``

    * **Purpose**: Return tool schemas in the requested format. v2.0 supports ``"mcp"`` only; Anthropic tool-use and OpenAI function-calling formats are deferred to v2.1 and derivable from the MCP schemas with small wrappers.
    * **Parameters**:
        * ``format``: ``"mcp"`` (only supported value in v2.0).
    * **Output**: A list of dicts, one per registered tool, each following the MCP tool-definition surface: ``{"name", "description", "inputSchema"}``.
    * **Raises**: ``NotImplementedError`` for any format other than ``"mcp"``.

* **Function**: ``defipy.tools.list_tool_names() -> list[str]``

    * **Purpose**: Return the sorted list of tool names currently in the registry. Useful for test assertions and for introspection at the MCP client.
    * **Output**: List of strings. In v2.0: ``AnalyzePosition``, ``AnalyzeBalancerPosition``, ``AnalyzeStableswapPosition``, ``AssessDepegRisk``, ``CalculateSlippage``, ``CheckPoolHealth``, ``DetectRugSignals``, ``SimulateBalancerPriceMove``, ``SimulatePriceMove``, ``SimulateStableswapPriceMove``.

* **Constant**: ``defipy.tools.TOOL_REGISTRY``

    * **Purpose**: The dict mapping tool name to ``ToolSpec``. Source of truth for which primitives are exposed and what their schemas look like.
    * **Usage**: ``from defipy.tools import TOOL_REGISTRY``
    * **Example**: ``TOOL_REGISTRY["CheckPoolHealth"].input_schema``

**Example: Inspect the shipped tool schemas**

.. code-block:: python

    import json
    from defipy.tools import get_schemas, list_tool_names

    # Step 1: List the 10 curated tools
    print(list_tool_names())

    # Step 2: Get the full MCP schemas
    schemas = get_schemas(format="mcp")

    # Step 3: Inspect one in detail
    check_pool_health = next(s for s in schemas if s["name"] == "CheckPoolHealth")
    print(json.dumps(check_pool_health, indent=2))

**Why these 10, not all 21**

The v2.0 tool set is deliberately curated. Three principles drove the cut:

* **Leaf primitives over composition primitives.** ``AnalyzePosition`` and ``DetectRugSignals`` ship as tools; ``AggregatePortfolio`` does not. An LLM composing ``AnalyzePosition`` three times to reason about a three-position portfolio is a better ergonomic fit than a single tool that demands the LLM assemble a structured multi-position payload up front.
* **Protocol parity or graceful degradation.** Tools that work cleanly across all four AMM families (or degrade transparently when a protocol isn't covered) were preferred over tools that force the LLM to understand per-protocol scope limits.
* **Direct question-to-answer mapping.** Each shipped tool answers a user-visible question in one call. Tools that require the LLM to thread multiple reasoning steps through the tool-use loop (``EvaluateRebalance``, ``CompareProtocols``) are deferred to v2.1+ as the ecosystem matures.

v2.1+ candidate promotions as protocol parity and dependency blockers clear are tracked in :ref:`roadmap`.

.. note::

   Dispatch parameters — ``lp``, ``token_in``, ``depeg_token`` — are deliberately absent from every tool's ``input_schema``. These are supplied by the dispatch layer (the MCP server) from the user's chosen pool, not by the LLM. ``defipy.tools.registry.DISPATCH_SUPPLIED_PARAMS`` is the frozenset that captures this boundary; schema drift tests reference it directly.
