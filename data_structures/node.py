from typing import Any


class Node:
    def __init__(self, value: Any):
        self._value = value
        self._next_node = None

    def set_value(self, value):
        self._value = value

    def get_value(self) -> Any:
        return self._value

    def set_next_node(self, node):
        self._next_node = node

    def get_next_node(self) -> Any:
        return self._next_node


if __name__ == "__main__":
    node_num1 = Node(1)
    node_num2 = Node(2)
    node_num1.set_next_node(node_num2)
    print(node_num1.get_value())
    print(node_num1.get_next_node())
    print(node_num2.get_value())

"""
# Result example
1
<__main__.Node object at 0x7f7e88203d30>
2
"""
