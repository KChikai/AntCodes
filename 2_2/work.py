# -*- coding:utf-8 -*-

n = 5
s = [1, 2, 4, 6, 8]
t = [3, 5, 7, 9, 10]
ans = 0
end = []
dellist = lambda items, indexes: [item for index, item in enumerate(items) if index not in indexes]

while True:
    work = t.index(min(t))
    ans += 1
    for i in range(len(t)):
        if s[i] < t[work]:
            end.append(i)
    s = dellist(s, end)
    t = dellist(t, end)
    end.clear()
    if len(t) == 0:
        break
print(ans)