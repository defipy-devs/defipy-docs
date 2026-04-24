.. _binding_to_claude:

Binding to Claude
====================

DeFiPy v2 ships a reference MCP server at ``python/mcp/defipy_mcp_server.py`` that exposes the 10 curated tools over stdio transport. Wiring the server into Claude Desktop or Claude Code takes one JSON edit and a restart.

**Install the MCP extra**

.. code-block:: bash

    pip install defipy[mcp]

The ``mcp`` extra pulls in the MCP Python SDK. Core DeFiPy (primitives, twin, tools) has no MCP dependency — the server is optional.

**Claude Desktop**

Edit ``~/Library/Application Support/Claude/claude_desktop_config.json`` on macOS. On Linux: ``~/.config/Claude/claude_desktop_config.json``. On Windows: ``%APPDATA%\Claude\claude_desktop_config.json``.

.. code-block:: json

    {
      "mcpServers": {
        "defipy": {
          "command": "/absolute/path/to/venv/bin/python",
          "args": [
            "/absolute/path/to/defipy/python/mcp/defipy_mcp_server.py"
          ]
        }
      }
    }

Restart Claude Desktop. The 10 DeFiPy tools appear in the MCP tool tray (hammer icon).

**Claude Code**

.. code-block:: bash

    claude mcp add defipy \
        /absolute/path/to/venv/bin/python \
        /absolute/path/to/defipy/python/mcp/defipy_mcp_server.py

Alternatively, commit a ``.mcp.json`` at your project root:

.. code-block:: json

    {
      "mcpServers": {
        "defipy": {
          "command": "/absolute/path/to/venv/bin/python",
          "args": ["/absolute/path/to/defipy/python/mcp/defipy_mcp_server.py"]
        }
      }
    }

**Verify the binding**

Open a session and ask one of these:

* "Is the ``eth_dai_v2`` pool healthy? Any rug signals?"
* "I have 10 LP tokens in the ``eth_dai_balancer_50_50`` pool where I deposited 1000 ETH and 100000 DAI. What's my IL if ETH drops 30%?"
* "How exposed is a ``usdc_dai_stableswap_A10`` position to a 5% USDC depeg versus just holding?"

Claude reads the tool descriptions, picks the appropriate tool, picks a compatible pool recipe, calls the MCP server, and returns a structured answer.

**Observing tool calls**

Every tool invocation writes one line of structured JSON to the MCP server's stderr — the v2.0 observability surface.

.. code-block:: json

    {"ts": "2026-04-23T22:31:14.479Z", "tool": "AnalyzePosition",
     "pool_id": "eth_dai_v2", "args": {...}, "status": "ok",
     "duration_ms": 0.26,
     "result_summary": "diagnosis=il_dominant, net_pnl=-1999.80"}

Claude Desktop surfaces MCP stderr through its developer console: **Help → Developer → Toggle Developer Tools**, then the Console tab while tools run.

Claude Code writes MCP stderr to ``~/.claude/mcp-logs/defipy.log`` (verify with your Claude Code version).

**Troubleshooting**

* **Claude Desktop doesn't show tools.** Check the developer console for MCP errors. The most common cause is a path typo in ``claude_desktop_config.json``. Restart the app after every config edit.
* **"Tool call returns 'not compatible with pool'".** Claude picked an incompatible recipe — for example, ``AnalyzeBalancerPosition`` against ``eth_dai_v2``. Either rephrase the question to make the protocol unambiguous, or tell Claude which pool recipe to use.
* **``gmpy2`` compilation fails on install.** ``gmpy2`` needs GMP / MPFR / MPC headers. On macOS: ``brew install gmp mpfr mpc``. On Debian / Ubuntu: ``apt install libgmp-dev libmpfr-dev libmpc-dev``.

.. note::

   The v2.0 MCP server is read-only. No swaps, no signing, no plans — just analytics. Positions, entry amounts, and holding periods come from the user's question, not from chain state. Live chain reads ship in v2.1 via ``LiveProvider`` (see :ref:`twin_concept`).
