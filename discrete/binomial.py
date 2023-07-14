import time
import numpy as np
from scipy.stats import binom

p = 0.3
n = 1000

N = pow(10, 4)
expected = n * p
variance = n * p * (1 - p)


def simulation():
    start_time = time.time()

    total = 0
    total_of_squares = 0

    for _ in range(N):
        success = sum(np.random.random(n) <= 0.3)
        total += success
        total_of_squares += success ** 2

    print("--------------------------------------------------------")
    print("Empirical Expected Value: {}".format(total / N))
    print("Theoretical Expected Value: {}".format(expected))

    print("Empirical Expected Value: {}".format(total_of_squares / N - (total / N) ** 2))
    print("Theoretical Expected Value: {}".format(variance))

    print("Runtime: {} seconds".format(time.time() - start_time))


def batch_simulation():
    start_time = time.time()

    success_counts = np.array([sum(np.random.random(n) <= 0.3) for _ in np.arange(N)])
    total_success = np.sum(success_counts)
    total_success_squares = np.sum(np.power(success_counts, 2))

    print("--------------------------------------------------------")
    print("Empirical Expected Value: {}".format(total_success / N))
    print("Theoretical Expected Value: {}".format(expected))

    print("Empirical Expected Value: {}".format(total_success_squares / N - (total_success / N) ** 2))
    print("Theoretical Expected Value: {}".format(variance))

    print("Runtime: {} seconds".format(time.time() - start_time))


def scipy_simulation():
    start_time = time.time()
    binomial_prob_dist = binom(n, p)
    success_counts = binomial_prob_dist.rvs(N)

    total_success = np.sum(success_counts)
    total_success_squares = np.sum(np.power(success_counts, 2))

    print("--------------------------------------------------------")
    print("Empirical Expected Value: {}".format(total_success / N))
    print("Theoretical Expected Value: {}".format(expected))

    print("Empirical Expected Value: {}".format(total_success_squares / N - (total_success / N) ** 2))
    print("Theoretical Expected Value: {}".format(variance))

    print("Runtime: {} seconds".format(time.time() - start_time))


if __name__ == "__main__":
    simulation()
    batch_simulation()
    scipy_simulation()
