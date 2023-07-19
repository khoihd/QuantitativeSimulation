import numpy as np
import time
from scipy.stats import norm, uniform
import matplotlib.pyplot as plt

N = pow(10, 8)
mu = 0
sigma = 3

expected_value = mu
variance = sigma**2


# X ~ Uniform[0, 100)
def box_muller_simulate():
    start_time = time.time()

    U = uniform.rvs(0, 1, N)
    V = uniform.rvs(0, 1, N)

    X = np.sqrt(-2 * np.log(U)) * np.cos(2 * np.pi * V) * sigma + mu
    Y = np.sqrt(-2 * np.log(U)) * np.sin(2 * np.pi * V) * sigma + mu

    # Test by plotting the probability distribution
    plt.hist(X, bins=200)
    plt.show()

    print("--------------------------------------------------------")
    print("Empirical Expected Value: {}".format(np.mean(X)))
    print("Theoretical Expected Value: {}".format(expected_value))

    print("Empirical Variance: {}".format(np.var(X)))
    print("Theoretical Variance: {}".format(variance))

    print("Runtime: {} seconds".format(time.time() - start_time))


def scipy_simulate():
    start_time = time.time()

    samples = norm.rvs(loc=mu, scale=sigma, size=N)

    print("--------------------------------------------------------")
    print("Empirical Expected Value: {}".format(np.mean(samples)))
    print("Theoretical Expected Value: {}".format(expected_value))

    print("Empirical Variance: {}".format(np.var(samples)))
    print("Theoretical Variance: {}".format(variance))

    print("Runtime: {} seconds".format(time.time() - start_time))


if __name__ == "__main__":
    box_muller_simulate()
    # scipy_simulate()
