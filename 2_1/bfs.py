# -*- coding:utf-8 -*-

import numpy as np

N = 10
M = 10
ground = [
    ['#', 'S', '#', '#', '#', '#', '#', '#', '.', '#'],
    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '#'],
    ['.', '#', '.', '#', '#', '.', '#', '#', '.', '#'],
    ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['#', '#', '.', '#', '#', '.', '#', '#', '#', '#'],
    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '#'],
    ['.', '#', '#', '#', '#', '#', '#', '#', '.', '#'],
    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '#', '.', '#', '#', '#', '.'],
    ['.', '.', '.', '.', '#', '.', '.', '.', 'G', '#'],
]
queue = []
d = np.zeros((N, M))
sx = sy = gx = gy = 0
for i in range(N):
    for j in range(M):
        if ground[i][j] == 'S':
            sx = i
            sy = j
        if ground[i][j] == 'G':
            gx = i
            gy = j

# initialize
for i in range(N):
    for j in range(M):
        d[i, j] = -1
d[sx, sy] = 0
queue.append((sx, sy))

while len(queue) > 0:
    p = queue.pop(0)
    if p[0] == gx and p[1] == gy:
        print(d[gx,gy])
        break
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if abs(dx) != abs(dy):
                nx = p[0] + dx
                ny = p[1] + dy
                if 0 <= nx < N and 0 <= ny < M and ground[nx][ny] != '#' and d[nx, ny] == -1:
                    queue.append((nx, ny))
                    d[nx, ny] = d[p[0], p[1]] + 1
print(d[gx, gy])