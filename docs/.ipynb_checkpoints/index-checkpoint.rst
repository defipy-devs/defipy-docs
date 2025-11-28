DeFiPy: Python SDK for DeFi Analytics and Agents
==============================================================================================

`DeFiPy <https://github.com/defipy-devs/defipy>`_ is the first unified Python SDK for DeFi analytics, simulation, and autonomous agents. It was built with modularity and autonomy in mind, as it is the only OSS Python SDK that treats DeFi agents as first-class citizens and lets you isolate and extend your analytics by protocol using:

* `UniswapPy <https://github.com/defipy-devs/uniswappy>`_
* `BalancerPy <https://github.com/defipy-devs/balancerpy>`_
* `StableswapPy <https://github.com/defipy-devs/stableswappy>`_

For onchain event access and scripting, pair it with `Web3Scout <https://github.com/defipy-devs/web3scout>`_ — a companion tool for `decoding pool events <onchain/pool_events.html>`_ and `interfacing with Solidity contracts <onchain/testnet_sim_univ2.html>`_. Whether you're building dashboards, simulations, or agent-based trading systems, DeFiPy + Web3Scout deliver a uniquely powerful toolset — unlike anything else in the ecosystem.

These docs are intended for anyone who is interfacing with or building with DeFi. Whether you're a trade aggregator, yield aggregator, trader, liquidity provider, founder, web dev, arbitrageur, AMM designer, mathematician, or curious individual, this is the place for you. Check out the `Quick Start <quick/index.html>`_ section for getting started, including how to `install <installation.html>`_ the project.

Check out the `Quick Start <quick/index.html>`_ section for getting started, including how to `install <installation.html>`_ the project.

.. note::

    **📘 Official Textbook - DeFiPy: Python SDK for On-chain Analytics**

    .. grid:: 2
        :gutter: 1

        .. grid-item::
            .. image:: img/book_cover_small.jpg
               :alt: DeFiPy Book Cover
               :width: 75%
               :align: center
               :target: https://www.amazon.com/dp/B0G3RV5QRB

        .. grid-item::
            **🔍 What this book covers:**

            - AMM math and invariants for Uni V2 & V3, Balancer and Stableswap  
            - On-chain analytics and real-world event decoding  
            - Python engineering workflows for DeFi  
            - Risk modeling and liquidity simulations  
            - Agent-based design for DeFi automation  
            - Production-ready pipelines using Web3Scout  
            - `Downloadable Jupyter notebook tutorials <https://github.com/defipy-devs/defipy-book>`_ 

            🔗 `Buy on Amazon >> <https://www.amazon.com/dp/B0G3RV5QRB>`_


Usage
===============


The two main ways to work with DeFiPy are either through the Primitive and/or Abstract API.

.. note::

    It is highly recommended to consider the **Abstract Interface** over the **Primitive Interface**, which makes it an essential tool for rapid prototyping and decision-making. See `Quick Start <quick/index.html>`_ section for more on this.

Primitive Interface
--------------------------

As the DeFiPy backbone consists of refactors of various DeFi (solidity) frameworks to analyze mock DeFi setups using Python, we've done our best to maintain the integrity of the original solidity interface in the pythonized version that we offer. This option is best suited for solidity developers who are familiar with working with solidity interface, and want to use DeFiPy as an additional support resource.

Abstract Interface
--------------------------

This option is best suited for analysts who want to streamline their work to implement DeFi analytics on the various protocols that are made available. The following is an overiew of the available abstract interface objects. To learn more, you can visit Tutorials and/or API references in the left menu.

.. image:: img/abstract_interface.png

Object descriptions are as follows:

1. ``Join()``: Join token amounts amounts to initialize pool with liquidity
2. ``Swap()``: Swap exact token x for token y, and vice versa
3. ``AddLiquidity()``: Double-sided deposit; for Uniswap V2/V3 we enter one token and will calculate the other amount to perform 50/50 deposit; for Balancer/Stableswap enter one token
4. ``RemoveLiquidity()``: Double-sided withdrawal; for Uniswap V2/V3 we enter one token and will calculate the other amount to perform 50/50 withdrawal; for Balancer/Stableswap enter one token
5. ``SwapDeposit()``: Single-sided deposit; deposit exact x or y by coming to pool with just one token from trading pair to make a deposit. Works by calculating portion to swap, performs swap to aquire other token, and performs 50/50 deposit with other token and remaining portion
6. ``WithdrawSwap()``: Single-sided withdrawal; withdraw exact x or y by leaving pool with desired token from trading pair. Works by calculating portion to withdraw, perform approximate 50/50 withdraw, swap remaining portion then return desired token
7. ``LPQuote()``: Quote liquidity pool, via either: (a) token price; (b) LP token amount to token amount; or (c) token amount to LP token amount

Precision
--------------------------

To make DeFiPy usable to the analyst, by default, all output is presented in human form (unless specified). Examples of which include:

+---------+------------------+---------------------------------+---------+
| Format  | Calculation      | Machine                         | Human   |
+=========+==================+=================================+=========+
| GWEI    | price*10^18      | 3000000000000000000000          | 3000    |
+---------+------------------+---------------------------------+---------+
| Q64.96  | sqrt(price)*2^96 | 4339505179874779672736325173248 | 3000    |
+---------+------------------+---------------------------------+---------+

.. note::

    We have implemented a parameter setting to toggle output from human to machine in the event the analyst wants to pipeline their work into any backend development; see `here <uniswapv2/tutorials/machine_precision.html>`_ for Uniswap V2 and `here <uniswapv3/tutorials/machine_precision.html>`_ for Uniswap V3


.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Getting Started

    Home <self>
    quick/index
    book
    installation
    legal

.. toctree::
    :maxdepth: 3
    :hidden:
    :caption: DeFi Math

    math/univ2_math.ipynb
    math/univ3_math.ipynb

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
    :caption: Analytics 

    tutorials/univ2_sim.ipynb    
    tutorials/order_book.ipynb  
    tutorials/imp_loss.ipynb
    tutorials/fsm.ipynb
    tutorials/simple_tree_pt1.ipynb  
    tutorials/simple_tree_pt2.ipynb

.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Onchain 

    onchain/price_threshold_swap.ipynb 
    onchain/tvl_based_liquidity.ipynb 
    onchain/volume_spike_notifier.ipynb 
    onchain/impermanent_loss.ipynb 
    onchain/pool_events.ipynb 
    onchain/testnet_sim_univ2.ipynb   
    
      
.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Abstract API
   
    abstract_uniswap
   
.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Primitive API
   
    primitive_uniswapv2
    primitive_uniswapv3
    primitive_balancer
    primitive_stableswap

   
   
   

