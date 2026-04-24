.. _binding_to_other_llms:

Binding to Other LLMs
========================

v2.0 ships MCP schemas only. Anthropic tool-use and OpenAI function-calling adapters are deferred to v2.1 and will be derivable from the shipped MCP schemas with small wrappers.

``defipy.tools.get_schemas(format="anthropic")`` and ``get_schemas(format="openai")`` will raise ``NotImplementedError`` in v2.0. The MCP format is strategically first for v2.0 because MCP is the direction the agent ecosystem is heading — Claude Desktop, Claude Code, and third-party MCP clients all consume it natively. Shipping DeFiPy as MCP-native is stronger positioning than emitting vendor-specific tool-use JSON.

A developer who needs an Anthropic or OpenAI schema today can derive one from the shipped MCP schema directly. The input-schema surface is nearly identical across formats — it's the envelope (description placement, required fields, tool-routing semantics) that differs. For users with an urgent need, a ~30-line adapter script is straightforward.

**What v2.1 will ship**

* ``get_schemas(format="anthropic")`` — returns the list of schemas in Anthropic tool-use JSON shape
* ``get_schemas(format="openai")`` — returns the list in OpenAI function-calling shape
* Reference examples for both in ``python/examples/``

**Workarounds for today**

1. **Roll a derivation script.** Load the MCP schemas via ``get_schemas("mcp")``, transform the envelope. The ``input_schema`` field moves to ``input_schema`` (Anthropic) or ``parameters`` (OpenAI); the ``name`` and ``description`` fields transfer unchanged.
2. **Wait for v2.1.** Timeline tracked in :ref:`roadmap`.

.. note::

   The primitives themselves are LLM-agnostic. Whatever format wraps them, the ``.apply()`` call is the same code path. That's the architectural commitment — the primitive is the tool, regardless of which vendor's tool-use format is in play.
