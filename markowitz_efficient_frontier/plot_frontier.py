import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf


def get_data():
    aapl_df = pd.read_csv('AAPL.csv').Close
    amzn_df = pd.read_csv('AMZN.csv').Close
    googl_df = pd.read_csv('GOOGL.csv').Close
    msft_df = pd.read_csv('MSFT.csv').Close

    print(aapl_df.shape)
    print(amzn_df.shape)
    print(googl_df.shape)
    print(msft_df.shape)

    df = pd.concat([aapl_df, amzn_df, googl_df, msft_df], axis=1)
    df.columns = ['aapl', 'amzn', 'googl', 'msft']
    df.dropna(axis=0, inplace=True)

    return df


def compute_frontier(stock_prices):
    iterations = 100000
    volatility = np.zeros(iterations)
    returns = np.zeros(iterations)
    sharpe_ratio = np.zeros(iterations)

    n_days, n_portfolios = stock_prices.shape

    stock_returns = np.log(stock_prices / stock_prices.shift(1))
    stock_returns.dropna(axis=0, inplace=True)

    for i in range(iterations):
        print("Running {}".format(i))
        weights = np.random.random(n_portfolios)
        weights = weights / weights.sum()
        weights = weights.reshape(-1, 1)

        expected_return = np.sum(weights.flatten() * stock_returns.mean() * 252)
        std_return = np.matmul(np.matmul(weights.T, stock_returns.cov().values), weights) * 252
        std_return = std_return[0][0]
        sr = expected_return / std_return

        returns[i] = expected_return
        volatility[i] = std_return
        sharpe_ratio[i] = sr

    return returns, volatility, sharpe_ratio 


def plot_frontier(returns, volatility, sharpe_ratio):
    plt.figure(figsize=(12, 8))
    plt.scatter(volatility, returns, c=sharpe_ratio, cmap='viridis')
    plt.colorbar(label='Sharpe Ratio')
    plt.xlabel('Volatility')
    plt.ylabel('Return')
    plt.show()


if __name__ == "__main__":
    df = get_data()
    returns, volatility, sharpe_ratio = compute_frontier(df)
    plot_frontier(returns, volatility, sharpe_ratio)
