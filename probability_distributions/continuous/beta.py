import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta as beta_scipy
import time

N = np.power(10, 7)

alpha = 3
beta = 5
expected_value = alpha / (alpha+beta)
variance = alpha * beta / ((alpha+beta+1) * (alpha+beta)**2)


def scipy_simulation():
    start_time = time.time()

    samples = beta_scipy.rvs(alpha, beta, size=N)

    plt.hist(samples, bins=200)
    plt.show()

    print("--------------------------------------------------------")
    print("Empirical Expected Value: {}".format(np.mean(samples)))
    print("Theoretical Expected Value: {}".format(expected_value))

    print("Empirical Variance: {}".format(np.var(samples)))
    print("Theoretical Variance: {}".format(variance))

    print("Runtime: {} seconds".format(time.time() - start_time))


if __name__ == "__main__":
    scipy_simulation()
