from typing import Any
from node import Node


class SinglyLinkedList:
    def __init__(self, value=None):
        self._head_node = Node(value)

    def get_head_node(self) -> Node:
        return self._head_node

    def insert(self, value: Any):
        if self._head_node is None:
            node = Node(value)
            self._head_node = node
        else:
            current_node = self._head_node
            while current_node.get_next_node():
                current_node = current_node.get_next_node()
            node = Node(value)
            current_node.set_next_node(node)

    def stringify_list(self) -> str:
        stringify_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() is not None:
                stringify_list = stringify_list + str(current_node.get_value()) + " -> "
            current_node = current_node.get_next_node()
        return stringify_list


if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    print(linked_list.stringify_list())

"""
# Result example
1 -> 2 -> 
"""
