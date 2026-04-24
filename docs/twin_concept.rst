.. _twin_concept:

State Twin Concept
====================

A State Twin is a live, protocol-specific exchange object built from a declarative pool snapshot. It gives a primitive everything it needs to answer a question — reserves, fees, tick state, weights, amplification coefficient — without the primitive knowing or caring where that state came from. MockProvider builds twins from canonical recipes for notebooks and demos. LiveProvider (v2.1) will build them from live chain reads. Both return the same kind of object; the primitive can't tell the difference.

The separation matters because every primitive in DeFiPy takes an ``lp`` argument. If the primitive had to know whether that ``lp`` was mocked or live, the testability story would collapse — and so would the story of "the same interface for a notebook quant and for an agent." The twin is the indirection that keeps both stories clean.

**Key Classes**

* **Class**: ``defipy.twin.StateTwinProvider``

    * **Purpose**: Abstract base class for any source of pool snapshots. Subclass it to define where snapshots come from.
    * **Usage**: ``class MyProvider(StateTwinProvider): def snapshot(self, pool_id: str) -> PoolSnapshot: ...``
    * **Example**: a worked example for custom providers is included below.

* **Class**: ``defipy.twin.MockProvider``

    * **Purpose**: Synthetic pool snapshots for notebooks, tests, and demos. Ships four canonical recipes.
    * **Usage**: ``MockProvider()``
    * **Example**: ``provider = MockProvider()``
    * **Recipes**: ``eth_dai_v2``, ``eth_dai_v3``, ``eth_dai_balancer_50_50``, ``usdc_dai_stableswap_A10``

* **Class**: ``defipy.twin.LiveProvider`` *(v2.1, stub in v2.0)*

    * **Purpose**: Build twins from live chain reads. Constructor signature is stable (``LiveProvider(rpc_url)``) so v2.1 adoption is not an API break; calling ``.snapshot()`` in v2.0 raises ``NotImplementedError``.
    * **Usage**: ``LiveProvider(rpc_url="https://...")``
    * **Status**: Ships as a stub in v2.0. Functional implementation lands in v2.1.

* **Class**: ``defipy.twin.StateTwinBuilder``

    * **Purpose**: Turn a ``PoolSnapshot`` into a concrete exchange object. Dispatches on snapshot type — V2, V3, Balancer, or Stableswap.
    * **Usage**: ``StateTwinBuilder()``
    * **Example**: ``builder = StateTwinBuilder()``

* **Class**: ``defipy.twin.PoolSnapshot``

    * **Purpose**: Declarative, protocol-agnostic representation of pool state. The discriminated union base class; subclasses (``V2PoolSnapshot``, ``V3PoolSnapshot``, ``BalancerPoolSnapshot``, ``StableswapPoolSnapshot``) carry protocol-specific fields.
    * **Usage**: ``V2PoolSnapshot(pool_id, token0_name, token1_name, reserve0, reserve1)``
    * **Example**: ``snap = V2PoolSnapshot(pool_id="custom_eth_usdc", token0_name="ETH", token1_name="USDC", reserve0=500, reserve1=1000000)``

**Twin Construction Operations**

* **Class**: ``defipy.twin.StateTwinProvider``

    * **Purpose**: Return a pool snapshot for a given pool identifier. ``pool_id`` semantics are provider-specific — a recipe name for MockProvider, a chain address for LiveProvider.
    * **Methods**:
        * ``snapshot(pool_id: str) -> PoolSnapshot``
            * **Parameters**:
                * ``pool_id``: Provider-specific identifier.
    * **Output**: A ``PoolSnapshot`` of the appropriate protocol subclass.

* **Class**: ``defipy.twin.StateTwinBuilder``

    * **Purpose**: Build a protocol-specific exchange object from a snapshot.
    * **Methods**:
        * ``build(snapshot: PoolSnapshot)``
            * **Parameters**:
                * ``snapshot``: A ``V2PoolSnapshot``, ``V3PoolSnapshot``, ``BalancerPoolSnapshot``, or ``StableswapPoolSnapshot``.
    * **Output**: A live exchange object (``UniswapExchange``, ``UniswapV3Exchange``, ``BalancerExchange``, or ``StableswapExchange``) functionally identical to what the ``conftest`` fixtures produce for the same reserves — same ``get_reserve`` outputs, same spot prices, same ``total_supply``.

**Example 1: Build a twin from a MockProvider recipe**

.. code-block:: python

    from defipy import AnalyzePosition
    from defipy.twin import MockProvider, StateTwinBuilder

    # Step 1: Pick a provider
    provider = MockProvider()

    # Step 2: Get a snapshot by pool_id
    snapshot = provider.snapshot("eth_dai_v2")

    # Step 3: Build the twin
    lp = StateTwinBuilder().build(snapshot)

    # Step 4: Run any primitive against it — same interface as a conftest pool
    result = AnalyzePosition().apply(lp, lp_init_amt=10000.0,
                                     entry_x_amt=1000.0, entry_y_amt=100000.0)
    print(result.diagnosis, result.il_percentage)

**Example 2: Build a twin from a custom PoolSnapshot**

For pools outside MockProvider's four canonical recipes, construct a ``PoolSnapshot`` directly and pass it to ``StateTwinBuilder``. MockProvider's recipe registry is bypassed entirely.

.. code-block:: python

    from defipy import CheckPoolHealth
    from defipy.twin import V2PoolSnapshot, StateTwinBuilder

    # Step 1: Declare the pool state
    snap = V2PoolSnapshot(
        pool_id     = "custom_eth_usdc",
        token0_name = "ETH",
        token1_name = "USDC",
        reserve0    = 500.0,
        reserve1    = 1_000_000.0,
    )

    # Step 2: Build the twin
    lp = StateTwinBuilder().build(snap)

    # Step 3: Run any primitive
    health = CheckPoolHealth().apply(lp)
    print(health.spot_price, health.tvl_in_token0)

**Example 3: Write a custom provider**

A custom provider subclasses ``StateTwinProvider`` and implements ``snapshot(pool_id)``. Same contract as MockProvider; different source of truth. This is the hook for fork state, cached blocks, or any snapshot source that isn't live chain (v2.1) and isn't a canned recipe.

.. code-block:: python

    from defipy.twin import StateTwinProvider, V2PoolSnapshot

    class CSVProvider(StateTwinProvider):
        """Load pool state from a per-pool CSV row."""

        def __init__(self, csv_path: str):
            self.rows = self._load(csv_path)

        def snapshot(self, pool_id: str):
            row = self.rows[pool_id]
            return V2PoolSnapshot(
                pool_id     = pool_id,
                token0_name = row["token0"],
                token1_name = row["token1"],
                reserve0    = float(row["reserve0"]),
                reserve1    = float(row["reserve1"]),
            )

        def _load(self, path):
            ...  # implementation elided

.. note::

   MockProvider returns bare exchange objects via the snapshot → builder path; it does not return the test-context dataclass (``.eth``, ``.dai``, ``.entry_x_amt``, etc.) that ``conftest`` fixtures provide. Test context is the caller's responsibility.

.. note::

   ``PoolSnapshot`` stays minimal in v2.0 — no ``block_number``, ``timestamp``, or ``chain_id``. Those are LiveProvider concerns and ship in v2.1 when they're actually needed.
