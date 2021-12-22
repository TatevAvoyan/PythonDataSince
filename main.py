# The given code includes a list of heights for various basketball players.
# You need to calculate and output how many players are in the range of one standard deviation from the mean.
import numpy as np


def players_count():
    players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]

    a = np.array(players)
    mean = np.sum(a)/a.size  # 189.2 np.mean(players)
    variance = np.sum((a - mean)**2) / a.size  # 111.56 np.var(players)
    std = variance ** (1/2)  # 10.56 np.std(players)
    b = int(mean - std)
    c = int(mean + std)
    count = 0
    for i in range(b, c):
        if i in players:
            count += 1
    return count


print(players_count())
