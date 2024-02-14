from stableswappy.vault import StableswapVault 

# ----------------------------------------------------------------------------------------------- #

class FactoryData():
    pass

# ----------------------------------------------------------------------------------------------- #

class StableswapExchangeData():
    pass

# ----------------------------------------------------------------------------------------------- #


class StableswapExchange():
    
    """ 
        How Stableswap calls liquidity pools and uses the constant weighted product automated market maker

        Parameters
        ---------------
        self.factory_struct : FactoryData
            Factory data
        self.exchg_struct : StableswapExchangeData
            Stableswap exchange data         
    """       
    
    def __init__(self, factory_struct: FactoryData, exchg_struct: StableswapExchangeData):
        pass
        
    def summary(self):
     
        """ 
            Print-out summary on current liquidity pool state   
        """        
        pass    
            
    def join_pool(self, vault : StableswapVault, ampl_coeff : float, to: str):
        
        """ join_pool

            Initialize a Stableswap pool, and add liquidity for all asset deposit
                
            Parameters
            ---------------
            vault : StableswapERC20Group
                Group of ERC20 objects     
            amt_shares_in : float
                Amount of pool shares in      
            to : str
                User name/address                 
        """          
        
        pass   
            
    def swap(self, amt_tkn_in, tkn_in, tkn_out, to):
        
        """ swap

            Swap output token given input token 
                
            Parameters
            ---------------
            amt_tkn_in : float
                Amount of input token requested for swaping   
            tkn_in : ERC20
                Input token           
            tkn_out : ERC20
                Output token                    
            to : str
                User name/address                 
        """          
        
        pass
    
    def add_liquidity(self, tkn_amt_in, tkn_in, to):
        
        """ add_liquidity

            Add token amounts for LP token
                
            Parameters
            ---------------
            amt_shares_in : float
                Amount of pool shares coming in     
            tkn_in : ERC20
                Input token     
            to : str
                User name/address                  
        """    
        
        pass
        
    def remove_liquidity(self, liquidity_amt_out, tkn_out, to, use_fee = True):
        
        """ remove_liquidity

            Remove liquidity from specified token in the pool based on lp amount
                
            Parameters
            ---------------
            to : str
                receiving user address  
            liquidity_amt_out : float
                lp amount to removed                 
            tkn_out : ERC20
                Output token                
        """  
        
        pass
        
        
    def burn(self, liquidity_out, tkn_out_amt, tkn_out, _from):
        
        """ burn

            Burn liquidity from token based on amount of liquidity and amount of token
                
            Parameters
            ---------------
            liquidity_out : float
                Amount of liquidity requested for burn              
            amt_tkn_out : float
                Amount of token requested for burn    
            tkn_out : ERC20
                Output token     
            _from : str
                User name/address                 
        """          
        
        pass
        
    def _burn(self, _from, liquidity_out):
        
        """ burn

            Burn liquidity from token based on amount of liquidity
                
            Parameters
            ---------------
            liquidity_out : float
                Amount of liquidity requested for burn        
            _from : str
                User name/address                 
        """         
        
        pass 
    
    def _swap(self, amt_swap, amt_fee, tkn_out, tkn_in, to): 
        
        """ _swap

            Swap output token given input token 
                
            Parameters
            ---------------
            amt_out : float
                Amount of input token requested for swaping   
            tkn_in : ERC20
                Input token           
            tkn_out : ERC20
                Output token                    
            to : str
                User name/address                 
        """         
        
        pass  
        
        
    def _swap_math_pool(self, amt_tkn_in, tkn_in, tkn_out): 
        
        """ swap_math_pool

            Given some amount of an asset, quotes an equivalent amount of the other asset
                
            Parameters
            ---------------
            amt_tkn_in : float
                Amount of token requested for quote            
            tkn_in : ERC20
                Input token                    
            tkn_out : ERC20
                Output token                    
        """          
        
        pass      
    
    def get_amount_out(self, amt_tkn_in, tkn_in, tkn_out):  
        
        """ get_amount_out

            Given some amount of an asset, quotes an equivalent amount of the other asset
                
            Parameters
            ---------------
            amt_tkn_in : float
                Amount of token requested for quote            
            tkn_in : ERC20
                Input token                    
            tkn_out : ERC20
                Output token                    
        """          
        
        pass
        
    
    def mint(self, new_liquidity, amt_tkn_in, tkn_in, to): 
        
        """ mint

            Update reserve amount for specific token in the pool
                
            Parameters
            ---------------
            new_shares : float
                Amount of new pool shares requested for minting   
            amt_tkn_in : float
                Input token           
            tkn_in : ERC20
                Output token                    
            to : str
                User name/address                 
        """          
        
        pass
    
    def _tally_fees(self, tkn, fee):
        
        
        """ _tally_fees

            Tally fee from swap and record last collected fee
                
            Parameters
            ---------------   
            tkn : ERC20
                Token where fees are being collected for     
            fee : float
                Fee being collected                
        """         
        
        pass
   
    def _mint(self, to, value):
        
        """ _mint

            Update reserve amount for specific token in the pool
                
            Parameters
            ---------------
            value : float
                Amount of new pool shares requested for minting                     
            to : str
                User name/address                 
        """      
                        
        pass
        
    def _update(self, new_balance, tkn_nm):
        
        """ _update

            Update reserve amounts specified token
                
            Parameters
            ---------------   
            new_balance : float
                New reserve amount of token      
            tkn_nm : ERC20
                Name of token being updated                  
        """          
        
        pass          
        
            
    def get_math_pool(self):
        
        """ get_math_pool

            Get underlying StableswapPoolMath object
                
            Parameters
            ---------------
            math_pool : StableswapPoolMath
                Stableswap math implementation from curveresearch github repos                                        
        """          
        
        pass
    


    def get_price(self, base_tkn, opp_tkn, fee = False):
        
        """ get_price

            Get price of select token in the exchange pair
                
            Parameters
            ---------------
            base_tkn : float
                Base token request for price quote           
            opp_tkn : ERC20
                Denomination token of price quote                                     
        """         
        
        pass
    
    def get_reserve(self, token):
        
        """ get_reserve

            Get reserve amount of select token in the pool
                
            Parameters
            ---------------
            token : ERC20
                ERC20 token                
        """            
        
        pass 
            

