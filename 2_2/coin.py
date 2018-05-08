# -*- coding:utf-8 -*-

value = [1, 5, 10, 50, 100, 500]
c = [3, 2, 1, 3, 0, 2]
a = 620

ans = 0
for i in reversed(range(len(value))):
    t = min(a // value[i], c[i])
    a -= t * value[i]
    ans += t
print(ans)