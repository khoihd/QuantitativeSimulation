from AutoRegressive import AutoRegressive
from OrnsteinUhlenbeck import OrnsteinUhlenbeck
import matplotlib.pyplot as plt


def simulate_autoregressive():
    coefficients = [1]
    ar = AutoRegressive(coefficients, mean=0)
    sequence = ar.simulate(init='zero', timestep=10)
    plt.plot(sequence)
    plt.show()


def simulate_ornstein_uhlenbeck():
    ou = OrnsteinUhlenbeck(phi=1, mean=0, sigma=1)
    sequence = ou.simulate(duration=10, steps=100000, init='zero')
    plt.plot(sequence)
    plt.show()


if __name__ == "__main__":
    simulate_ornstein_uhlenbeck()
