import numpy as np
import time
from scipy.stats import norm, uniform, bernoulli
import matplotlib.pyplot as plt

N = pow(10, 4)
mu = 0
sigma = 3

expected_value = mu
variance = sigma ** 2


# X = sqrt(-2lnU) * cos(2piV)
# Y = sqrt(-2lnU) * sin(2piV)
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


# Sample standard normal from Uniform(a, b)
def rejection_sampling():
    start_time = time.time()

    a, b = -100, 100
    M = (b - a) / np.sqrt(2 * np.pi)
    uniform_pdf = lambda z: 1 / (b - a)
    normal_pdf = lambda t: 1 / np.sqrt(2 * np.pi) * np.exp(-t ** 2 / 2)
    samples = np.zeros(N)
    uniform_dist = uniform(a, b - a)
    for i in range(N):
        while True:
            x = uniform_dist.rvs(1)
            y = bernoulli.rvs(normal_pdf(x) / (M * uniform_pdf(x)))
            if y:
                samples[i] = x
                break

    plt.hist(samples, bins=200)
    plt.show()

    print("--------------------------------------------------------")
    print("Empirical Expected Value: {}".format(np.mean(samples)))
    print("Theoretical Expected Value: {}".format(0))

    print("Empirical Variance: {}".format(np.var(samples)))
    print("Theoretical Variance: {}".format(1))

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
    # box_muller_simulate()
    # scipy_simulate()
    rejection_sampling()
