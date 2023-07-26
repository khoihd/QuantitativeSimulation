import numpy as np
import time
from multiprocessing import Pool, cpu_count
from scipy.stats import nbinom

N = pow(10, 6)
p = 0.02
r = 10
expected_value = r / p
variance = r * (1 - p) / p ** 2


def simulation():
    start_time = time.time()

    samples = np.empty(
        N)  # instead of appending new values, let's initialize a fixed-size array and update its elements instead
    sample_squares = np.empty(N)
    for i in np.arange(N):
        count = 0
        success = 0
        while True:
            count += 1
            # success
            if np.random.random() <= p:
                success += 1
            if success == r:
                break
        samples[i] = count
        sample_squares[i] = count ** 2

    sum_samples = sum(samples)
    sum_of_squares = sum(sample_squares)

    print("--------------------------------------------------------")
    print("Empirical Expected Value: {}".format(sum_samples / N))
    print("Theoretical Expected Value: {}".format(expected_value))

    print("Empirical Variance: {}".format(sum_of_squares / N - (sum_samples / N) ** 2))
    print("Theoretical Variance: {}".format(variance))

    print("Runtime: {} seconds".format(time.time() - start_time))


def batch_simulation():
    start_time = time.time()
    with Pool(cpu_count()) as pool:
        results = pool.map(sample_geometric, range(N))

    sum_samples = 0
    sum_of_squares = 0

    # sum_samples = sum(x[0] for x in results)
    # sum_of_squares = sum(x[1] for x in results)

    # This could be optimized by sharing the variable. Might have some overheads due to the lock.
    for res in results:
        sum_samples += res[0]
        sum_of_squares += res[1]

    print("--------------------------------------------------------")
    print("Empirical Expected Value: {}".format(sum_samples / N))
    print("Theoretical Expected Value: {}".format(expected_value))

    print("Empirical Variance: {}".format(sum_of_squares / N - (sum_samples / N) ** 2))
    print("Theoretical Variance: {}".format(variance))
    #
    print("Runtime: {} seconds".format(time.time() - start_time))


def sample_geometric(idx):
    # Loop until the first success
    count = 0
    success = 0
    while True:
        count += 1
        if np.random.random() <= p:
            success += 1
        if success == r:
            break

    return count, count**2


def scipy_simulation():
    start_time = time.time()
    geometric_prob_dist = nbinom(r, p)
    samples = geometric_prob_dist.rvs(N)
    sample_squares = np.square(samples)

    sum_samples = sum(samples)
    sum_of_squares = sum(sample_squares)

    print("--------------------------------------------------------")
    print("Empirical Expected Value: {}".format(sum_samples / N))
    print("Theoretical Expected Value: {}".format(expected_value))

    print("Empirical Variance: {}".format(sum_of_squares / N - (sum_samples / N) ** 2))
    print("Theoretical Variance: {}".format(variance))

    print("Runtime: {} seconds".format(time.time() - start_time))


if __name__ == "__main__":
    simulation()
    batch_simulation()
    scipy_simulation()
