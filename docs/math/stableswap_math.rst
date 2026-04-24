.. _stableswap_math:

Stableswap Math
====================

Curve-style Stableswap 2-asset pools use an amplified invariant that interpolates between constant-product (:math:`xy = k`) and constant-sum (:math:`x + y = k`) behavior:

.. math::

   A \cdot n^n \cdot (x + y) + D = A \cdot D \cdot n^n + \frac{D^{n+1}}{n^n \cdot x \cdot y}

where :math:`A` is the amplification coefficient, :math:`n = 2` for a 2-asset pool, and :math:`D` is the pool invariant (total liquidity at equal prices). High :math:`A` concentrates liquidity around the 1:1 peg; low :math:`A` behaves more like a standard constant-product pool.

**Amplification coefficient**

:math:`A` controls how tightly the pool prices around peg. At :math:`A = 0`, the pool degrades to constant-product. As :math:`A \to \infty`, the pool approaches constant-sum (zero slippage at peg, catastrophic slippage off-peg). Real-world pools typically use :math:`A` values between 10 and 2000.

**Impermanent loss under depeg**

Stableswap IL behaves differently from constant-product IL. Near peg, IL is suppressed by the amplification factor — the pool holds close to 50/50 reserves even as prices drift slightly. Off peg, IL accelerates sharply because the amplified invariant concentrates liquidity in a narrow price band. The transition between "near peg" and "off peg" depends on :math:`A`: higher :math:`A` means a sharper cliff.

**The ε ↔ δ relationship**

For a depeg of magnitude :math:`\epsilon` (fractional price deviation from peg), the reserve imbalance :math:`\delta` is a function of :math:`A` and :math:`\epsilon`. This relationship is computed numerically via fixed-point iteration rather than closed-form — the invariant equation is transcendental in the general case. DeFiPy's ``AssessDepegRisk`` primitive uses this numerical approach.

**DeFiPy implementation**

DeFiPy's Stableswap math lives in `StableswapPy <https://github.com/defipy-devs/stableswappy>`_. The amplified invariant, swap math, and ``D`` computation are implemented in ``stableswappy.cpt.exchg.StableswapExchange``. The impermanent loss formula is implemented in ``stableswappy.analytics.risk.StableswapImpLoss``.

The agentic primitives that consume Stableswap math:

* ``AnalyzeStableswapPosition`` — full position decomposition with alpha/unreachable-alpha regime handling
* ``SimulateStableswapPriceMove`` — project position value at a hypothetical price change
* ``AssessDepegRisk`` — quantify exposure to a stablecoin depeg using the ε ↔ δ relationship

See :ref:`agentic_primitives_by_category` for executable examples.

.. note::

   Full derivation notebook (matching the depth of the Uniswap V2 and V3 math pages) is planned for v2.1.
