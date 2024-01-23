import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import minimize


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


stock_prices = get_data()
stock_returns = np.log(stock_prices / stock_prices.shift(1))
stock_returns.dropna(axis=0, inplace=True)


def compute_frontier():
    iterations = 100000
    volatility = np.zeros(iterations)
    returns = np.zeros(iterations)
    sharpe_ratio = np.zeros(iterations)

    n_days, n_portfolios = stock_prices.shape

    for i in range(iterations):
        print("Running {}".format(i))
        weights = np.random.random(n_portfolios)
        weights = weights / weights.sum()

        expected_return, std_return, sr = get_sharpe_ratio(weights)

        returns[i] = expected_return
        volatility[i] = std_return
        sharpe_ratio[i] = sr

    return returns, volatility, sharpe_ratio


def minimize_neg_sharpe(weights):
    return -sharpe_ratio[2]


def get_sharpe_ratio(weights):
    weights = weights.reshape(-1, 1)

    expected_return = np.sum(weights.flatten() * stock_returns.mean() * 252)
    std_return = np.matmul(np.matmul(weights.T, stock_returns.cov().values), weights) * 252
    std_return = std_return[0][0]
    sr = expected_return / std_return

    return expected_return, std_return, sr


# Return 0 if the equality constraint is satisfied
def check_sum(weights):
    return sum(weights) - 1


def solve_frontier():
    cons = ({'type': 'eq', 'fun': check_sum})
    bounds = ((0, 1), (0, 1), (0, 1), (0, 1))
    init_guess = [0.25, 0.25, 0.25, 0.25]

    opt_results = minimize(minimize_neg_sharpe, init_guess, bounds=bounds, constraints=cons)
    print(opt_results)
    return opt_results.x


def minimize_volatility(weights):
    return get_sharpe_ratio(weights)[1]


def plot_frontier(returns, volatility, sharpe_ratio):
    plt.figure(figsize=(12, 8))
    plt.scatter(volatility, returns, c=sharpe_ratio, s=10, cmap='viridis')
    plt.colorbar(label='Sharpe Ratio')

    min_ret, max_ret = min(returns), max(returns)
    min_t_ret = np.floor(min_ret * 100) / 100
    max_t_ret = np.ceil(max_ret * 100) / 100

    frontier_x = []
    frontier_y = np.linspace(min_t_ret, max_t_ret, 100)

    print([min_t_ret, max_t_ret])

    for t_ret in frontier_y:
        cons = ({'type': 'eq', 'fun': check_sum},
                {'type': 'eq', 'fun': lambda w: get_sharpe_ratio(w)[0] - t_ret}
                )
        bounds = ((0, 1), (0, 1), (0, 1), (0, 1))
        init_guess = [0.25, 0.25, 0.25, 0.25]

        opt_results = minimize(minimize_volatility, init_guess, bounds=bounds, constraints=cons)
        opt_weights = opt_results.x
        frontier_x.append(get_sharpe_ratio(opt_weights)[1])

    plt.scatter(frontier_x, frontier_y, c='red', s=10)  # red dot
    plt.xlabel('Volatility')
    plt.ylabel('Return')
    plt.show()


if __name__ == "__main__":
    returns, volatility, sharpe_ratio = compute_frontier()
    plot_frontier(returns, volatility, sharpe_ratio)
