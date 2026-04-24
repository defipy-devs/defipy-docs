.. _balancer_math:

Balancer Math
====================

Balancer 2-asset weighted pools use a generalized constant-product invariant with configurable token weights:

.. math::

   B_x^{w_x} \cdot B_y^{w_y} = k

where :math:`B_x` and :math:`B_y` are the pool's token balances and :math:`w_x`, :math:`w_y` are the normalized weights (summing to 1). When :math:`w_x = w_y = 0.5`, this reduces to the standard Uniswap V2 constant-product invariant :math:`x \cdot y = k`.

**Spot price**

.. math::

   P = \frac{B_y / w_y}{B_x / w_x}

**Impermanent loss with weights**

For a price change :math:`\alpha = P_{\text{new}} / P_{\text{entry}}`, the impermanent loss for a weighted pool is:

.. math::

   IL(\alpha, w_x) = \frac{\alpha^{w_x}}{w_x \cdot \alpha + (1 - w_x)} - 1

When :math:`w_x = 0.5`, this reduces to the standard :math:`2\sqrt{\alpha}/(1+\alpha) - 1` formula used in Uniswap V2. Asymmetric weights compress or amplify IL exposure depending on the direction of price movement.

**DeFiPy implementation**

DeFiPy's Balancer math lives in `BalancerPy <https://github.com/defipy-devs/balancerpy>`_. The weighted-pool invariant, spot-price calculation, and swap math are implemented in ``balancerpy.cpt.exchg.BalancerExchange``. The impermanent loss formula is implemented in ``balancerpy.analytics.risk.BalancerImpLoss``.

The agentic primitives that consume Balancer math:

* ``AnalyzeBalancerPosition`` — full position decomposition using the weighted IL formula
* ``SimulateBalancerPriceMove`` — project position value at a hypothetical price change

See :ref:`agentic_primitives_by_category` for executable examples.

.. note::

   Full derivation notebook (matching the depth of the Uniswap V2 and V3 math pages) is planned for v2.1.
