import numpy as np
from scipy.stats import norm

def black_scholes(r, S, K, T, sigma, option_type="Call"):
    """
    Black-Scholes Option Pricing Model
    
    Parameters:
    r : float : risk-free interest rate
    S : float : current stock price
    K : float : strike price
    T : float : time to maturity in years
    sigma : float : volatility of the stock
    option_type : str : 'Call' or 'Put'
    
    Returns:
    price : float : price of the option
    """
    if S <= 0 or K <= 0 or T < 0 or sigma <= 0:
        raise ValueError("All inputs must be positive and T >= 0")

    # Calculate d1 and d2
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    try:
        if option_type == "Call":
            # Call option price
            price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
        elif option_type == "Put":
            # Put option price
            price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
        else:
            raise ValueError("Invalid option type. Choose either 'Call' or 'Put'")
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

    return price

def main():
    # Parameters
    r = 0.01        # Risk-free rate
    S = 30          # Current stock price
    K = 40          # Strike price
    T = 240 / 365   # Time to maturity (240 days = 240/365 years)
    sigma = 0.30    # Volatility of 30%

    # Call Option Pricing
    option_price_call = black_scholes(r, S, K, T, sigma, option_type="Call")
    if option_price_call is not None:
        print(f"Call Option Price: {round(option_price_call, 2)}")
    
    # Put Option Pricing
    option_price_put = black_scholes(r, S, K, T, sigma, option_type="Put")
    if option_price_put is not None:
        print(f"Put Option Price: {round(option_price_put, 2)}")

if __name__ == "__main__":
    main()