.. _agentic_result_dataclasses:

Result Dataclasses
====================

Every agentic primitive returns a typed dataclass — no raw tuples, no dicts, no strings. Callers (human or LLM) can rely on named fields. This page catalogs the result types returned by the 21 primitives.

**Position Analysis**

* ``PositionAnalysis`` — returned by ``AnalyzePosition``
    * Fields: ``current_value``, ``hold_value``, ``il_percentage``, ``il_with_fees``, ``fee_income``, ``net_pnl``, ``real_apr``, ``diagnosis``

* ``BalancerPositionAnalysis`` — returned by ``AnalyzeBalancerPosition``
    * Fields: ``current_value``, ``hold_value``, ``il_percentage``, ``net_pnl``, ``weight_base``, ``weight_opp``, ``real_apr``, ``diagnosis``

* ``StableswapPositionAnalysis`` — returned by ``AnalyzeStableswapPosition``
    * Fields: ``current_value``, ``hold_value``, ``il_percentage``, ``net_pnl``, ``A``, ``alpha``, ``real_apr``, ``diagnosis``

**Price Scenarios**

* ``PriceMoveScenario`` — returned by ``SimulatePriceMove``
    * Fields: ``projected_value``, ``projected_hold_value``, ``projected_il_percentage``, ``projected_net_pnl``, ``price_change_pct``

* ``BalancerPriceMoveScenario`` — returned by ``SimulateBalancerPriceMove``
    * Fields: ``projected_value``, ``projected_hold_value``, ``projected_il_percentage``, ``projected_net_pnl``, ``price_change_pct``, ``weight_base``, ``weight_opp``

* ``StableswapPriceMoveScenario`` — returned by ``SimulateStableswapPriceMove``
    * Fields: ``projected_value``, ``projected_hold_value``, ``projected_il_percentage``, ``projected_net_pnl``, ``price_change_pct``, ``A``

**Pool Health**

* ``PoolHealth`` — returned by ``CheckPoolHealth``
    * Fields: ``version``, ``token0_name``, ``token1_name``, ``spot_price``, ``reserve0``, ``reserve1``, ``total_liquidity``, ``tvl_in_token0``, ``total_fee0``, ``total_fee1``, ``num_swaps``, ``fee_accrual_rate_recent``, ``num_lps``, ``top_lp_share_pct``, ``has_activity``

* ``RugSignalReport`` — returned by ``DetectRugSignals``
    * Fields: ``tvl_suspiciously_low``, ``single_sided_concentration``, ``inactive_with_liquidity``, ``signals_detected``, ``risk_level``, ``details``, ``pool_health``

* ``FeeAnomalyResult`` — returned by ``DetectFeeAnomaly``
    * Fields: see source at ``defipy.utils.data.FeeAnomalyResult``

**Risk**

* ``TickRangeStatus`` — returned by ``CheckTickRangeStatus``
    * Fields: see source at ``defipy.utils.data.TickRangeStatus``

* ``DepegRiskAssessment`` — returned by ``AssessDepegRisk``
    * Fields: see source at ``defipy.utils.data.DepegRiskAssessment``

**Optimization**

* ``DepositSplitResult`` — returned by ``OptimalDepositSplit``
    * Fields: see source at ``defipy.utils.data.DepositSplitResult``

* ``RebalanceCostReport`` — returned by ``EvaluateRebalance``
    * Fields: see source at ``defipy.utils.data.RebalanceCostReport``

* ``TickRangeEvaluation`` — returned by ``EvaluateTickRanges``
    * Fields: see source at ``defipy.utils.data.TickRangeEvaluation``

**Comparison**

* ``FeeTierComparison`` — returned by ``CompareFeeTiers``
    * Fields: see source at ``defipy.utils.data.FeeTierComparison``

* ``ProtocolComparison`` — returned by ``CompareProtocols``
    * Fields: see source at ``defipy.utils.data.ProtocolComparison``

**Execution**

* ``SlippageAnalysis`` — returned by ``CalculateSlippage``
    * Fields: see source at ``defipy.utils.data.SlippageAnalysis``

* ``MEVDetectionResult`` — returned by ``DetectMEV``
    * Fields: see source at ``defipy.utils.data.MEVDetectionResult``

**Portfolio**

* ``PortfolioAnalysis`` — returned by ``AggregatePortfolio``
    * Fields: ``numeraire``, ``total_value``, ``total_hold_value``, ``total_net_pnl``, ``total_fees``, ``pnl_ranking``, ``shared_exposure_warnings``, ``positions``

* ``PortfolioPosition`` — input dataclass for ``AggregatePortfolio``
    * Fields: ``lp``, ``lp_init_amt``, ``entry_x_amt``, ``entry_y_amt``, ``entry_amounts``, ``holding_period_days``, ``name``

* ``PositionSummary`` — per-position entry inside ``PortfolioAnalysis.positions``
    * Fields: ``name``, ``protocol``, ``net_pnl``, ``il_percentage``, ``fee_income``, ``tokens``, ``analysis``

**Break-Even**

* ``BreakEvenAlphas`` — returned by ``FindBreakEvenPrice``
    * Fields: see source at ``defipy.utils.data.BreakEvenAlphas``

* ``BreakEvenTime`` — returned by ``FindBreakEvenTime``
    * Fields: see source at ``defipy.utils.data.BreakEvenTime``

.. note::

   Fields listed as "see source" will be expanded with full field documentation when autodoc is wired in Brief 3. The dataclasses whose fields are listed inline above are the most commonly used and were verified during the category notebook drafting.

For the primitive that returns each dataclass, see :ref:`agentic_categories`.
