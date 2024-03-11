# Portfolio Optimize

A simple Python package for optimizing investment portfolios using historical return data from Yahoo Finance. Users can easily determine the optimal portfolio allocation among a given set of tickers based on the mean-variance optimization method or other algorithms.

## Features

- Easy-to-use interface for defining a portfolio of tickers.
- Supports customization of the data window (in years) for historical data analysis.
- Allows choosing between mean-variance optimization and other optimization algorithms.
- Includes functionality to plot the efficient frontier for the selected portfolio.

## Installation

```
pip install portfolio-optimize
```

## Usage

### Portfolio Optimization

```python
from portfolio_optimize import portfolio_optimize

# Optimize portfolio
optimal_weights = portfolio_optimize(tickers=["MSFT", "AAPL", "GOOG"], window=5, optimization="MV")

print(optimal_weights)
```

### Plotting the Efficient Frontier

```python
from portfolio_optimize import portfolio_optimize

# Plot the efficient frontier for a set of tickers
portfolio_optimize.graph(tickers=["MSFT", "AAPL", "GOOG"], window=5)
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
