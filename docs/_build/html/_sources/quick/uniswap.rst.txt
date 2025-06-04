Key Classes and Methods
=======================

This section outlines the key classes and methods within DeFiPy’s **Abstract Interface**, which are utilized across major DeFi protocols: Uniswap V2, Uniswap V3, Balancer, and StableSwap. The Abstract Interface provides a simplified, high-level abstraction for common operations such as joining pools, swapping tokens, and managing liquidity, making it ideal for rapid prototyping and analytics. The following subsections demonstrate how these Abstract Interface classes are applied, with examples drawn from the document’s listings.

Uniswap V2
----------

The Abstract Interface simplifies Uniswap V2 operations, such as pool creation and liquidity management. While the Primitive Interface offers detailed control (e.g., via ``UniswapFactory`` and ``UniswapExchange``), the Abstract Interface streamlines these tasks, as partially reflected in Listing 2.1, which sets up a pool and adds liquidity.

**Key Abstract Interface Classes**

- **Class**: ``defipy.Join``
  - **Purpose**: Simplifies liquidity addition to Uniswap V2 pools.
  - **Methods**:
    - ``apply(pool, user: str, amount0: float, amount1: float)``
      - **Parameters**:
        - ``pool``: Pool instance (e.g., created via Primitive Interface).
        - ``user``: User address.
        - ``amount0``: Amount of token0.
        - ``amount1``: Amount of token1.
      - **Output**: Liquidity added to the pool.

- **Class**: ``defipy.Swap``
  - **Purpose**: Facilitates token swaps in Uniswap V2 pools.
  - **Methods**:
    - ``apply(pool, user: str, token_in: str, token_out: str, amount_in: float)``
      - **Parameters**:
        - ``pool``: Pool instance.
        - ``user``: User address.
        - ``token_in``: Input token symbol.
        - ``token_out``: Output token symbol.
        - ``amount_in``: Input amount.
      - **Output**: Tokens swapped.

**Listing 2.1: Uniswap V2 Setup and Liquidity Addition**

.. code-block:: python

   from defipy import UniswapFactory, UniswapExchangeData
   # Create a Uniswap V2 factory (Primitive Interface)
   factory = UniswapFactory(name="UniswapV2")
   # Deploy a pool (Primitive Interface)
   exchg_data = UniswapExchangeData(token0="ETH", token1="USDC", fee=3000)
   pool = factory.deploy(exchg_data)
   # Add liquidity (could be simplified with Abstract Interface 'Join')
   pool.add_liquidity(from_addr="alice", amountADesired=100, amountBDesired=100000, amountAMin=90, amountBMin=90000)

.. note::
   While Listing 2.1 uses the Primitive Interface (``UniswapFactory`` and ``UniswapExchange``), the Abstract Interface’s ``Join`` class could simplify liquidity addition with a call like ``join.apply(pool, "alice", 100, 100000)``.

Uniswap V3
-----------

The Abstract Interface shines in Uniswap V3 by simplifying complex operations like adding liquidity within specific price ranges. Listing 2.2 demonstrates this with the ``Join`` class, abstracting the detailed tick management required by the Primitive Interface.

**Key Abstract Interface Classes**

- **Class**: ``defipy.Join``
  - **Purpose**: Adds liquidity to Uniswap V3 pools across specified tick ranges.
  - **Methods**:
    - ``apply(pool, user: str, amount0: float, amount1: float, lwr_tick: int, upr_tick: int)``
      - **Parameters**:
        - ``pool``: Uniswap V3 pool instance.
        - ``user``: User address.
        - ``amount0``: Amount of token0.
        - ``amount1``: Amount of token1.
        - ``lwr_tick``: Lower tick of the price range.
        - ``upr_tick``: Upper tick of the price range.
      - **Output**: Liquidity added to the specified range.

- **Class**: ``defipy.Swap``
  - **Purpose**: Executes swaps in Uniswap V3 pools.
  - **Methods**:
    - ``apply(pool, user: str, token_in: str, token_out: str, amount_in: float)``
      - **Parameters**:
        - ``pool``: Pool instance.
        - ``user``: User address.
        - ``token_in``: Input token symbol.
        - ``token_out``: Output token symbol.
        - ``amount_in``: Input amount.
      - **Output**: Tokens swapped.

**Listing 2.2: Uniswap V3 Setup and Liquidity Addition**

