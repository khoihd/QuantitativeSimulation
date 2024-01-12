from AutoRegressive import AutoRegressive
import matplotlib.pyplot as plt


def simulate_autoregressive():
    coefficients = [1, 1]
    ar = AutoRegressive(coefficients, mean=0)
    sequence = ar.simulate(mode='zero', timestep=10)
    plt.plot(sequence)
    plt.show()


if __name__ == "__main__":
    simulate_autoregressive()
