import matplotlib.pyplot as plt
import numpy as np

from brownian_motion.GeometricBrownianMotion import GeometricBrownianMotion
from brownian_motion.RandomWalk import RandomWalk
from brownian_motion.BrownianMotion import BrownianMotion

def simulate_random_walks():
    rw = RandomWalk(10000, 0.49)
    random_walks = {"line_" + str(i): rw.simulate() for i in range(10)}
    for k, v in random_walks.items():
        plt.plot(v, label=k)
    plt.legend()
    plt.show()


def simulate_brownian_motion_no_drift():
    rw = BrownianMotion()
    brownian_motions = {"line_" + str(i): rw.simulate() for i in range(10)}
    for k, v in brownian_motions.items():
        plt.plot(v, label=k)
    plt.legend()
    plt.show()


def simulate_brownian_motion_with_drift():
    rw = BrownianMotion(mu=1, steps=np.power(10, 5))
    brownian_motions = {"line_" + str(i): rw.simulate() for i in range(10)}
    for k, v in brownian_motions.items():
        plt.plot(v, label=k)
    plt.legend()
    plt.show()


def simulate_geometric_bm():
    rw = GeometricBrownianMotion(mu=0, steps=np.power(10, 5))
    brownian_motions = {"line_" + str(i): rw.simulate() for i in range(10)}
    for k, v in brownian_motions.items():
        plt.plot(v, label=k)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # simulate_random_walks()
    # simulate_brownian_motion_no_drift()
    # simulate_brownian_motion_with_drift()
    simulate_geometric_bm()

