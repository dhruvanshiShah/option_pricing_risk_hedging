import numpy as np

def monte_carlo_option_price(S0, K, T, r, sigma, simulations=10000, option_type="Call"):
    """
    Monte Carlo simulation for European option pricing.
    
    Parameters:
    S0 : float : Initial stock price
    K : float : Strike price
    T : float : Time to maturity (in years)
    r : float : Risk-free rate
    sigma : float : Volatility (standard deviation of stock returns)
    simulations : int : Number of Monte Carlo simulations (default=10000)
    option_type : str : "Call" for Call option, "Put" for Put option (default="Call")
    
    Returns:
    float : Estimated option price
    """
    
    # Generate random paths for the underlying asset's price
    Z = np.random.standard_normal(simulations)
    ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    
    # Calculate the payoff for Call or Put options
    if option_type == "Call":
        payoffs = np.maximum(ST - K, 0)
    elif option_type == "Put":
        payoffs = np.maximum(K - ST, 0)
    else:
        raise ValueError("Invalid option type. Choose 'Call' or 'Put'")
    
    # Discount the average payoff to present value
    option_price = np.exp(-r * T) * np.mean(payoffs)
    
    return option_price

# Example usage
def main():
    S0 = 100  # Initial stock price
    K = 100   # Strike price
    T = 1     # Time to maturity (in years)
    r = 0.05  # Annual risk-free rate
    sigma = 0.2  # Volatility (standard deviation)
    simulations = 10000  # Number of Monte Carlo simulations

    # Calculate Call option price
    call_price = monte_carlo_option_price(S0, K, T, r, sigma, simulations, option_type="Call")
    print(f"Monte Carlo Call Option Price: {call_price:.2f}")

    # Calculate Put option price
    put_price = monte_carlo_option_price(S0, K, T, r, sigma, simulations, option_type="Put")
    print(f"Monte Carlo Put Option Price: {put_price:.2f}")

if __name__ == "__main__":
    main()