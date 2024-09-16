DeFiPy: DeFi Analytics with Python
===============================================

Welcome to the worlds first DeFi Analytics Python package with all major protocols integrated into one with `DeFiPy <https://github.com/icmoore/defipy>`_! Since DeFiPy is built with a modular design in mind, you can silo your analytics by protocol using:

* `UniswapPy <https://github.com/defipy-devs/uniswappy>`_
* `BalancerPy <https://github.com/defipy-devs/balancerpy>`_
* `StableswapPy <https://github.com/defipy-devs/stableswappy>`_

For DeFi event surveilance, you can checkout:

* `Web3Scout <https://github.com/defipy-devs/web3scout>`_

Uniswap V2 Example
--------------------------

To setup a liquidity pool, you must first create the tokens in the pair using the ``ERC20`` object. Next, create a liquidity pool (LP) factory using ``UniswapExchangeData`` data class object. Available via :ref:`primitive_uniswapv2` primitive API, and also abstract API tools; see `Abstract Interface (V2) <uniswapv2/tutorials/uniswap_v2.html>`_ for tutorial. For basic setup, see following:

.. code-block:: console

    from defipy import *

    user_nm = 'user_intro'
    eth_amount = 3162.277660168379
    dai_amount = 316227.7660168379
    
    dai = ERC20("DAI", "0x111")
    eth = ERC20("ETH", "0x09")
    exchg_data = UniswapExchangeData(tkn0 = eth, tkn1 = dai, symbol="LP", 
    address="0x011")
    
    factory = UniswapFactory("ETH pool factory", "0x2")
    lp = factory.deploy(exchg_data)
    lp.add_liquidity("user0", eth_amount, dai_amount, eth_amount, dai_amount)
    lp.summary()
    
.. code-block:: console

    #OUTPUT:
    Exchange ETH-DAI (LP)
    Reserves: ETH = 3162.277660168379, DAI = 316227.7660168379
    Liquidity: 31622.776601683792 

Uniswap V3 Example
--------------------------

Simular setup as above, available via :ref:`primitive_uniswapv3` primitive API, and also abstract API tools; see `Abstract Interface (V3) <uniswapv3/tutorials/uniswap_v3.html>`_ for tutorial. Once this is setup, an unlimited amount of LPs can be created. For basic setup, see following:

.. code-block:: console

    from defipy import *

    user = 'user_intro'
    fee = UniV3Utils.FeeAmount.MEDIUM
    tick_spacing = UniV3Utils.TICK_SPACINGS[fee]
    lwr_tick = UniV3Utils.getMinTick(tick_spacing)
    upr_tick = UniV3Utils.getMaxTick(tick_spacing)
    init_price = UniV3Utils.encodePriceSqrt(100, 1)
    
    dai = ERC20("DAI", "0x09")
    eth = ERC20("ETH", "0x111")
    
    exchg_data = UniswapExchangeData(tkn0 = eth, tkn1 = dai, symbol="LP", 
                                       address="0x011", version = 'V3', 
                                       tick_spacing = tick_spacing, 
                                       fee = fee)
    
    factory = UniswapFactory("ETH pool factory", "0x2")
    lp = factory.deploy(exchg_data)
    lp.initialize(init_price)
    out = lp.mint(user, lwr_tick, upr_tick, 31622.776601683792)
    lp.summary()
    
.. code-block:: console

    #OUTPUT:
    Exchange ETH-DAI (LP)
    Reserves: ETH = 3162.277660168379, DAI = 316227.7660168379
    Liquidity: 31622.776601683792 
    
Balancer Example
--------------------------   

Only available via primitive API; see left side menu. This protocol serves as an extension of constant product trading pool (ie, Uniswap) to handle pools with more than two assets, and are known as weighted pools.  As both Balancer and Stableswap are muilt-asset protocols, they have what is called a Vault, which is touted as being the defining feature of these protocols. Hence, we also include ``BalancerVault`` and ``StableswapVault`` as shown in the following basic setups:

.. code-block:: console

    from defipy import *
    
    USER = 'user_test'

    amt_dai = 10000000
    denorm_wt_dai = 10

    amt_eth = 67738.6361731024
    denorm_wt_eth = 40

    init_pool_shares = 100    

    dai = ERC20("DAI", "0x01")
    dai.deposit(None, amt_dai)

    weth = ERC20("WETH", "0x02")
    weth.deposit(None, amt_eth)

    bgrp = BalancerVault()
    bgrp.add_token(dai, denorm_wt_dai)
    bgrp.add_token(weth, denorm_wt_eth)

    bfactory = BalancerFactory("WETH pool factory", "0x")
    exchg_data = BalancerExchangeData(vault = bgrp, symbol="LP", address="0x1")
    lp = bfactory.deploy(exchg_data)
    lp.join_pool(bgrp, init_pool_shares, USER)
    lp.summary()

