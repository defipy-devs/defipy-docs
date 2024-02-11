DeFiPy: DeFi Analytics for Python
===============================================

.. image:: https://readthedocs.org/projects/example-sphinx-basic/badge/?version=latest
    :target: https://example-sphinx-basic.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
    
Decoupled into `UniswapPy <https://github.com/icmoore/uniswappy>`_, `BalancerPy <https://github.com/icmoore/balancerpy>`_, and `StableswapPy <https://github.com/icmoore/stableswappy>`_, python packages

Simple Example: Setup a Liquidity Pool
--------------------------------------

To setup a liquidity pool, you must first create the tokens in the pair using the ``ERC20`` object. Next, create a liquidity pool (LP) factory using ``Factory`` object. Once this is setup, an unlimited amount of LPs can be created; the procedure for such is as follows:

.. code-block:: console

    from uniswappy.erc import ERC20
    from uniswappy.cpt.factory import UniswapFactory
    from uniswappy.utils.data import UniswapExchangeData

    user_nm = 'user_intro'
    eth_amount = 1000
    dai_amount = 1000000

    dai = ERC20("DAI", "0x111")
    eth = ERC20("ETH", "0x09")
    exchg_data = UniswapExchangeData(tkn0 = eth, tkn1 = dai, symbol="LP", address="0x011")

    factory = UniswapFactory("ETH pool factory", "0x2")
    lp = factory.deploy(exchg_data)
    lp.add_liquidity("user0", eth_amount, dai_amount, eth_amount, dai_amount)
    lp.summary()
    
.. code-block:: console

    #OUTPUT:
    Exchange ETH-DAI (LP)
    Reserves: ETH = 1000, DAI = 1000000
    Liquidity: 31622.776601683792 
