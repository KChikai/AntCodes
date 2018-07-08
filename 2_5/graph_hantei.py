# -*- coding:utf-8 -*-
"""
二部グラフの彩色問題
"""

max_v = 4
t = [(0, 1), (0, 3), (1, 2), (2, 3)]
color = [0] * max_v

# 隣接リスト
G = {v: [] for v in range(max_v)}
for e in t:
    G[e[0]].append(e[1])
    G[e[1]].append(e[0]) # 無効グラフの場合は逆の情報も入れる


def dfs(v, c):
    color[v] = c
    for i in range(len(G[v])):
        if color[G[v][i]] == c:
            return False
        if color[G[v][i]] == 0 and dfs(G[v][i], -c) is False:
            return False
    return True


def solve():
    for i in range(max_v):
        if color[i] == 0:
            if dfs(i, 1) is False:
                print("No")
                return None
    print("Yes", color)
    return None

if __name__ == '__main__':
    solve()
