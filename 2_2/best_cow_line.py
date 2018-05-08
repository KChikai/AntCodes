# -*- coding:utf-8 -*-

N = 6
S = list('ACDBCB')
T = ''
print(S)
for i in range(N):
    if S[0] < S[-1]:
        T += S[0]
        S.pop(0)
    elif S[0] > S[-1]:
        T += S[-1]
        S.pop(-1)
    elif S[0] == S[-1]:
        if len(S) != 1:
            # 同一文字のケースで残り複数個
            j = 1
            while True:
                if S[j] == S[len(S) - 1 - j]:
                    j += 1
                else:
                    break
            if S[j] < S[len(S) - 1 - j]:
                T += S[0]
                S.pop(0)
            else:
                T += S[-1]
                S.pop(-1)
        else:
            # S残り一個
            T += S[0]
            S.pop(0)

print(T)


# T = ''
# S = list('ACDBCB')
# S_rev = S[::-1]
# while True:
#     print('a', T)
#     if S[0] <= S_rev[0]:
#         T += S[0]
#         S.pop(0)
#     else:
#         T += S_rev[0]
#         S_rev.pop(0)
#     if len(T) == N:
#         break
#
# print(T, len(T))