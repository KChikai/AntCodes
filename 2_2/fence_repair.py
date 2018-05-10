# -*- coding:utf-8 -*-
"""ハフマン符号"""
# N = 3
# L = [8, 5, 8]
N = 5
L = [3, 4, 5, 1, 2]
ans = 0

while len(L) > 1:
    L.sort()
    v1 = L.pop(0)
    v2 = L.pop(0)
    ans += v1 + v2
    L.append(v1 + v2)
print(ans)