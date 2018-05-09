# -*- coding:utf-8 -*-

# 失敗例
N = 6
R = 10
X = [1, 7, 15, 20, 30, 50]
now = ans = 0
points = []
while now < len(X) - 1:
    right_max = X[now] + R
    for j in range(now + 1, N):
        if X[j] < right_max:
            pass
        else:
            now = j
            ans += 1
            if now < len(X) - 1:
                points.append(X[j - 1])
            else:
                points.append(X[j])
            break
print(ans, points)


# 模範回答
N = 6
R = 10
X = [1, 7, 15, 20, 30, 50]
now = i = ans = 0
points = []
while i < len(X):
    right_max = X[i] + R
    i += 1
    while i < len(X) and X[i] <= right_max: # 先に i < N を書かないとインデックスエラーが起こる
        i += 1
    points.append(X[i - 1])
    right_max = X[i - 1] + R
    while i < len(X) and X[i] <= right_max:
        i += 1
    ans += 1
print(ans, points)
