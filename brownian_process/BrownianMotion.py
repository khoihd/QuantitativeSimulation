import numpy as np


class BrownianMotion:
    def __init__(self, duration=10, steps=10000):
        self.duration = duration
        self.steps = steps

    def simulate_no_drift(self):
        """
        [https://medium.com/@mlblogging.k/simulating-brownian-motion-and-stock-prices-using-python-17b6b4bd2a1]
        :return: a Simple Brownian Motion without drift
        """
        # dW = sqrt(t) * N(0,1)
        delta_t = self.duration / self.steps
        jumps = np.sqrt(delta_t) * np.random.standard_normal(self.steps)
        jumps[0] = 0
        return np.cumsum(jumps)

    def simulate_with_drift(self):
        pass
    