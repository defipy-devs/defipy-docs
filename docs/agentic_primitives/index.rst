.. _agentic_categories:

####################
  Overview
####################

Agentic Primitives are stateless, typed analytics functions that answer questions about DeFi positions, pools, and risk. They follow a three-line contract: stateless construction, computation at ``.apply()``, typed dataclass return. Every primitive works identically whether called from a notebook or from an LLM via the MCP server. See :ref:`agentic_primitive_contract` for the contract invariants.

These primitives **read pool state** — they are analytics operations (position decomposition, risk assessment, price scenarios). For execution operations that mutate pool state (mint, burn, swap, zap), see :ref:`core_primitives_index` under Core Primitives.

**Availability**

.. list-table::
   :header-rows: 1
   :widths: 30 14 14 14 14 14

   * - Primitive
     - V2
     - V3
     - Balancer
     - Stableswap
     - MCP
   * - ``AnalyzePosition``
     - ✅
     - ✅
     - ❌
     - ❌
     - ✅
   * - ``AnalyzeBalancerPosition``
     - ❌
     - ❌
     - ✅
     - ❌
     - ✅
   * - ``AnalyzeStableswapPosition``
     - ❌
     - ❌
     - ❌
     - ✅
     - ✅
   * - ``SimulatePriceMove``
     - ✅
     - ✅
     - ❌
     - ❌
     - ✅
   * - ``SimulateBalancerPriceMove``
     - ❌
     - ❌
     - ✅
     - ❌
     - ✅
   * - ``SimulateStableswapPriceMove``
     - ❌
     - ❌
     - ❌
     - ✅
     - ✅
   * - ``CheckPoolHealth``
     - ✅
     - ✅
     - ❌
     - ❌
     - ✅
   * - ``DetectRugSignals``
     - ✅
     - ✅
     - ❌
     - ❌
     - ✅
   * - ``DetectFeeAnomaly``
     - ✅
     - ❌
     - ❌
     - ❌
     - ❌
   * - ``CheckTickRangeStatus``
     - ❌
     - ✅
     - ❌
     - ❌
     - ❌
   * - ``AssessDepegRisk``
     - ❌
     - ❌
     - ❌
     - ✅
     - ✅
   * - ``OptimalDepositSplit``
     - ✅
     - ❌
     - ❌
     - ❌
     - ❌
   * - ``EvaluateRebalance``
     - ✅
     - ❌
     - ❌
     - ❌
     - ❌
   * - ``EvaluateTickRanges``
     - ❌
     - ✅
     - ❌
     - ❌
     - ❌
   * - ``CompareFeeTiers``
     - ❌
     - ✅
     - ❌
     - ❌
     - ❌
   * - ``CompareProtocols``
     - ✅
     - ✅
     - ✅
     - ✅
     - ❌
   * - ``CalculateSlippage``
     - ✅
     - ✅
     - ❌
     - ❌
     - ✅
   * - ``DetectMEV``
     - ✅
     - ✅
     - ❌
     - ❌
     - ❌
   * - ``AggregatePortfolio``
     - ✅
     - ✅
     - ✅
     - ⚠️
     - ❌
   * - ``FindBreakEvenPrice``
     - ✅
     - ✅
     - ❌
     - ❌
     - ❌
   * - ``FindBreakEvenTime``
     - ✅
     - ✅
     - ❌
     - ❌
     - ❌

**Primitive descriptions**

* ``AnalyzePosition()`` — Decompose a V2/V3 LP position into impermanent loss, fee income, net PnL, and diagnosis.
* ``AnalyzeBalancerPosition()`` — Position decomposition for Balancer weighted pools, accounting for asymmetric token weights.
* ``AnalyzeStableswapPosition()`` — Position decomposition for Stableswap pools, with alpha/unreachable-alpha regime handling.
* ``SimulatePriceMove()`` — Project a V2/V3 position's value at a hypothetical price change.
* ``SimulateBalancerPriceMove()`` — Project a Balancer position's value at a hypothetical price change, respecting pool weights.
* ``SimulateStableswapPriceMove()`` — Project a Stableswap position's value at a hypothetical price change, respecting amplification.
* ``CheckPoolHealth()`` — Snapshot pool-level health metrics: TVL, reserves, LP concentration, fee activity, spot price.
* ``DetectRugSignals()`` — Threshold-based rug-pull signal detector. Composes over ``CheckPoolHealth``.
* ``DetectFeeAnomaly()`` — Detect unusual fee patterns in V2 pools.
* ``CheckTickRangeStatus()`` — V3-only: is the position's tick range still active?
* ``AssessDepegRisk()`` — Stableswap-only: quantify exposure to a stablecoin depeg using the ε ↔ δ relationship.
* ``OptimalDepositSplit()`` — Compute the optimal token split for a single-sided V2 deposit.
* ``EvaluateRebalance()`` — Evaluate whether rebalancing a V2 position is worth the cost.
* ``EvaluateTickRanges()`` — V3-only: compare candidate tick ranges for a position.
* ``CompareFeeTiers()`` — V3-only: compare fee tier options for a position.
* ``CompareProtocols()`` — Cross-protocol comparison of the same token pair across V2, V3, Balancer, and Stableswap.
* ``CalculateSlippage()`` — Compute slippage and price impact for a proposed swap on a V2/V3 pool.
* ``DetectMEV()`` — Detect potential MEV exposure for a swap on a V2/V3 pool.
* ``AggregatePortfolio()`` — Aggregate N LP positions into a single portfolio-level view. Dispatches to per-protocol analyzers.
* ``FindBreakEvenPrice()`` — Find the price at which IL equals fee income for a V2/V3 position.
* ``FindBreakEvenTime()`` — Find the holding period at which fee income compensates IL for a V2/V3 position.

**Relationship to other sections**

Core Primitives and Agentic Primitives are both abstract — they dispatch across protocols without the caller knowing protocol details. The distinction is what they do:

* **Core Primitives** mutate pool state (execution: mint, burn, swap, zap)
* **Agentic Primitives** read pool state and return analytics (position analysis, risk, scenarios)

For the Solidity-derived protocol-specific classes underneath both layers, see :ref:`primitive_uniswapv2` and siblings under Protocol Classes.

.. toctree::
    :maxdepth: 2

    notebooks/position_analysis.ipynb
    notebooks/price_scenarios.ipynb
    notebooks/pool_health.ipynb
    notebooks/risk.ipynb
    notebooks/optimization.ipynb
    notebooks/comparison.ipynb
    notebooks/execution.ipynb
    notebooks/portfolio.ipynb
    notebooks/break_even.ipynb
