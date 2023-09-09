from brownian_motion.BrownianMotion import BrownianMotion
from overrides import override
import numpy as np


class GeometricBrownianMotion(BrownianMotion):
    def __init__(self, mu=0, sigma=1, duration=10, steps=10000):
        super().__init__(mu, sigma, duration, steps)

    @override
    def simulate(self):
        brownian_motion = BrownianMotion(0, 1, self.duration, self.steps)
        brownian_motion = brownian_motion.simulate()

        # D(t) = D(0) * exp{ (mu - sigma^2/2)* dt + sigma * dB(t)}
        geometric_bm = np.exp((self.mu - 0.5*self.sigma**2) * np.linspace(0, self.duration, self.steps) + self.sigma * brownian_motion)
        return geometric_bm
