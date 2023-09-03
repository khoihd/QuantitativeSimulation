import numpy as np


class RandomWalk:
    def __init__(self, steps=10000, p=0.5):
        self.steps = steps
        self.p = p

    def simulate(self):
        jumps = np.where(np.random.random(self.steps) <= self.p, 1, -1)
        return np.cumsum(jumps)
    