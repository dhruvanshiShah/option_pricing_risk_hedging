# Option Pricing and Risk Analysis Tool

## Overview

This project provides a Python-based tool for calculating and analyzing option prices and Greeks using various financial models. The tool supports three primary methodologies:

- **Black-Scholes Model**: Calculates European option prices and Greeks.
- **Binomial Tree Model**: Calculates American option prices and supports early exercise.
- **Monte Carlo Simulation**: Estimates option prices using stochastic processes.

The tool is designed for financial analysts and traders to evaluate and manage option portfolios effectively.

## Features

- **Option Pricing Models**: 
  - Black-Scholes for European options.
  - Binomial Tree for American options.
  - Monte Carlo Simulation for complex and stochastic option pricing.

- **Option Greeks Calculation**:
  - Delta
  - Gamma
  - Vega
  - Theta
  - Rho

## Files

- `binomial_option_pricing_american.py`: Implements the Binomial Tree model for American options pricing.
- `black_scholes_model.py`: Contains the Black-Scholes model for European options pricing and Greeks.
- `monte_carlo_option_pricing.py`: Provides Monte Carlo simulation for option pricing.
- `option_greeks.py`: Computes option Greeks using the Black-Scholes model.

## Usage

To use the provided scripts, run each Python file with the desired parameters. For example:

```bash
python binomial_option_pricing_american.py
python black_scholes_model.py
python monte_carlo_option_pricing.py
python option_greeks.py