.. code-block:: python

   from defipy import UniswapV3Pool, Join
   # Create a Uniswap V3 pool (Primitive Interface)
   pool = UniswapV3Pool(token0="ETH", token1="USDC", fee=3000)
   # Initialize the Join interface (Abstract Interface)
   join = Join()
   # Add liquidity to a specific price range using the Abstract Interface
   join.apply(pool, user="alice", amount0=100, amount1=100000, lwr_tick=190000, upr_tick=200000)

Balancer
--------

For Balancer, the Abstract Interface simplifies multi-token pool management, such as joining weighted pools. Listing 2.3 shows pool setup and liquidity addition, which could leverage Abstract Interface classes like ``Join`` for streamlined operations.

**Key Abstract Interface Classes**

- **Class**: ``defipy.Join``
  - **Purpose**: Adds liquidity to Balancer weighted pools.
  - **Methods**:
    - ``apply(pool, user: str, amounts: dict)``
      - **Parameters**:
        - ``pool``: Balancer pool instance.
        - ``user``: User address.
        - ``amounts``: Dictionary of token symbols to amounts (e.g., ``{"ETH": 500, "USDC": 300, "DAI": 200}``).
      - **Output**: Liquidity added proportionally to weights.

- **Class**: ``defipy.Swap``
  - **Purpose**: Executes swaps in Balancer pools.
  - **Methods**:
    - ``apply(pool, user: str, token_in: str, token_out: str, amount_in: float)``
      - **Parameters**:
        - ``pool``: Pool instance.
        - ``user``: User address.
        - ``token_in``: Input token symbol.
        - ``token_out``: Output token symbol.
        - ``amount_in``: Input amount.
      - **Output**: Tokens swapped.

**Listing 2.3: Balancer Setup and Liquidity Addition**

.. code-block:: python

   from defipy import BalancerFactory, BalancerExchangeData
   # Create a Balancer factory (Primitive Interface)
   factory = BalancerFactory(name="Balancer")
   # Deploy a weighted pool (Primitive Interface)
   exchg_data = BalancerExchangeData(tokens=["ETH", "USDC", "DAI"], weights=[0.5, 0.3, 0.2])
   pool = factory.deploy(exchg_data)
   # Add liquidity (Primitive Interface; Abstract 'Join' could simplify)
   pool.join_pool(vault=BalancerVault(), amt_shares_in=1000, to="alice")

.. note::
   The Abstract Interface’s ``Join`` could replace the Primitive Interface call with ``join.apply(pool, "alice", {"ETH": 500, "USDC": 300, "DAI": 200})`` for a more concise operation.

StableSwap
----------

StableSwap operations, optimized for stablecoins, are simplified by the Abstract Interface, particularly for liquidity addition and swaps. Listing 2.4 demonstrates pool setup and liquidity addition, adaptable to the Abstract Interface.

**Key Abstract Interface Classes**

- **Class**: ``defipy.Join``
  - **Purpose**: Adds liquidity to StableSwap pools.
  - **Methods**:
    - ``apply(pool, user: str, token: str, amount: float)``
      - **Parameters**:
        - ``pool``: StableSwap pool instance.
        - ``user``: User address.
        - ``token``: Token symbol to add.
        - ``amount``: Amount to add.
      - **Output**: Liquidity added.

- **Class**: ``defipy.Swap``
  - **Purpose**: Executes swaps in StableSwap pools with low slippage.
  - **Methods**:
    - ``apply(pool, user: str, token_in: str, token_out: str, amount_in: float)``
      - **Parameters**:
        - ``pool``: Pool instance.
        - ``user``: User address.
        - ``token_in``: Input token symbol.
        - ``token_out``: Output token symbol.
        - ``amount_in``: Input amount.
      - **Output**: Tokens swapped.

**Listing 2.4: StableSwap Setup and Operations**

.. code-block:: python

   from defipy import StableSwapFactory, StableSwapExchangeData
   # Create a StableSwap factory (Primitive Interface)
   factory = StableSwapFactory(name="StableSwap")
   # Deploy a stablecoin pool (Primitive Interface)
   exchg_data = StableSwapExchangeData(tokens=["USDC", "DAI"], ampl_coeff=100)
   pool = factory.deploy(exchg_data)
   # Add liquidity (Primitive Interface; Abstract 'Join' could simplify)
   pool.add_liquidity(tkn="USDC", amt_in=10000, to="alice")

.. note::
   Using the Abstract Interface, this could be simplified to ``join.apply(pool, "alice", "USDC", 10000)`` for adding liquidity.