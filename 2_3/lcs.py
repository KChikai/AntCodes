# -*- coding:utf-8 -*-

import numpy as np

n = 4
m = 4
s = list('abcd')
t = list('becd')
dp = np.zeros((n + 1, m + 1))


def solve():
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:   # indexなので -1
                dp[i + 1, j + 1] = dp[i, j] + 1
            else:
                dp[i + 1, j + 1] = max(dp[i, j + 1], dp[i + 1, j])
    print(dp[n, m])
    print(dp)
solve()
