import numpy as np


class AutoRegressive:
    def __init__(self, coefficients, mean):
        self.coefficients = coefficients
        self.lag = len(coefficients)
        self.mean = mean

    def simulate(self, timestep, init='zero'):
        result = np.zeros(timestep)

        if init == 'mean':
            result[:self.lag] = self.mean
        elif init == 'random':
            result[:self.lag] = np.random.standard_normal(self.lag)

        for i in range(self.lag, timestep):
            result[i] = np.dot(self.coefficients, result[i - self.lag:i]) + np.random.standard_normal()

        return result
