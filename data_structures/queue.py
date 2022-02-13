from typing import Any


class Queue:
    def __init__(self, limit=10):
        self._queue = []
        self._limit = limit

    def enqueue(self, value: Any):
        try:
            if len(self._queue) < self._limit:
                self._queue.append(value)
            else:
                raise Exception('Queue overflow')
        except Exception as e:
            print(e)

    def dequeue(self) -> Any:
        if len(self._queue) > 0:
            return self._queue.pop(0)

    def get_front(self) -> Any:
        if len(self._queue) > 0:
            return self._queue[0]

    def __str__(self):
        return self._queue


if __name__ == '__main__':
    queue = Queue(3)
    queue.enqueue(1)
    print(queue.__str__())
    queue.enqueue(2)
    print(queue.__str__())
    queue.enqueue(3)
    print(queue.__str__())
    queue.enqueue(4)
    print(queue.__str__())
    print(queue.get_front())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

'''
# Result example
[1]
[1, 2]
[1, 2, 3]
Queue overflow
[1, 2, 3]
1
1
2
3
None
'''
