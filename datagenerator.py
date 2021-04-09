"""
trend

seasonality

noise


"""

from pprint import pprint
import matplotlib.pyplot as plt

import numpy as np
from numpy.random import randint
import math
import pandas as pd

np.random.seed(0)

n = 10_0
n = 10_000
n = 1_000
n = 365 * 6


def get_trend(trend_changes, mul):
    result = []
    trend_change_times = [0] + sorted([int(x * n) for x in np.random.rand(trend_changes)]) + [n]

    # print(f'{trend_change_times=}')
    for i in range(len(trend_change_times) - 1):
        start = trend_change_times[i]
        stop = trend_change_times[i + 1]
        # print(f'{trend_change_times[i]=}')
        # print(f'{trend_change_times[i+1]=}')
        slope = (np.random.rand() - 0.5) * mul
        result += [slope for _ in range(start, stop)]

    f = []
    for i, x in enumerate(result):
        if i == 0:
            f.append(x)
        else:
            f.append(f[-1] + x)
    return f


def get_seasonality(div, mul):
    offset = randint(0, 100)
    a = [math.sin((offset + i) * 2 * math.pi / div) * mul for i in range(n)]
    # pprint(a)
    return a
    pass


def get_noise(mul):
    noise = [(np.random.rand() - 0.5) * mul for _ in range(n)]
    # noise2 = [np.random.rand() * mul for _ in range(n)]
    f = []
    for i, x in enumerate(noise):
        if i == 0:
            f.append(x)
        else:
            f.append(f[-1] + x)  # + noise2[i])
    return f


def save(res, suff=''):
    import datetime
    res = [[datetime.datetime(2000, 1, 1) + datetime.timedelta(days=i), x] for i, x in enumerate(res)]
    df = pd.DataFrame(res, columns=['ds', 'y'])
    # print(df)
    df.to_csv(f'datasets/generated{suff}.csv', index=False)


def main():
    res = [0 for _ in range(n)]
    trend_changes = 2
    res = get_trend(trend_changes, 0.01)
    res = [sum(z) for z in zip(res, get_seasonality(7, 1.1))]
    res = [sum(z) for z in zip(res, get_seasonality(365, 1))]
    res = [sum(z) for z in zip(res, get_noise(4.0 * 0.1))]

    save(res)
    res_partial = res[0: int(n * 0.9)]
    save(res_partial, suff='_partial')

    # plt.clf()
    plt.plot(res, color='blue')
    plt.plot(res_partial, color='black')
    plt.savefig(f'out/mydata.png')


main()
