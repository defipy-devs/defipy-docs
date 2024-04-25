DeFiPy: DeFi Analytics with Python
===============================================

Welcome to the worlds first DeFi Analytics Python package with all major protocols integrated into one! Implement your analytics in one package with `DeFiPy <https://github.com/icmoore/defipy>`_. Since DeFiPy is built with a modular design in mind, your can also silo your analytics by protocol using:

* `UniswapPy <https://github.com/defipy-devs/uniswappy>`_
* `BalancerPy <https://github.com/defipy-devs/balancerpy>`_
* `StableswapPy <https://github.com/defipy-devs/stableswappy>`_

Uniswap V2 Example
--------------------------

To setup a liquidity pool, you must first create the tokens in the pair using the ``ERC20`` object. Next, create a liquidity pool (LP) factory using ``UniswapExchangeData`` data class object. Available via primitive API, and also abstract API tools such as ``Swap``, ``AddLiquidity``, ``RemoveLiquidity``, ``SwapDeposit``, and ``WithdrawSwap``; see tutorials. Once this is setup, an unlimited amount of LPs can be created; the procedures for such are as follows:

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

Simular setup as Uniswap V2, however only available via primitive API; see left side menu. See following basic setup:

.. code-block:: console

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

Only available via primitive API; see left side menu. This is a lesser known protocol used to implement Composable Stable Pools which are ideal for setting up stable coin pools. See following basic setup:

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
