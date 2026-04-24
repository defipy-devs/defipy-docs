.. _installation:

Installation
===============

DeFiPy requires **Python 3.10 or later**. Install via pip:

.. code-block:: console

    pip install defipy

The core install is the pure analytics engine — AMM math, primitives, State Twin, and all 21 typed analytics functions. It has **zero web3 dependencies and zero LLM dependencies**. No chain reads, no RPC calls, no MCP. Chain reads come from `Web3Scout <https://github.com/defipy-devs/web3scout>`_ (via the ``[book]`` extra); MCP tool serving comes from the ``[mcp]`` extra. Both are optional.

**MCP install (Claude Desktop / Claude Code demo)**

To run the MCP server that exposes DeFiPy's primitives as tools to Claude Desktop, Claude Code, or any MCP-compatible client, install the ``[mcp]`` extra:

.. code-block:: console

    pip install defipy[mcp]

This adds the `mcp <https://github.com/modelcontextprotocol/python-sdk>`_ Python SDK on top of the core install. The MCP server itself lives at ``python/mcp/defipy_mcp_server.py``; see :ref:`binding_to_claude` for Claude Desktop and Claude Code configuration snippets.

**Book install (chapter 9 agents)**

Chapter 9 of *Hands-On AMMs with Python* — *Building Autonomous DeFi Agents* — uses live chain integration via ``web3scout``. To run those examples, install the ``[book]`` extra:

.. code-block:: console

    pip install defipy[book]

This pulls in ``web3scout`` on top of the core install, enabling the chain event monitoring, ABI loading, and token-fetching utilities that chapter 9's agents require. Other chapters work with the core install alone.

**Anvil install (local Foundry workflows)**

If you're using ``ExecuteScript`` or ``UniswapScriptHelper`` against a local `Anvil <https://book.getfoundry.sh/anvil/>`_ node and don't need the full ``web3scout`` event-monitoring stack, the lighter ``[anvil]`` extra just adds ``web3.py``:

.. code-block:: console

    pip install defipy[anvil]

``[book]`` already includes everything in ``[anvil]``, so book readers only need ``[book]``.

**Source install**

To install from source:

.. code-block:: console

    git clone https://github.com/defipy-devs/defipy
    cd defipy
    pip install .

**System libraries for gmpy2**

DeFiPy depends on ``gmpy2`` for high-precision arithmetic in StableSwap math. On most platforms, ``pip`` will install ``gmpy2`` from a prebuilt wheel and no further setup is needed. If the install fails, you may need the GMP, MPFR, and MPC system libraries installed *before* ``pip install``:

*macOS (Homebrew):*

.. code-block:: console

    brew install gmp mpfr libmpc

*Linux (Debian / Ubuntu):*

.. code-block:: console

    sudo apt install libgmp-dev libmpfr-dev libmpc-dev

See the `gmpy2 installation docs <https://gmpy2.readthedocs.io/en/latest/install.html>`_ for other platforms.
