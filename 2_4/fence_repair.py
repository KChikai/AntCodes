# -*- coding:utf-8 -*-
"""ハフマン符号"""
import heapq

# N = 3
# L = [8, 5, 8]
N = 5
L = [3, 4, 5, 1, 2]
ans = 0

heapq.heapify(L)
while len(L) > 1:
    v1 = heapq.heappop(L)
    v2 = heapq.heappop(L)
    ans += v1 + v2
    heapq.heappush(L, v1 + v2)
print(ans)