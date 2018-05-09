# -*- coding:utf-8 -*-


N = 6
S = list('ACDBCB')
T = ''
a = 0
b = N - 1
ans = ''
while a <= b:
    left = False
    for i in range(b - a):
        if S[a + i] < S[b - i]:
            left = True
            break
        elif S[a + i] > S[b - i]:
            left = False
            break
    if left:
        ans += S[a]
        a += 1
    else:
        ans += S[b]
        b -= 1
print(ans)


# 別解
# N = 6
# S = list('ACDBCB')
# T = ''
# print(S)
# for i in range(N):
#     if S[0] < S[-1]:
#         T += S[0]
#         S.pop(0)
#     elif S[0] > S[-1]:
#         T += S[-1]
#         S.pop(-1)
#     elif S[0] == S[-1]:
#         if len(S) != 1:
#             # 同一文字のケースで残り複数個
#             j = 1
#             while True:
#                 if S[j] == S[len(S) - 1 - j]:
#                     j += 1
#                 else:
#                     break
#             if S[j] < S[len(S) - 1 - j]:
#                 T += S[0]
#                 S.pop(0)
#             else:
#                 T += S[-1]
#                 S.pop(-1)
#         else:
#             # S残り一個（文字列ラスト）
#             T += S[0]
#             S.pop(0)
#
# print(T)


# 同一文字を考慮していないケース
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