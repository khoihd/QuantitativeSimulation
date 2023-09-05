import numpy as np


class BrownianMotion:
    def __init__(self, mu=0, duration=10, steps=10000):
        self.mu = mu
        self.duration = duration
        self.steps = steps

    def simulate(self):
        """
        [https://medium.com/@mlblogging.k/simulating-brownian-motion-and-stock-prices-using-python-17b6b4bd2a1]
        :return: a Simple Brownian Motion with drift mean mu
        """
        delta_t = self.duration / self.steps
        jumps = self.mu * delta_t + np.sqrt(delta_t) * np.random.standard_normal(self.steps)
        jumps[0] = 0
        return np.cumsum(jumps)
