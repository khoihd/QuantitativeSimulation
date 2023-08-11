import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon, uniform
import time

N = np.power(10, 7)
lambda_par = 3
expected_value = 1 / lambda_par
variance = 1 / lambda_par**2


def inverse_cdf(y):
    return -1/lambda_par * np.log(1-y)


def inverse_cdf_simulation():
    start_time = time.time()

    # inverse_cdf = lambda y: -1 / lambda_par * np.log(1 - y)
    samples = list(map(inverse_cdf, uniform.rvs(0, 1, N)))

    # plt.hist(samples, bins=200)
    # plt.show()

    print("--------------------------------------------------------")
    print("Empirical Expected Value: {}".format(np.mean(samples)))
    print("Theoretical Expected Value: {}".format(expected_value))

    print("Empirical Variance: {}".format(np.var(samples)))
    print("Theoretical Variance: {}".format(variance))

    print("Runtime: {} seconds".format(time.time() - start_time))


def scipy_simulation():
    start_time = time.time()

    samples = expon.rvs(0, 1 / lambda_par, N)

    # plt.hist(samples, bins=200)
    # plt.show()

    print("--------------------------------------------------------")
    print("Empirical Expected Value: {}".format(np.mean(samples)))
    print("Theoretical Expected Value: {}".format(expected_value))

    print("Empirical Variance: {}".format(np.var(samples)))
    print("Theoretical Variance: {}".format(variance))

    print("Runtime: {} seconds".format(time.time() - start_time))


if __name__ == "__main__":
    inverse_cdf_simulation()
    scipy_simulation()
