# -*- coding:utf-8 -*-
"""
Stack for Python ver
(通常は collection class を用いる)
"""


class Stack:

    def __init__(self, stack):
        if isinstance(stack, list):
            self.stack = stack
        elif isinstance(stack, None):
            self.stack = []
        else:
            raise TypeError

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop(-1)
        else:
            print('stack length is zero...')

if __name__ == '__main__':
    s = Stack([1, 2, 3])
    s.push(4)
    print(s.stack)  # [1,2,3,4]
    s.pop()         # [1,2,3]
    print(s.pop())  # 3
    print(s.stack)  # [1,2]
    s.pop()         # 2
    print(s.stack)  # [1]
    s.pop()         # 1
    s.pop()         # []なのでpopする値がない