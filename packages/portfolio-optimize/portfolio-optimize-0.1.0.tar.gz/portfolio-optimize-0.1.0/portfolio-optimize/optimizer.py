import yfinance as yf
from datetime import datetime, timedelta
from pypfopt import EfficientFrontier, risk_models, expected_returns, plotting
import matplotlib.pyplot as plt

class PortfolioOptimize:
    def __init__(self, tickers, window=5, optimization='MV'):
        self.tickers = tickers
        self.window = window
        self.optimization = optimization
        self.weights = None
        self.ef = None

    def fetch_data(self):
        end_date = datetime.today()
        start_date = end_date - timedelta(days=365 * self.window)
        data = yf.download(self.tickers, start=start_date, end=end_date)['Adj Close']
        return data

    def optimize(self):
        data = self.fetch_data()
        mu = expected_returns.mean_historical_return(data)
        S = risk_models.sample_cov(data)
        
        self.ef = EfficientFrontier(mu, S)
        if self.optimization == 'MV':
            self.weights = self.ef.max_sharpe()
        elif self.optimization == 'MINVOL':
            self.weights = self.ef.min_volatility()
        
        self.ef.portfolio_performance(verbose=True)
        return self.ef.clean_weights()

    def graph(self):
        if self.ef is None:
            print("You must optimize the portfolio before plotting.")
            return
        fig, ax = plt.subplots()
        plotting.plot_efficient_frontier(self.ef, ax=ax, show_assets=True)
        plt.show()

# Example usage
portfolio = PortfolioOptimize(tickers=["MSFT", "AAPL", "GOOG"], window=5, optimization='MV')
optimal_weights = portfolio.optimize()
print(optimal_weights)
# To graph
portfolio.graph()
