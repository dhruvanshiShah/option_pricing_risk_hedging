import numpy as np
from scipy.stats import norm

# Defining variables
r = 0.01       # Risk-free interest rate
S = 30         # Current stock price
K = 40         # Strike price
T = 240 / 365  # Time to maturity in years (240 days)
sigma = 0.30   # Volatility

# Delta: Sensitivity to the price of the underlying asset
def delta(r, S, K, T, sigma, type="Call"):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    try:
        if type == "Call":
            return norm.cdf(d1)
        elif type == "Put":
            return -norm.cdf(-d1)
    except Exception as e:
        print(f"Error Occured: {e}")

# Gamma: Sensitivity to changes in Delta
def gamma(r, S, K, T, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    try:
        return norm.pdf(d1) / (S * sigma * np.sqrt(T))
    except Exception as e:
        print(f"Error Occured: {e}")

# Vega: Sensitivity to volatility
def vega(r, S, K, T, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    try:
        return S * norm.pdf(d1) * np.sqrt(T)
    except Exception as e:
        print(f"Error Occured: {e}")

# Theta: Sensitivity to the passage of time (time decay)
def theta(r, S, K, T, sigma, type="Call"):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    try:
        if type == "Call":
            return - (S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T)) - r * K * np.exp(-r * T) * norm.cdf(d2) / 365
        elif type == "Put":
            return - (S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T)) + r * K * np.exp(-r * T) * norm.cdf(-d2) / 365
    except Exception as e:
        print(f"Error Occured: {e}")

# Rho: Sensitivity to interest rate
def rho(r, S, K, T, sigma, type="Call"):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    try:
        if type == "Call":
            return K * T * np.exp(-r * T) * norm.cdf(d2) / 100
        elif type == "Put":
            return -K * T * np.exp(-r * T) * norm.cdf(-d2) / 100
    except Exception as e:
        print(f"Error Occured: {e}")

if __name__ == "__main__":
    print(f"Delta (Call): {np.round(delta(r, S, K, T, sigma, type='Call'), 3)}")
    print(f"Delta (Put): {np.round(delta(r, S, K, T, sigma, type='Put'), 3)}")
    print(f"Gamma: {np.round(gamma(r, S, K, T, sigma), 3)}")
    print(f"Vega: {np.round(vega(r, S, K, T, sigma), 3)}")
    print(f"Theta (Call): {np.round(theta(r, S, K, T, sigma, type='Call'), 3)}")
    print(f"Theta (Put): {np.round(theta(r, S, K, T, sigma, type='Put'), 3)}")
    print(f"Rho (Call): {np.round(rho(r, S, K, T, sigma, type='Call'), 3)}")
    print(f"Rho (Put): {np.round(rho(r, S, K, T, sigma, type='Put'), 3)}")