import matplotlib.pyplot as plt
from brownian_process.RandomWalk import RandomWalk

if __name__ == "__main__":
    rw = RandomWalk(10000, 0.49)
    random_walks = {"line_" + str(i): rw.simulate() for i in range(10)}
    for k, v in random_walks.items():
        plt.plot(v, label=k)
    plt.legend()
    plt.show()

