DeFiPy: Python SDK for Agentic DeFi
==============================================================================================

`DeFiPy <https://github.com/defipy-devs/defipy>`_ is a unified Python SDK for agentic DeFi, covering analytics, simulation, and LLM-native tool schemas for autonomous agents. Built with modularity in mind, it exposes DeFi primitives as MCP tools and lets you isolate and extend your analytics by protocol using:

* `UniswapPy <https://github.com/defipy-devs/uniswappy>`_
* `BalancerPy <https://github.com/defipy-devs/balancerpy>`_
* `StableswapPy <https://github.com/defipy-devs/stableswappy>`_

New here? The `Quick Start <quick/index.html>`_ walks through the essential Core Primitives — pool setup, ``Join``, ``Swap`` — protocol by protocol. For onchain event access, pair with `Web3Scout <https://github.com/defipy-devs/web3scout>`_.

🔗 DAPX-Anchor: `anchorregistry.ai/AR-2026-YdPXB5g <https://anchorregistry.ai/AR-2026-YdPXB5g>`_


Where to start
===============

.. grid:: 2
    :gutter: 3

    .. grid-item-card:: 🤖 Building an agent?
        :link: agentic_overview
        :link-type: ref

        Wire DeFiPy's primitives into Claude Desktop, Claude Code, or any MCP-compatible client. 10 curated tools ship with schemas; a reference MCP server closes the end-to-end loop.

    .. grid-item-card:: 📊 Running analytics?
        :link: agentic_categories
        :link-type: ref

        21 stateless, typed primitives across 9 categories — position analysis, risk, pool health, price scenarios, portfolio aggregation. Every primitive returns a structured dataclass.

    .. grid-item-card:: 🔧 Executing swaps & liquidity?
        :link: core_primitives_index
        :link-type: ref

        Cross-protocol execution primitives: ``Join``, ``Swap``, ``AddLiquidity``, ``SwapDeposit``, ``LPQuote``. Unified interface across Uniswap V2, V3, Balancer, and Stableswap.

    .. grid-item-card:: 📐 Learning the math?
        :link: balancer_math
        :link-type: ref

        Hand-derived AMM math for all four protocols. Full derivations for Uniswap V2 and V3 as runnable notebooks; Balancer and Stableswap reference pages with invariants and IL formulas.


Quick install
==============

.. code-block:: console

    pip install defipy

Core install is pure math — no chain reads, no LLM dependencies. For MCP server, chain reads, or Foundry workflows, see :ref:`installation`.


Here's what a primitive call looks like
========================================

.. code-block:: python

    from defipy import AnalyzePosition
    from defipy.twin import MockProvider, StateTwinBuilder

    # Build a synthetic ETH/DAI Uniswap V2 pool
    provider = MockProvider()
    builder = StateTwinBuilder()
    lp = builder.build(provider.snapshot("eth_dai_v2"))

    # Ask the primitive: why is this LP position gaining or losing money?
    result = AnalyzePosition().apply(
        lp,
        lp_init_amt=1.0,
        entry_x_amt=1000,
        entry_y_amt=100000,
    )

    print(f"Diagnosis:   {result.diagnosis}")
    print(f"Net PnL:     {result.net_pnl:.4f}")
    print(f"IL %:        {result.il_percentage:.4f}")
    print(f"Current val: {result.current_value:.4f}")

``MockProvider`` ships canonical synthetic pools; ``StateTwinBuilder`` turns a snapshot into a usable exchange object; any primitive runs against it. The same pattern works against live chain state once ``LiveProvider`` ships in v2.1 — the primitives don't care where the pool state came from.


Learning resources
===================

.. grid:: 2
    :gutter: 2

    .. grid-item::
        .. image:: img/book_cover_small.jpg
           :alt: DeFiPy Book Cover
           :width: 120px
           :align: left
           :target: https://www.amazon.com/dp/B0G3RV5QRB

        **📘 DeFiPy: Python SDK for On-Chain Analytics**

        Textbook covering AMM math, risk modeling, and agent-based simulation.
        `Buy on Amazon → <https://www.amazon.com/dp/B0G3RV5QRB>`_

    .. grid-item::
        .. image:: img/onchain_course_banner.png
           :alt: On-Chain Analytics Foundations
           :width: 120px
           :align: left
           :target: https://defipy.thinkific.com/products/courses/foundations

        **🎓 On-Chain Analytics Foundations**

        Practical course on transforming raw blockchain data into Python analytics pipelines.
        `Take the course → <https://defipy.thinkific.com/products/courses/foundations>`_


.. toctree::
    :maxdepth: 1
    :hidden:

    Home <self>


.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: DeFiPy Ecosystem

    book
    courses
    hackathons
    presentations


.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Getting Started

    quick/index
    quick/whats_new_v2
    installation
    legal


.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Core Primitives

    core_primitives/index


.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Agentic Primitives

    agentic_primitives/index
    primitive_contract
    agentic_tools_reference
    agentic_twin_reference
    agentic_result_dataclasses


.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Agentic DeFi

    agentic_overview
    twin_concept
    agentic_tool_schemas
    binding_to_claude
    binding_to_other_llms
    mcp_demo


.. toctree::
    :maxdepth: 3
    :hidden:
    :caption: DeFi Math

    math/univ2_math.ipynb
    math/univ3_math.ipynb
    math/balancer_math
    math/stableswap_math


.. toctree::
    :maxdepth: 3
    :hidden:
    :caption: Tutorials

    uniswapv2/index
    uniswapv3/index
    balancer/index
    stableswap/index

.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Primitive Classes

    abstract_uniswap


.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Protocol Classes

    primitive_uniswapv2
    primitive_uniswapv3
    primitive_balancer
    primitive_stableswap


.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Roadmap & Changelog

    roadmap
