import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def log2_zero(arr):
    return np.array([np.log2(x) if x != 0 else 0 for x in arr])


def compute_entropy_2d(p):
    q = 1 - p
    if p <= 0 or q <= 0:
        return 0

    return -np.dot([p, q], log2_zero([p, q]))


def compute_entropy_3d(x, y):
    z = 1 - (x + y)
    if z <= 0:
        return np.nan

    return -np.dot([x, y, z], np.log2([x, y, z]))


def entropy_2d_visualization():
    probs = np.linspace(0, 1, 21)
    entropy = np.array([compute_entropy_2d(p) for p in probs])

    fig, ax = plt.subplots()
    ax.plot(probs, entropy)
    ax.set_xlabel('Probability')
    ax.set_ylabel('Entropy')
    plt.show()


def entropy_3d_visualization():
    N = 101
    x_probs = np.linspace(0, 1, N)
    y_probs = np.linspace(0, 1, N)

    [x_grid, y_grid] = np.meshgrid(x_probs, y_probs)

    z_grid = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            x = x_grid[i, j]
            y = y_grid[i, j]
            z_grid[i, j] = compute_entropy_3d(x, y)

    # Plotting
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x_grid, y_grid, z_grid)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Entropy')
    plt.show()


if __name__ == "__main__":
    entropy_2d_visualization()
    # entropy_3d_visualization()
