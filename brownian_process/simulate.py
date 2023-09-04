import matplotlib.pyplot as plt
from brownian_process.RandomWalk import RandomWalk
from brownian_process.BrownianMotion import BrownianMotion

def simulate_random_walks():
    rw = RandomWalk(10000, 0.49)
    random_walks = {"line_" + str(i): rw.simulate() for i in range(10)}
    for k, v in random_walks.items():
        plt.plot(v, label=k)
    plt.legend()
    plt.show()


def simulate_brownian_motion():
    rw = BrownianMotion()
    brownian_motions = {"line_" + str(i): rw.simulate_no_drift() for i in range(10)}
    for k, v in brownian_motions.items():
        plt.plot(v, label=k)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # simulate_random_walks()
    simulate_brownian_motion()


