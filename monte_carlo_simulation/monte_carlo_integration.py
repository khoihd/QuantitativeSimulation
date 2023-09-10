import numpy as np
from scipy.stats import uniform
from scipy.integrate import quad

iteration = np.power(10, 3)
sample_size = np.power(10, 6)
lower, higher = -2, 5


def mc_sampling():
    uniform_dist = uniform(loc=lower, scale=higher - lower)
    return uniform_dist.rvs(size=sample_size)


def mc_antithetic_sampling():
    std_uniform_samples = uniform(-1, 1).rvs(size=int(sample_size / 2))
    # Antithetic for samples from uniform(-1, 1)
    std_uniform_samples = np.concatenate((std_uniform_samples, std_uniform_samples * (-1)))
    return lower + (std_uniform_samples + 1) / 2 * (higher - lower)


def mc_moment_matching_sampling():
    uniform_dist = uniform(loc=lower, scale=higher-lower)
    samples = uniform_dist.rvs(size=sample_size)
    print("Before: {}".format(np.mean(samples)))
    mean_adjusted_samples = samples - np.mean(samples) + (higher+lower)/2
    print("After: {}".format(np.mean(mean_adjusted_samples)))
    scaled_samples = mean_adjusted_samples / np.std(mean_adjusted_samples) * (higher-lower) / np.sqrt(12)
    return scaled_samples


def sample_f(x):
    """
    f(x) = -x^3 + 6x^2 - x + 17
    :param x:
    :return:
    """
    return -x ** 3 + 6 * x ** 2 - x + 17


def mc_evaluation(f, samples):
    results = np.zeros(iteration)
    for i in range(iteration):
        evaluations = f(samples) * (higher-lower)
        results[i] = np.mean(evaluations)

    return np.mean(results), np.std(results)


def mc_simulation(f):
    mean, std = mc_evaluation(f, mc_sampling())
    print("MC Sampling: Mean={}, STD={}".format(mean, std))
    mean, std = mc_evaluation(f, mc_moment_matching_sampling())
    print("MC Scaled Sampling: Mean={}, STD={}".format(mean, std))
    mean, std = mc_evaluation(f, mc_antithetic_sampling())
    print("MC Antithetic Sampling: Mean={}, STD={}".format(mean, std))
    print("Integration={}".format(quad(sample_f, lower, higher)))


if __name__ == "__main__":
    mc_simulation(sample_f)
