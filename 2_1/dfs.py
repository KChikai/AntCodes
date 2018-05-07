# -*- coding:utf-8 -*-


def dfs(index, s):
    global a, n, k

    if index == n:
        return s == k

    # a[index]を使用しない場合（二分木の左にシフトする）
    if dfs(index + 1, s):
        return True

    # a[index] を使用する場合
    if dfs(index + 1, s + a[index]):
        return True

n = 4
a = [1, 2, 4, 7]
k = 13

if dfs(index=0, s=0):
    print('Yes')
else:
    print('No')