import numpy as np


class WienerProcess:
    def __init__(self, duration=10, steps=10000):
        self.duration = duration
        self.steps = steps

    def simulate(self):
        # dW = sqrt(t) * N(0,1)
        t = self.duration / self.steps
        jumps = [np.random.standard_normal() * np.sqrt(t) for _ in range(self.steps)]
        return np.cumsum(jumps)
