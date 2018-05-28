# -*- coding:utf-8 -*-

# n = 5
# s = 11
# a = [1, 2, 3, 4, 5]

n = 10
s = 15
a = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]


res = 99999999
j = 0
su = 0
for i in range(n):
    while j < n:
        if su + a[j] >= s:
            break
        su += a[j]
        j += 1

    if j == n:
        # j が最終まで移動しきっているパターン (while条件文で抜けるパターン)
        if su >= s:
            res = min(res, j - i + 1)
    else:
        # それ以外 (break文でループを抜けているパターン)
        if su + a[j] >= s:
            res = min(res, j - i + 1)
    su -= a[i]

print(res)