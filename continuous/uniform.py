import numpy as np
import time
from scipy.stats import uniform

N = pow(10, 9)
a = 50
b = 100

expected_value = (a + b) / 2
variance = (b - a) ** 2 / 12


# X ~ Uniform[0, 100)
def simulate():
    start_time = time.time()

    samples = np.random.random(N) * (b - a) + a
    sample_squares = np.square(samples)

    print("--------------------------------------------------------")
    print("Empirical Expected Value: {}".format(np.mean(samples)))
    print("Theoretical Expected Value: {}".format(expected_value))

    print("Empirical Variance: {}".format(np.mean(sample_squares) - np.mean(samples) ** 2))
    print("Theoretical Variance: {}".format(variance))

    print("Runtime: {} seconds".format(time.time() - start_time))


def scipy_simulate():
    start_time = time.time()

    samples = uniform.rvs(loc=a, scale=b-a, size=N)
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