.. code-block:: console

    #OUTPUT:
    Balancer Exchange: DAI|WETH (LP)
    Reserves: DAI = 10000000, WETH = 67738.6361731024
    Weights: DAI = 0.2, WETH = 0.8
    Pool Shares: 100 
    
StableSwap Example
--------------------------  

Only available via primitive API; see left side menu. This is a lesser known protocol used to implement Composable Stable Pools which are ideal for setting up stable coin pools. For basic setup, see following:

.. code-block:: console

    from defipy import *
    
    USER = 'user_test'

    AMPL_COEFF = 2000 

    amt_dai = 79566307.559825807715868071
    decimal_dai = 18

    amt_usdc = 81345068.187939
    decimal_usdc = 6

    amt_usdt = 55663250.772939
    decimal_usdt = 6
    
    dai = ERC20("DAI", "0x01", decimal_dai)
    dai.deposit(None, amt_dai)

    usdc = ERC20("USDC", "0x02", decimal_usdc)
    usdc.deposit(None, amt_usdc)

    usdt = ERC20("USDT", "0x03", decimal_usdt)
    usdt.deposit(None, amt_usdt)    
    
    sgrp = StableswapVault()
    sgrp.add_token(dai)
    sgrp.add_token(usdc)
    sgrp.add_token(usdt)    

    sfactory = StableswapFactory("Pool factory", "0x")
    exchg_data = StableswapExchangeData(vault = sgrp, symbol="LP", address="0x11")
    lp = sfactory.deploy(exchg_data)
    lp.join_pool(sgrp, AMPL_COEFF, USER)
    lp.summary()

.. code-block:: console

    #OUTPUT:
    Stableswap Exchange: DAI-USDC-USDT (LP)
    Reserves: DAI = 79566307.55982581, USDC = 81345068.187939, USDT = 55663250.772939
    Liquidity: 216573027.91811988 

Web3Scout Example
--------------------------

To pull DeFi events from on-chain, you can utilize our new Web3Scout package. To include more ABIs, you'll have to fork and implement yourself, however we will be making it customizable, so you can monitor your favorite protocols.  

.. code-block:: console

    from web3scout import *
    
    abi = ABILoad(Platform.UNIV3, JSONContract.UniswapV3Pool)
    connect = ConnectW3(Net.POLYGON)
    connect.apply()
    
    rEvents = RetrieveEvents(connect, abi)
    last_block = rEvents.latest_block()
    start_block = last_block - 15
    dict_events = rEvents.apply(EventType.MINT, start_block=start_block, end_block=last_block)
    dict_events

.. code-block:: console

    {0: {'chain': 'polygon',
      'contract': 'uniswapv3pool',
      'type': 'mint',
      'platform': 'uniswap_v3',
      'pool_address': '0xb6e57ed85c4c9dbfef2a68711e9d6f36c56e0fcb',
      'tx_hash': '0xe499971b5410e766d00bf4467c6b333cda04577f1068bb676debe72331254365',
      'blk_num': 61391083,
      'timestamp': 1725401207,
      'details': {'web3_type': web3._utils.datatypes.Mint,
       'owner': '0xC36442b4a4522E871399CD717aBDD847Ab11FE88',
       'tick_lower': -286090,
       'tick_upper': -284860,
       'liquidity_amount': 884887839988325,
       'amount0': 39958320744269616249,
       'amount1': 17912626}},
     1: {'chain': 'polygon',
      'contract': 'uniswapv3pool',
      'type': 'mint',
      'platform': 'uniswap_v3',
      'pool_address': '0x960fdfe0de1079459493a7e3aa857f8ce0b34016',
      'tx_hash': '0x29d53602b1bbd67734c2e3deba8ad0a55aa84204a6244e720f24ee5160505213',
      'blk_num': 61391092,
      'timestamp': 1725401227,
      'details': {'web3_type': web3._utils.datatypes.Mint,
       'owner': '0xC36442b4a4522E871399CD717aBDD847Ab11FE88',
       'tick_lower': 22600,
       'tick_upper': 40000,
       'liquidity_amount': 7675592444129481120,
       'amount0': 64052149877205455,
       'amount1': 29656680135133456015}}}
