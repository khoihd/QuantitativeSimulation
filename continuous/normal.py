import numpy as np
import time
from scipy.stats import norm

N = pow(10, 9)
mu = 0
sigma = 10

expected_value = mu
variance = sigma**2


# X ~ Uniform[0, 100)
def simulate():
    start_time = time.time()

    samples = []
    sample_squares = np.square(samples)

    print("--------------------------------------------------------")
    print("Empirical Expected Value: {}".format(np.mean(samples)))
    print("Theoretical Expected Value: {}".format(expected_value))

    print("Empirical Variance: {}".format(np.mean(sample_squares) - np.mean(samples) ** 2))
    print("Theoretical Variance: {}".format(variance))

    print("Runtime: {} seconds".format(time.time() - start_time))


def scipy_simulate():
    start_time = time.time()

    samples = norm.rvs(loc=mu, scale=sigma, size=N)
    sample_squares = np.square(samples)

    print("--------------------------------------------------------")
    print("Empirical Expected Value: {}".format(np.mean(samples)))
    print("Theoretical Expected Value: {}".format(expected_value))

    print("Empirical Variance: {}".format(np.mean(sample_squares) - np.mean(samples) ** 2))
    print("Theoretical Variance: {}".format(variance))

    print("Runtime: {} seconds".format(time.time() - start_time))


if __name__ == "__main__":
    # simulate()
    scipy_simulate()
