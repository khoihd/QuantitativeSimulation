from brownian_process.BrownianMotion import BrownianMotion
from overrides import override
import numpy as np


class GeometricBrownianMotion(BrownianMotion):
    def __init__(self, mu=0, sigma=1, duration=10, steps=10000):
        super().__init__(mu, sigma, duration, steps)

    @override
    def simulate(self):
        delta_t = self.duration / self.steps
        # dB(t)
        jumps = np.sqrt(delta_t) * np.random.standard_normal(self.steps)
        # dD(t) = (mu - sigma^2/2)* dt + sigma * dB(t)
        jumps = (self.mu - 0.5*self.sigma**2)*delta_t + self.sigma*jumps
        # d(logGt) = e^{mu - sigma^2/2)*dt + sigma*dB(t)}
        jumps = np.exp(jumps)
        jumps[0] = 1
        return np.cumprod(jumps)
