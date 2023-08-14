import numpy as np

N = pow(10, 6)


def simulate_random_walk():
    """This is the problem Drunk Man from Chapter 5.2 of "Practical Guide to Quantitative Finance Interviews".

    On a line from points 0 to 100, the man starts at position 17.
    At each step, the man can walk forward or backward with probability 0.5 each.

    What is the probability of the man reach the 100th point before the 0th point

    :return:
    """
    reach_100 = 0
    for _ in range(N):
        pos = 17
        while 0 < pos < 100:
            prob = np.random.random()
            if prob <= 0.5:
                pos -= 1
            else:
                pos += 1
        if pos == 100:
            reach_100 += 1

    print("Probability is {}".format(reach_100 / N))


if __name__ == "__main__":
    simulate_random_walk()
