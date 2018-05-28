# -*- coding:utf-8 -*-

p = 5
a = [1, 8, 8, 8, 1]

a_set = [0] * max(a)
a_num = len(set(a))
res = 999999
j = 0
num = 0
for i in range(len(a)):
    # move right side
    while j < len(a):
        if a_set[a[j]-1] == 0:
            a_set[a[j]-1] += 1
            num += 1
        if num == a_num:
            break
        j += 1

    # update res
    if num == a_num:
        if j == len(a):
            res = min(res, j - i)
        else:
            res = min(res, j - i + 1)

    print(i, j, j-i+1, num)
    # move left side
    num -= 1
    a_set[a[i]-1] -= 1

print(res)

