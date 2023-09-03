import numpy as np
import time

N = pow(10, 5)


def simulate_random_walk():
    """This is the problem Drunk Man from Chapter 5.2 of "Practical Guide to Quantitative Finance Interviews".

    On a line from points 0 to 100, the man starts at position 17.
    At each step, the man can walk forward or backward with probability 0.5 each.

    What is the probability of the man reach the 100th point before the 0th point

    :return:
    """

    start_time = time.time()

    reach_100 = 0  # for probability
    steps = 0  # for expected value of steps
    for _ in range(N):
        pos = 17
        while 0 < pos < 100:
            steps += 1
            prob = np.random.random()
            if prob <= 0.5:
                pos -= 1
            else:
                pos += 1
        if pos == 100:
            reach_100 += 1

    print("Probability is {}".format(reach_100 / N))
    print("Expected number of step reaching either 0 or 100: {}".format(steps / N))
    print("Runtime: {} ms".format(time.time() - start_time))


if __name__ == "__main__":
    simulate_random_walk()
