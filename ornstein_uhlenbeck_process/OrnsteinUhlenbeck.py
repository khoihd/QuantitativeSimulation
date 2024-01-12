import numpy as np


class OrnsteinUhlenbeck:
    def __init__(self, phi, mean, sigma):
        # dXt = phi(mean - Xt)dt + sigma * dW_t
        self.phi = phi
        self.mean = mean
        self.sigma = sigma

    # dXt = phi(mean - Xt)dt + sigma * dW(t)
    def simulate(self, duration, steps, init='zero'):
        result = np.zeros(steps)
        dt = duration / steps
        # dW(t)
        jumps = np.sqrt(dt) * np.random.standard_normal(steps)

        if init == 'random':
            result[0] = np.random.standard_normal(0)

        for i in range(1, steps):
            dx = self.phi * (self.mean - result[i - 1]) * dt + self.sigma * jumps[i]
            result[i] = result[i - 1] + dx

        return result
