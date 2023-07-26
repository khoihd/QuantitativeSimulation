import numpy as np
import time

N = np.power(10, 6)
type_count = 2


def simulation():
    start_time = time.time()
    samples = list(range(type_count))

    expected_turns = 0
    for _ in np.arange(N):
        distinct_samples = set()
        turn = 0
        while True:
            sample = np.random.choice(samples)
            turn += 1
            distinct_samples.add(sample)
            if len(distinct_samples) == type_count:
                expected_turns += turn
                break

    print("Expected turns = {}".format(expected_turns / N))
    print("Runtime = {}s".format(time.time() - start_time))


if __name__ == "__main__":
    simulation()
