# -*- coding:utf-8 -*-

import numpy as np

n = 4
W = 5
K = [(2, 3), (1, 2), (3, 4), (2, 2)]

mat = np.zeros((n + 1, W + 1))  # 個数と総重量の行列
for a in range(n+1):
    for b in range(W+1):
        mat[a, b] = -1


def search(i, weight):
    global mat
    # 計算結果値がある場合
    if mat[i, weight] >= 0:
        return mat[i, weight]

    # 未計算の場合
    # i番目のモノの重量を調べて許容範囲内であれば，使用する場合としない場合でi+1を同様に調べる
    result = 0
    if i == n:
        result = 0
    elif weight < K[i][0]:
        result = search(i + 1, weight)
    else:
        result = max(search(i + 1, weight), search(i + 1, weight - K[i][0]) + K[i][1])
    mat[i, weight] = result
    return result

ans = search(0, W)
print(ans)
print(mat)
