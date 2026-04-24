.. _agentic_primitive_contract:

The Primitive Contract
========================

Every analytics primitive in DeFiPy follows the same three-line contract:

.. code-block:: python

    primitive = SomePrimitive()                     # Stateless construction
    result    = primitive.apply(lp, *args)          # Computation
    value     = result.<field>                      # Typed dataclass access

This contract is what makes the primitives composable, testable, and exposable as LLM tools without any adapter layer. A quant in a notebook calls ``AnalyzePosition(...).apply(...)`` and reads ``result.il_percentage``. The MCP server wrapping that same primitive for an LLM dispatches ``AnalyzePosition(...).apply(...)`` and returns ``result.il_percentage`` — exactly the same code path. No translation, no branching, no agent-specific glue.

Three invariants hold across all 21 primitives:

* **Stateless construction.** ``SomePrimitive()`` takes no state that affects the math. Any parameters passed at construction time (e.g., ``DetectFeeAnomaly(threshold_bps=10)``) are tuning, not state — calling ``.apply()`` twice with the same arguments returns the same answer.
* **Computation at** ``apply()``. All work happens in one call. Primitives do not subscribe, stream, or maintain internal caches.
* **Typed dataclass return.** Every primitive returns a specific result dataclass (``PositionAnalysis``, ``PriceMoveScenario``, ``PoolHealth``, etc.) with named fields. Nothing is returned as a raw tuple, a dict, or a string. Callers — human or LLM — can rely on field names.

These invariants aren't just stylistic. They're what lets the library serve three audiences with one interface: notebook quants who want typed introspection, LLMs that need JSON-serializable outputs, and agent frameworks that compose primitives into larger tools.

**What this section covers**

* :ref:`agentic_primitives_by_category` — the 9 categories, each listing the primitives that belong and their call signatures
* :ref:`agentic_tools_reference` — ``defipy.tools`` module: schema emission, registry, binding
* :ref:`agentic_twin_reference` — ``defipy.twin`` module: provider interface and snapshot types
* :ref:`agentic_result_dataclasses` — the full catalog of result dataclasses returned by the primitives

.. note::

   "Primitive" here means an analytics primitive — ``AnalyzePosition``, ``CheckPoolHealth``, etc. The word is also used elsewhere in the docs at a lower layer to mean the protocol-bound exchange classes (``UniswapExchange``, ``BalancerExchange``). Those live under :ref:`primitive_uniswapv2` and siblings. The Agentic Primitives section is specifically about the stateless, typed, composable layer — the 21 classes exported from ``defipy.primitives``.
