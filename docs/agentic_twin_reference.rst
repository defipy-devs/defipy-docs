.. _agentic_twin_reference:

defipy.twin
====================

The ``defipy.twin`` module provides the State Twin abstraction — a protocol-agnostic way to construct exchange objects from declarative pool snapshots.

**Key exports**

* ``StateTwinProvider`` — ABC defining the ``snapshot(pool_id) → PoolSnapshot`` contract
* ``MockProvider`` — synthetic pool snapshots for notebooks, tests, and demos (4 canonical recipes)
* ``LiveProvider`` — on-chain pool snapshots (v2.1; stub ships in v2.0)
* ``StateTwinBuilder`` — dispatches on snapshot type to construct the protocol's exchange object
* ``PoolSnapshot`` — base class; subclasses ``V2PoolSnapshot``, ``V3PoolSnapshot``, ``BalancerPoolSnapshot``, ``StableswapPoolSnapshot``

**Usage**

.. code-block:: python

    from defipy.twin import MockProvider, StateTwinBuilder

    provider = MockProvider()
    snapshot = provider.snapshot("eth_dai_v2")
    lp = StateTwinBuilder().build(snapshot)

    # lp is now a live UniswapExchange — pass it to any primitive
    from defipy import CheckPoolHealth
    result = CheckPoolHealth().apply(lp)

**Available MockProvider recipes**

.. list-table::
   :header-rows: 1
   :widths: 35 25 40

   * - Recipe
     - Protocol
     - Reserves
   * - ``eth_dai_v2``
     - Uniswap V2
     - 1000 ETH / 100000 DAI
   * - ``eth_dai_v3``
     - Uniswap V3
     - 1000 ETH / 100000 DAI, full-range, fee=3000
   * - ``eth_dai_balancer_50_50``
     - Balancer 2-asset
     - 1000 ETH / 100000 DAI, 50/50 weights
   * - ``usdc_dai_stableswap_A10``
     - Stableswap 2-asset
     - 100000 USDC / 100000 DAI, A=10

For the full conceptual treatment — including custom providers, the LiveProvider stub, and the snapshot → builder → primitive pipeline — see :ref:`twin_concept`.
