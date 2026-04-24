.. _core_primitives_index:

Overview
====================

Core Primitives are the cross-protocol execution dispatchers that have been the recommended DeFiPy interface since v1.0. They handle pool initialization, swapping, liquidity management, and quoting across Uniswap V2/V3, Balancer, and Stableswap through a single abstract interface.

These primitives **mutate pool state** — they are execution operations (mint, burn, swap, zap). For read-only analytics (position analysis, risk assessment, price scenarios), see :ref:`agentic_primitive_contract`.

**Availability**

.. list-table::
   :header-rows: 1
   :widths: 25 15 15 15 15

   * - Operation
     - Uniswap V2
     - Uniswap V3
     - Balancer
     - Stableswap
   * - ``Join()``
     - ✅
     - ✅
     - ✅
     - ✅
   * - ``Swap()``
     - ✅
     - ✅
     - ✅
     - ✅
   * - ``AddLiquidity()``
     - ✅
     - ✅
     - ✅
     - ✅
   * - ``RemoveLiquidity()``
     - ✅
     - ✅
     - ✅
     - ✅
   * - ``SwapDeposit()``
     - ✅
     - ✅
     - ❌
     - ❌
   * - ``WithdrawSwap()``
     - ✅
     - ✅
     - ❌
     - ❌
   * - ``LPQuote()``
     - ✅
     - ✅
     - 🔜
     - 🔜

**Operation descriptions**

* ``Join()`` — Join token amounts to initialize pool with liquidity.
* ``Swap()`` — Swap exact token x for token y, and vice versa.
* ``AddLiquidity()`` — Double-sided deposit. For Uniswap V2/V3, enter one token and the other amount is calculated for a 50/50 deposit. For Balancer/Stableswap, enter one token.
* ``RemoveLiquidity()`` — Double-sided withdrawal. For Uniswap V2/V3, enter one token and the other amount is calculated for a 50/50 withdrawal. For Balancer/Stableswap, enter one token.
* ``SwapDeposit()`` — Single-sided deposit. Deposit exact x or y by coming to pool with just one token from the trading pair. Works by calculating portion to swap, performing swap to acquire other token, and performing 50/50 deposit with other token and remaining portion.
* ``WithdrawSwap()`` — Single-sided withdrawal. Withdraw exact x or y by leaving pool with desired token from the trading pair. Works by calculating portion to withdraw, performing approximate 50/50 withdraw, swapping remaining portion, then returning desired token.
* ``LPQuote()`` — Quote liquidity pool via either: (a) token price; (b) LP token amount to token amount; or (c) token amount to LP token amount.

**Relationship to other sections**

Core Primitives and :ref:`agentic_primitive_contract` are both abstract — they dispatch across protocols without the caller knowing protocol details. The distinction is what they do:

* **Core Primitives** mutate pool state (execution: mint, burn, swap, zap)
* **Agentic Primitives** read pool state and return analytics (position analysis, risk, scenarios)

For the Solidity-derived protocol-specific classes underneath both layers, see :ref:`primitive_uniswapv2` and siblings under Protocol Classes.

For the full abstract interface API reference, see :ref:`abstract_uniswap`.