# ----------------------------------------------------------------------------------------------- #

class StableswapFactory:
    
    """ 
        Create Stableswap liquidity pools for given token sets
        
        Parameters
        ---------------
        self.name : str
            Token name 
        self.address : str
            Address name                   
    """         
      
    def __init__(self, name: str, address: str) -> None:
        pass 
        
    def deploy(self, exchg_data : StableswapExchangeData):   
        
        """ deploy

            Deploy a Stableswap liquidity pool (LP) exchange
                
            Parameters
            -----------------
            exchg_data : StableswapExchangeData
                Exchange initialization data     

            Returns
            -----------------
            exchange : StableswapExchange
                Newly created exchange that is also a LP token                    
        """           
        
        pass 
    
    def get_exchange(self, token):
        
        """ get_exchange

            Get exchange from given token
                
            Parameters
            -----------------
            token : ERC20
                receiving user address      
                
            Returns
            -----------------
            exchange : StableswapExchange
                exchange from mapped token                    
        """          
        
        pass 

    def get_token(self, exchange):       
        
        """ get_token

            Get token set from exchange
                
            Parameters
            -----------------
            exchange : StableswapExchange
                receiving user address      
                
            Returns
            -----------------
            token : ERC20 
                token from mapped exchange                     
        """           
        
        pass 
    
# ----------------------------------------------------------------------------------------------- #    


class CSQuote():
    
    """ 
        Composable stable liquidity pool token quotes (ie, price, reserve and liquidity)
    """         
    
    def get_lp_from_amount(self, lp, tkn, tkn_amt_in):
        
        """ get_lp_from_amount

            Get amount of liquidity, given an amount of input token
                
            Parameters
            -----------------
            lp : UniswapExchange
                Uniswap LP    
            tkn: ERC20
                Token asset from CWPT set  
            amount_in: float
                Amount of input token             

            Returns
            -----------------
            lp_amt: float
                Amount of liquidity
        """    
        
        pass 
             
    
    