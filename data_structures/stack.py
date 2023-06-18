from typing import Any


class Stack:
    def __init__(self, limit=10):
        self._stack = []
        self._limit = limit

    def push(self, value: Any):
        try:
            if len(self._stack) < self._limit:
                self._stack.append(value)
            else:
                raise Exception("Stack overflow")
        except Exception as e:
            print(e)

    def top(self) -> Any:
        return self._stack[-1]

    def pop(self) -> Any:
        return self._stack.pop(-1)

    def empty(self) -> int:
        if len(self._stack) == 0:
            return 1
        else:
            return 0

    def __str__(self):
        return self._stack


if __name__ == "__main__":
    stack = Stack(limit=3)
    stack.push(1)
    print(stack.__str__())
    stack.push(2)
    print(stack.__str__())
    stack.push(3)
    print(stack.__str__())
    stack.push(4)
    print(stack.__str__())
    print(stack.pop())
    print(stack.__str__())

"""
# Result example
[1]
[1, 2]
[1, 2, 3]
Stack overflow
[1, 2, 3]
3
[1, 2]
"""
