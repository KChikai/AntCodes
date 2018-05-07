# -*- coding:utf-8 -*-
"""
Queue for Python ver
"""


class Queue:
    def __init__(self, queue):
        if isinstance(queue, list):
            self.queue = queue
        elif isinstance(queue, None):
            self.queue = []
        else:
            raise TypeError

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) != 0:
            return self.queue.pop(0)
        else:
            print("queue length is zero...")


if __name__ == '__main__':
    q = Queue([1, 2, 3])
    q.enqueue(4)
    print(q.queue)
    q.dequeue()
    print(q.dequeue())
    print(q.queue)