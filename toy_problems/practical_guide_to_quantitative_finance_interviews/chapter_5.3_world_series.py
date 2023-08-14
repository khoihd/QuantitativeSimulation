# Mapping from (wins, losses) to the current balance
store = {}


# dp[i, j] = 1/2 * (dp[i+1, j] + dp[i, j+1])
def dp(i, j):
    """This is the problem World Series from Chapter 5.3 of "Practical Guide to Quantitative Finance Interviews".

    The player has $100 to bet each game in a series of winning 4 out of 7 games between two teams A and B.
    The player will only bet for team A each game with double-or-nothing.
    What is the strategy to bet such that the player finally has $200 if A wins the series and $0 otherwise?
    """
    if (i, j) in store:
        return store[(i, j)]

    balance = 1/2 * (dp(i+1, j) + dp(i, j+1))
    store[(i, j)] = balance
    return balance


def init_dp():
    # store[(0, 0)] = 100
    for i in range(4):
        store[(4, i)] = 200
        store[(i, 4)] = 0


if __name__ == "__main__":
    init_dp()
    dp(0, 0)

    for state, value in store.items():
        print(state, value)
