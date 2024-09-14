import numpy as np
from functools import wraps
from time import time

# Timing decorator to measure performance
def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f'func:{f.__name__} args:[{args}, {kw}] took: {te-ts:.4f} sec')
        return result
    return wrap 

@timing
def american_tree(K, T, S0, r, N, u, d, opttype="P"):
    """
    Binomial Tree model for American Option Pricing
    
    Parameters:
    K: Strike price
    T: Time to maturity in years
    S0: Initial stock price
    r: Risk-free interest rate
    N: Number of time steps
    u: Up factor in binomial model
    d: Down factor in binomial model
    opttype: Option type ('P' for Put, 'C' for Call)

    Returns:
    Option price
    """
    dt = T / N  # Time step
    q = (np.exp(r * dt) - d) / (u - d)  # Risk-neutral probability
    disc = np.exp(-r * dt)  # Discount factor per time step
    
    # Stock prices at maturity
    S = S0 * d ** np.arange(N, -1, -1) * u ** np.arange(0, N + 1)
    
    # Payoff at maturity
    C = np.maximum(0, K - S) if opttype == 'P' else np.maximum(0, S - K)
    
    # Backtrack the option price to time 0
    for i in np.arange(N - 1, -1, -1):
        S = S0 * d ** np.arange(i, -1, -1) * u ** np.arange(0, i + 1)  # Update stock prices
        # Compute option prices
        C[:i + 1] = disc * (q * C[1:i + 2] + (1 - q) * C[0:i + 1])  
        # Check for early exercise (American option feature)
        C = np.maximum(C[:-1], K - S) if opttype == 'P' else np.maximum(C[:-1], S - K)

    return C[0]  # Option price at the initial time

def main():
    # Example parameters for American options
    S0 = 100      # Initial stock price
    K = 100       # Strike price
    T = 1         # Time to maturity in years
    r = 0.06      # Annual risk-free rate
    N = 100       # Number of time steps (larger N for accuracy)
    u = 1.1       # Up-factor in binomial models
    d = 1 / u     # Ensure recombining tree
    opttype = 'P' # Option Type: 'P' for Put, 'C' for Call

    # Print the computed American option price
    print(f"American Option Price: {american_tree(K, T, S0, r, N, u, d, opttype):.4f}")

    # Test for a call option
    opttype = 'C'
    print(f"American Call Option Price: {american_tree(K, T, S0, r, N, u, d, opttype):.4f}")

if __name__ == "__main__":
    main()