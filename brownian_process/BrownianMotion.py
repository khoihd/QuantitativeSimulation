import numpy as np


class BrownianMotion:
    def __init__(self, mu=0, sigma=1, duration=10, steps=10000):
        self.mu = mu
        self.sigma = sigma
        self.duration = duration
        self.steps = steps

    def simulate(self):
        """
        [https://medium.com/@mlblogging.k/simulating-brownian-motion-and-stock-prices-using-python-17b6b4bd2a1]\n
        dD(t) = mu*delta_t + sigma*dB(t)
        :return: a Simple Brownian Motion with drift mean mu
        """
        dt = self.duration / self.steps
        # dB(t)
        jumps = np.sqrt(dt) * np.random.standard_normal(self.steps)
        # dD(t) = mu*delta_t + sigma*dB(t)
        jumps = self.mu*dt + self.sigma*jumps
        jumps[0] = 0
        return np.cumsum(jumps)
