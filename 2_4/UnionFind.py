# -*- coding:utf-8 -*-


class UnionFind:

    def __init__(self, max_n):
        self.par = [i for i in range(max_n)]
        self.rank = [0] * max_n

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return None

        if self.rank[x_root] < self.rank[y_root]:
            self.par[x_root] = y_root
        else:
            self.par[y_root] = x_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)


def solve():
    N = 100
    K = 7
    T = [1, 2, 2, 2, 1, 2, 1]
    X = [101, 1, 2, 3, 1, 3, 5]
    Y = [1, 2, 3, 3, 3, 1, 5]

    # x+N => x-B, x+2N => x-C
    tree = UnionFind(max_n=N * 3)

    ans = 0
    for i in range(K):
        t = T[i]
        x = X[i] - 1
        y = Y[i] - 1

        # not correct number
        if x < 0 or N <= x or y < 0 or N <= y:
            ans += 1
            continue

        if t == 1:
            # x is y
            if tree.same(x, y + N) or tree.same(x, y + 2 * N):
                ans += 1
            else:
                tree.unite(x, y)
                tree.unite(x + N, y + N)
                tree.unite(x + N * 2, y + N * 2)
        else:
            # x eats y
            if tree.same(x, y) or tree.same(x, y + 2 * N):
                ans += 1
            else:
                tree.unite(x, y + N)
                tree.unite(x + N, y + 2 * N)
                tree.unite(x + N * 2, y)

        print(tree.par)
        # print(tree.rank)

    print(ans)

if __name__ == '__main__':
    solve()