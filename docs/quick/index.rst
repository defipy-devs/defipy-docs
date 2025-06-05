Quick Start
=======================

This section outlines the key classes and methods within DeFiPy’s **Abstract Interface**, which are utilized across major DeFi protocols: Uniswap V2, Uniswap V3, Balancer, and StableSwap. The Abstract Interface provides a simplified, high-level abstraction for common operations such as joining pools, swapping tokens, and managing liquidity, making it ideal for rapid prototyping and analytics. The following subsections demonstrate how these Abstract Interface classes are applied, with examples drawn from the document’s listings.

Uniswap V2
----------

The Abstract Interface simplifies Uniswap V2 operations, such as pool creation and liquidity management. While the Primitive Interface offers detailed control (e.g., via ``UniswapFactory`` and ``UniswapExchange``), the Abstract Interface streamlines these tasks, as partially reflected in Listing 2.1, which sets up a pool and adds liquidity.

**Key Abstract Interface Classes**

* **Class**: ``defipy.Join`` 
    * **Purpose**: Simplifies initial liquidity addition to Uniswap V2 pools.
    * **Methods**:
        * ``apply(pool, user: str, amount0: float, amount1: float)``
            * **Parameters**:
                * ``pool``: Pool instance (e.g., created via Primitive Interface).
                * ``user``: User address.
                * ``amount0``: Amount of token0.
                * ``amount1``: Amount of token1.
    * **Output**: Liquidity added to the pool.

- **Class**: ``defipy.Swap``
    * **Purpose**: Facilitates token swaps in Uniswap V2 pools.
    * **Methods**:
        * ``apply(pool, user: str, token_in: str, token_out: str, amount_in: float)``
            * **Parameters**:
                * ``pool``: Pool instance.
                * ``user``: User address.
                * ``token_in``: Input token symbol.
                * ``token_out``: Output token symbol.
                * ``amount_in``: Input amount.
        * **Output**: Tokens swapped.

**Listing: Uniswap V2 Setup and Liquidity Addition**

.. code-block:: python

    from defipy import ERC20, UniswapFactory, UniswapExchangeData, Join, Swap
    
    # Step 1: Define tokens
    tkn = ERC20("TKN", "0x111")
    eth = ERC20("ETH", "0x999")
    
    # Step 2:  Initialize factory
    factory = UniswapFactory("ETH pool factory", "0x2")
    
    # Step 3: Set up exchange data for V2
    exch_data = UniswapExchangeData(tkn0=eth, tkn1=tkn, symbol="LP", address="0x3")
    
    # Step 4: Deploy pool
    lp = factory.deploy(exch_data)
    
    # Step 5: Add initial liquidity
    join = Join()
    join.apply(lp, "user", 1000, 10000)

    # Step 6: Perform swap
    swap = Swap()
    out = swap.apply(lp, tkn, "user", 10)
    
    # Check reserves and liquidity
    lp.summary()  

.. note::
   While the above code block uses the Primitive Interface (``UniswapFactory`` and ``UniswapExchange``), the Abstract Interface’s ``Join`` class simplifies liquidity addition with a call like ``join.apply(pool, "alice", 100, 100000)``. See `Uniswap V2 tutorial <../uniswapv2/tutorials/uniswap_v2.html>`_ for examples on full usage of abtstract interface.

Uniswap V3
-----------

The Abstract Interface shines in Uniswap V3 by simplifying complex operations like adding liquidity within specific price ranges. Listing 2.2 demonstrates this with the ``Join`` class, abstracting the detailed tick management required by the Primitive Interface.

**Key Abstract Interface Classes**

* **Class**: ``defipy.Join``
    * **Purpose**: Adds initial liquidity to Uniswap V3 pools across specified tick ranges.
    * **Methods**:
        * ``apply(pool, user: str, amount0: float, amount1: float, lwr_tick: int, upr_tick: int)``
            * **Parameters**:
                * ``pool``: Uniswap V3 pool instance.
                * ``user``: User address.
                * ``amount0``: Amount of token0.
                * ``amount1``: Amount of token1.
                * ``lwr_tick``: Lower tick of the price range.
                * ``upr_tick``: Upper tick of the price range.
    * **Output**: Liquidity added to the specified range.

* **Class**: ``defipy.Swap``
    * **Purpose**: Executes swaps in Uniswap V3 pools.
    * **Methods**:
        * ``apply(pool, user: str, token_in: str, token_out: str, amount_in: float)``
            * **Parameters**:
                * ``pool``: Pool instance.
                * ``user``: User address.
                * ``token_in``: Input token symbol.
                * ``token_out``: Output token symbol.
                * ``amount_in``: Input amount.
    * **Output**: Tokens swapped.

**Listing: Uniswap V3 Setup and Liquidity Addition**

.. code-block:: python

    from defipy import ERC20, UniswapFactory, UniswapExchangeData, Join, Swap, UniV3Utils
    
    # Step 1: Define tokens and parameters
    eth = ERC20("ETH", "0x93")
    tkn = ERC20("TKN", "0x111")
    tick_spacing = 60
    fee = 3000  # 0.3% fee tier
    
    # Step 2: Set up exchange data for V3
    exch_data = UniswapExchangeData(tkn0=eth, tkn1=tkn, symbol="LP", address="0x811", version='V3', tick_spacing=tick_spacing, fee=fee)
    
    # Step 3: Initialize factory
    factory = UniswapFactory("ETH pool factory", "0x2")
    
    # Step 4: Deploy pool
    lp = factory.deploy(exch_data)
    
    # Step 5: Add initial liquidity within tick range
    lwr_tick = UniV3Utils.getMinTick(tick_spacing)
    upr_tick = UniV3Utils.getMaxTick(tick_spacing)
    join = Join()
    join.apply(lp, "user", 1000, 10000, lwr_tick, upr_tick)

    # Step 6: Perform swap
    swap = Swap()
    out = swap.apply(lp, tkn, "user", 10)
    
    # Check reserves and liquidity
    lp.summary()

