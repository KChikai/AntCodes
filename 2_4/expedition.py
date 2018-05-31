# -*- coding:utf-8 -*-

import heapq

N = 4
L = 25
P = 10
A = [10, 14, 20, 21]
B = [10, 5, 2, 4]

A.append(L)
B.append(0)

pos = ans = false_flg = 0
tank = P
fuel = []
heapq.heapify(fuel)
for i in range(N):
    l = A[i] - pos
    while tank < l:
        if len(fuel) == 0:
            false_flg = 1
            break
        tank += fuel[0][1]
        heapq.heappop(fuel)
        ans += 1

    heapq.heappush(fuel, (-B[i], B[i]))
    tank -= l
    pos = A[i]

if false_flg:
    print('-1')
else:
    print(ans)