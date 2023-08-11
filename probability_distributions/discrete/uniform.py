import random
import time
import numpy as np
from scipy.stats import randint

# Discrete uniform distribution U(a, b)
N = pow(10, 7)
a = 0
b = 100

expected = 1/2 * (a+b)
variance = 1/12 * (a-b)**2


def simulation():
    start = time.time()

    sample_space = [i for i in range(a, b+1)]
    sum_of_values = 0
    sum_of_squares = 0
    for _ in range(N):
        sample = random.choice(sample_space)
        sum_of_values += sample  # Could be implemented in a way to avoid overflow
        sum_of_squares += sample**2

    print("--------------------------------------------------------")
    print("Empirical Expected value: {}".format(sum_of_values / N))
    print("Theoretical Expected value: {}".format(expected))

    print("Empirical Variance: {}".format(sum_of_squares/N - (sum_of_values/N)**2))
    print("Theoretical Variance: {}".format(variance))

    print("Takes {} seconds".format(time.time() - start))


def batch_simulation():
    start = time.time()

    sample_space = [i for i in range(a, b+1)]
    samples = np.random.choice(sample_space, N)  # Consume memory to store all samples
    sample_squares = [i**2 for i in samples]

    sum_of_values = sum(samples)
    sum_of_squares = sum(sample_squares)

    print("--------------------------------------------------------")
    print("Empirical Expected value: {}".format(sum_of_values / N))
    print("Theoretical Expected value: {}".format(expected))

    print("Empirical Variance: {}".format(sum_of_squares/N - (sum_of_values/N)**2))
    print("Theoretical Variance: {}".format(variance))

    print("Takes {} seconds".format(time.time() - start))


def scipy_simulation():
    start = time.time()
    u = randint(a, b+1)
    samples = u.rvs(N)
    sample_squares = np.square(samples)

    sum_of_values = np.sum(samples)
    sum_of_squares = np.sum(sample_squares)

    print("--------------------------------------------------------")
    print("Empirical Expected value: {}".format(sum_of_values / N))
    print("Theoretical Expected value: {}".format(expected))

    print("Empirical Variance: {}".format(sum_of_squares/N - (sum_of_values/N)**2))
    print("Theoretical Variance: {}".format(variance))

    print("Takes {} seconds".format(time.time() - start))


if __name__ == "__main__":
    simulation()
    batch_simulation()
    scipy_simulation()
