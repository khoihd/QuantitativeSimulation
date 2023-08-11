import numpy as np
import time
from scipy.stats import poisson

N = pow(10, 8)
lambda_par = 10
expected_value = lambda_par
variance = lambda_par


# TODO:
def simulation():
    None


# TODO:
def batch_simulation():
    None


def scipy_simulation():
    start_time = time.time()
    poisson_prob_dist = poisson(lambda_par)
    samples = poisson_prob_dist.rvs(N)
    sample_squares = np.square(samples)

    sum_samples = sum(samples)
    sum_of_squares = sum(sample_squares)

    print("--------------------------------------------------------")
    print("Empirical Expected Value: {}".format(sum_samples / N))
    print("Theoretical Expected Value: {}".format(expected_value))

    print("Empirical Variance: {}".format(sum_of_squares/N - (sum_samples/N)**2))
    print("Theoretical Variance: {}".format(variance))

    print("Runtime: {} seconds".format(time.time() - start_time))


if __name__ == "__main__":
    simulation()
    batch_simulation()
    scipy_simulation()
