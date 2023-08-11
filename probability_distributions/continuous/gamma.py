import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma
import time

N = np.power(10, 7)

lambda_par = 3
n = 6
expected_value = n / lambda_par
variance = n / lambda_par**2


def scipy_simulation():
    start_time = time.time()

    samples = gamma.rvs(n, 1/lambda_par, size=N)

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