.. note::
   See `Uniswap V3 tutorial <../uniswapv3/tutorials/uniswap_v3.html>`_ for examples on full usage of abtstract interface.

Balancer
--------

For Balancer, the Abstract Interface simplifies multi-token pool management, such as joining weighted pools. The above code block shows pool setup and liquidity addition, which could leverage Abstract Interface classes like ``Join`` for streamlined operations.

**Key Abstract Interface Classes**

* **Class**: ``defipy.Join``
    * **Purpose**: Adds initial liquidity to Balancer weighted pools.
        * **Methods**:
            * ``apply(pool, user: str, amounts: dict)``
                * **Parameters**:
                    * ``pool``: Balancer pool instance.
                    * ``user``: User address.
                    * ``amount``: Input shares.
    * **Output**: Liquidity added proportionally to weights.

* **Class**: ``defipy.Swap``
    * **Purpose**: Executes swaps in Balancer pools.
    * **Methods**:
        * ``apply(pool, user: str, token_in: str, token_out: str, amount_in: float)``
            * **Parameters**:
                * ``pool``: Pool instance.
                * ``user``: User address.
                * ``token_in``: Input token symbol.
                * ``token_out``: Output token symbol.
                * ``amount_in``: Input token amount.
    * **Output**: Tokens swapped.

**Listing: Balancer Setup and Liquidity Addition**

.. code-block:: python

    from defipy import ERC20, BalancerVault, BalancerFactory, BalancerExchangeData, Join, Swap, Proc

    # Step 1: Define tokens
    dai = ERC20("DAI", "0x111")
    usdc = ERC20("USDC", "0x999")
    
    # Step 2: Deposit token amounts
    dai.deposit(None, 10000)
    usdc.deposit(None, 20000)
    
    # Step 3: Setup vault
    vault = BalancerVault()
    vault.add_token(dai, 10)  # Denormalized weight for DAI
    vault.add_token(usdc, 40)  # Denormalized weight for WETH
    
    # Step 4: Set up exchange data for Balancer
    exch_data = BalancerExchangeData(vault=vault, symbol="BSP", address="0x3")
    
    # Step 5: Initialize factor for Balancer
    bfactory = BalancerFactory("WETH pool factory", "0x2")
    
    # Step 6: Deploy pool
    lp = bfactory.deploy(exch_data)
    
    # Step 7: Join pool with initial liquidity
    join = Join()
    join.apply(lp, "user", 100) # Issue 100 pool shares

    # Step 8: Perform swap
    swap = Swap(Proc.SWAPIN)
    out = swap.apply(lp, dai, usdc, "user", 10)
    
    # Check reserves and liquidity
    lp.summary()

.. note::
   The Abstract Interface’s ``Join`` simplifies the Primitive Interface call with ``join.apply(pool, "alice", 100)`` for a more concise operation.

StableSwap
----------

StableSwap operations, optimized for stablecoins, are simplified by the Abstract Interface, particularly for liquidity addition and swaps. Listing 2.4 demonstrates pool setup and liquidity addition, adaptable to the Abstract Interface.

**Key Abstract Interface Classes**

* **Class**: ``defipy.Join``
    * **Purpose**: Adds initial liquidity to StableSwap pools.
    * **Methods**:
        * ``apply(pool, user: str, token: str, amount: float)``
            * **Parameters**:
                * ``pool``: StableSwap pool instance.
                * ``user``: User address.
                * ``token``: Token symbol to add.
                * ``amount``: Amount to add.
    * **Output**: Liquidity added.

* **Class**: ``defipy.Swap``
    * **Purpose**: Executes swaps in StableSwap pools with low slippage.
    * **Methods**:
        * ``apply(pool, user: str, token_in: str, token_out: str, amount_in: float)``
            * **Parameters**:
                * ``pool``: Pool instance.
                * ``user``: User address.
                * ``token_in``: Input token symbol.
                * ``token_out``: Output token symbol.
                * ``amount_in``: Input amount.
    * **Output**: Tokens swapped.

**Listing: StableSwap Setup and Operations**

.. code-block:: python

    from defipy import ERC20, StableswapVault, StableswapFactory, StableswapExchangeData, Join, Swap

    # Step 1: Define stablecoins and parameters
    dai = ERC20("DAI", "0x111", 18)
    usdc = ERC20("USDC", "0x222", 6)
    AMPL_COEFF = 2000
    
    # Step 2: Deposit token amounts
    dai.deposit(None, 10000)
    usdc.deposit(None, 20000)
    
    # Step 3: Setup Stableswap vault and add tokens
    sgrp = StableswapVault()
    sgrp.add_token(dai)
    sgrp.add_token(usdc)
    
    # Step 4: Set up exchange data for Stableswap
    exch_data = StableswapExchangeData(vault = sgrp, symbol="LP", address="0x011")
    
    # Step 5: Initialize factor for Balancer
    factory = StableswapFactory("Stableswap factory", "0x2")
    
    # Step 6: Deploy pool
    lp = factory.deploy(exch_data)
    
    # Step 7: Join pool with initial liquidity
    join = Join()
    join.apply(lp, "user", AMPL_COEFF)

    # Step 8: Perform swap
    swap = Swap()
    out = swap.apply(lp, dai, usdc, "user", 10)
    
    # Check reserves and liquidity
    lp.summary()

.. note::
   Using the Abstract Interface, this could be simplified to ``join.apply(pool, "alice", 10000)`` for adding liquidity.