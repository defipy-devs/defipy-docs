from balancerpy.vault import BalancerVault 

# ----------------------------------------------------------------------------------------------- #

class FactoryData():
    pass

# ----------------------------------------------------------------------------------------------- #

class BalancerExchangeData():
    pass

# ----------------------------------------------------------------------------------------------- #

class BalancerExchange():
    
    """ 
        How Balancer calls liquidity pools and uses the constant weighted product automated market maker

        Parameters
        ---------------
        self.factory_struct : FactoryData
            Factory data
        self.exchg_struct : BalancerExchangeData
            Balancer exchange data                  
    """     
    
    def __init__(self, factory_struct: FactoryData, exchg_struct: BalancerExchangeData):
        pass
    
    def summary(self):
        
        
        """ summary
            Summarize current state of balancer liquidity pool
        """         
        
        pass

            
    def join_pool(self, vault : BalancerVault, amt_shares_in: float, to: str):
        
        """ join_pool

            Initialize a Balancer pool, and add liquidity for all asset deposit
                
            Parameters
            ---------------
            tkn_grvaultoup : BalancerERC20Group
                Group of ERC20 objects     
            amt_shares_in : float
                Amount of pool shares in      
            to : str
                User name/address                 
        """          
        
        pass 
    
    def join_swap_extern_amount_in(self, amt_tkn_in, tkn_in, to): 
        
        """ join_swap_extern_amount_in

            Add liquidity via depositing token amount for single asset deposit
                
            Parameters
            ---------------
            amt_tkn_in : float
                Amount of token coming in     
            tkn_in : ERC20
                Input token     
            to : str
                User name/address                 
        """           
        
        pass
        
    def join_swap_pool_amount_out(self, amt_shares_in, tkn_in, to):  
        
        """ join_swap_pool_amount_out

            Add liquidity via depositing shares amount for single asset deposit
                
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
   
    
    def exit_swap_extern_amount_out(self, amt_tkn_out, tkn_out, to):  
          
        """ exit_swap_extern_amount_out

            Remove liquidity via withdrawing shares amount for a single asset 
                
            Parameters
            ---------------
            amt_tkn_out : float
                Amount of token requested for withdrawal    
            tkn_out : ERC20
                Output token     
            to : str
                User name/address                 
        """          
        
        pass
    
    def exit_swap_pool_amount_in(self, amt_shares_out, tkn_out, to):   
        
        """ exit_swap_pool_amount_in

            Remove liquidity via withdrawing shares amount for a single asset 
                
            Parameters
            ---------------
            amt_shares_out : float
                Amount of pool shares requested for withdrawal    
            tkn_out : ERC20
                Output token     
            to : str
                User name/address                 
        """          
        
        pass    
        
    def burn(self, shares, amt_tkn_out, tkn_out, _from):
        
        """ burn

            Burn liquidity from token based on number of pool shares and amount of token
                
            Parameters
            ---------------
            amt_tkn_out : float
                Amount of token requested for burn    
            tkn_out : ERC20
                Output token     
            _from : str
                User name/address                 
        """          
        
        pass
        
    def _burn(self, _from, shares_out):
        
        """ burn

            Burn liquidity from token based on number of pool shares
                
            Parameters
            ---------------
            shares_out : float
                Amount of pool shares requested for burn        
            _from : str
                User name/address                 
        """         
        
        pass 
    
    # remove liquidity: all asset withdrawal
    def exit_pool(self, amt_shares_out, _from):  
        
        """ exit_pool

            Remove liquidity via withdrawing shares amount for all assets within pool 
                
            Parameters
            ---------------
            amt_shares_out : float
                Amount of pool shares requested for exit        
            _from : str
                User name/address                 
        """          
        
        pass
      
    def swap_exact_amount_in(self, amt_tkn_in, tkn_in, tkn_out, to):
        
        """ swap_exact_amount_in

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
    
    def swap_exact_amount_out(self, amt_tkn_out, tkn_out, tkn_in, to):
        
        """ swap_exact_amount_out

            Swap input token given output token 
                
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
    
    
    def swap(self, amt_swap, amt_fee, tkn_out, tkn_in, to): 
        
        """ swap

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
        
    def mint(self, new_shares, amt_tkn_in, tkn_in, to): 
        
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
    
    def get_amount_in(self, amt_tkn_out, tkn_out, tkn_in):  
        
        """ get_amount_in

            Given some amount of an asset, quotes an equivalent amount of the other asset
                
            Parameters
            ---------------
            amt_tkn_out : float
                Amount of token requested for quote            
            tkn_out : ERC20
                Input token                    
            tkn_in : ERC20
                Output token                    
        """          
        
        pass  
        

    def get_price(self, base_tkn, opp_tkn):
        
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


class BalancerFactory():
    
    """ 
        Create Balancer liquidity pools for given token sets
        
        Parameters
        ---------------
        self.name : str
            Token name 
        self.address : str
            Address name            
    """       
      
    def __init__(self, name: str, address: str) -> None:
        pass
        
    def deploy(self, exchg_data : BalancerExchangeData):   
        
        """ deploy

            Deploy a Balancer liquidity pool (LP) exchange
                
            Parameters
            -----------------
            exchg_data : BalancerExchangeData
                Exchange initialization data     

            Returns
            -----------------
            exchange : BalancerExchange
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
            exchange : BalancerExchange
                exchange from mapped token                    
        """                 
        
        pass

    def get_token(self, exchange):      
        
        """ get_token

            Get token set from exchange
                
            Parameters
            -----------------
            exchange : BalancerExchange
                receiving user address      
                
            Returns
            -----------------
            token : ERC20 
                token from mapped exchange                     
        """          
        
        pass
    
    
# ----------------------------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------------------------- #

class CWPQuote():
    
    """ 
        Constant weighted product liquidity pool token quotes (ie, price, reserve and liquidity)
    """ 
        
    def get_amount_from_shares(self, lp, tkn, amount_shares_in):
        
        """ get_amount_from_shares

            Get amount of token reserve, given an amount of input liquidity pool shares
                
            Parameters
            -----------------
            lp : UniswapExchange
                Uniswap LP    
            tkn: ERC20
                Token asset from CWPT set     
            amount_shares_in: float
                Amount of input shares             

            Returns
            -----------------
            amt_out: float
                Amount of token reserve
        """            
        
        pass
 
    
    def get_shares_from_amount(self, lp, tkn, amount_in):
        
        """ get_shares_from_amount

            Get amount of liquidity pool shares, given an amount of input token
                
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
                Amount of liquidity pool shares
        """        
        
        pass 


             
    
    
    
    
    
    