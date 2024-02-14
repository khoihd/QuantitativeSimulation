import numpy as np
import pandas as pd
import math
from statsmodels.tsa.stattools import adfuller
from statsmodels.regression.linear_model import OLS
import matplotlib.pyplot as plt


def adf():
    N = 1000
    runs = 100
    alpha, beta = 0.3, 0.7

    for run in range(runs):
        series = np.ones(N) * 10000

        for i in range(2, N):
            series[i] = alpha * series[i - 2] + beta * series[i - 1] + np.random.normal()
        plt.plot(series)
    plt.show()


def adf_price(price_type, return_type, noise=True):
    np.random.seed(1711)
    mu = 2
    alpha = 0.5
    beta = 0.9  # stationary time series
    N = 1000

    trials = 100
    count = 0

    all_returns = []

    for _ in range(trials):
        series = np.zeros(N)
        epsilons = np.zeros(N)
        series[0] = mu
        for t in range(1, N):
            epsilon = np.random.normal() if noise else 0
            epsilons[t] = epsilon

            if price_type == 'raw':
                series[t] = mu + beta*series[t-1] + epsilon
            elif price_type == 'log':
                series[t] = np.exp(mu + beta*np.log(series[t-1]) + epsilon)

            if math.isinf(series[t]) or math.isnan(series[t]):
                print(series[:t+1])

        # plt.plot(series)

        if return_type == 'raw':
            returns = np.diff(series) / series[:-1]

            # time_steps = np.arange(1, N)
            # returns = (mu + alpha*time_steps + epsilons[1:]) / series[:-1] + (beta-1)
        elif return_type == 'log':
            returns = np.diff(np.log(series)) / np.log(series[:-1])

            # time_steps = np.arange(0, N)
            # returns = (mu + alpha*time_steps + + epsilons[1:]) / np.log(series) + (beta-1)

        plt.plot(returns[50:])
        all_returns.append(returns)

        adf_test = adfuller(series, regression='ct')
        adf_stat = adf_test[0]
        adf_1pct = adf_test[4]['1%']

        if adf_stat < adf_1pct:
            count += 1

    all_returns = np.array(all_returns)
    vars_over_time = np.zeros(N-1)
    for t in range(N-1):
        vars_over_time[t] = np.var(all_returns[:, t])

    # plt.plot(vars_over_time[100:], label='Variance Over Time')
    print(vars_over_time)
    plt.legend()

    print("Stationary: {}/{}".format(count, trials))
    print("Non-stationary: {}/{}".format(trials-count, trials))

    plt.show()


def dickey_fuller():
    normal_series = np.random.normal(size=1000)
    normal_series_df = pd.DataFrame(normal_series, columns=['data'])
    normal_series_df['prev'] = normal_series_df.data.shift()
    normal_series_df.dropna(inplace=True)
    normal_series_df['delta'] = normal_series_df.data - normal_series_df.prev

    # delta_y_t = phi * y_{t-1} + epsilon_t
    model = OLS(normal_series_df.delta, normal_series_df.prev)
    ols_result = model.fit()
    print('OLS SE', ols_result.bse)

    est_coeff = ols_result.params[0]
    sd_coeff = ols_result.bse[0]

    test_stat = est_coeff / sd_coeff
    print('test_stat t values', ols_result.tvalues[0])
    print('test_stat', test_stat)

    adf_result = adfuller(normal_series, maxlag=1)
    print('adf_result', adf_result)


def adf_random_walks():
    alpha = 1
    beta = 1  # stationary time series
    N = 1000

    trials = 100
    count = 0

    all_returns = []

    for _ in range(trials):
        series = np.zeros(N)
        series[0] = np.random.normal()
        for t in range(1, N):
            series[t] = alpha*t + beta*series[t - 1] + np.random.normal()

        # Converting the value to log
        returns = np.diff(series) / series[:-1]
        # plt.plot(returns)
        # print(max(returns))
        # plt.plot(series)

        all_returns.append(returns)

        adf_test = adfuller(series, regression='ct')
        adf_stat = adf_test[0]
        adf_1pct = adf_test[4]['1%']

        if adf_stat < adf_1pct:
            count += 1

    all_returns = np.array(all_returns)
    vars_over_time = np.zeros(N - 1)
    for t in range(N - 1):
        vars_over_time[t] = np.var(all_returns[:, t])

    plt.plot(vars_over_time[200:], label='Variance Over Time')
    print(vars_over_time)
    plt.legend()

    print("Stationary: {}/{}".format(count, trials))
    print("Non-stationary: {}/{}".format(trials - count, trials))

    plt.show()


if __name__ == "__main__":
    # dickey_fuller()
    # adf()
    adf_price(price_type='raw', return_type='raw', noise=True)
    # adf_random_walks()