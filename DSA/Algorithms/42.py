# Дано бинарное дерево поиска. Реализовать функцию поиска/вставки/удаления узла.

# Для разнообразия сделал через объекты, а не списком
# Кста, задание гроб, если попадётся, будет очень грустно


from collections import deque
from typing import Self


class Node:
    def __init__(self, value: int) -> None:
        self.left: Self | None = None
        self.right: Self | None = None
        self.value = value

    def __str__(self) -> str:
        return f'Node: {self.value}'


class BinaryTree:
    def __init__(self) -> None:
        self.start: None | Node = None

    def get_node(self, item_value: int) -> Node | None:
        if not self.start:
            return None

        current_node: Node | None = self.start

        while current_node:
            if current_node.value == item_value:
                return current_node

            if current_node.value > item_value:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return None

    def add_item(self, new_item_value: int) -> None:
        if not self.start:
            self.start = Node(new_item_value)
            return

        current_node: Node | None = self.start

        while current_node:
            current_value = current_node.value
            is_new_item_value_smaller = new_item_value < current_value

            if is_new_item_value_smaller and (not current_node.left):
                current_node.left = Node(new_item_value)
                current_node = None
            elif (not is_new_item_value_smaller) and (not current_node.right):
                current_node.right = Node(new_item_value)
                current_node = None
            elif is_new_item_value_smaller and current_node.left:
                current_node = current_node.left
            else:
                current_node = current_node.right

    # Наверняка можно написать лучше
    def delete_item(self, item_value: int) -> None:
        if not self.start:
            return None

        parent_node: Node | None = None
        current_node: Node | None = self.start

        # находим элемент для удаления и его родителя
        while current_node:
            if current_node.value == item_value:
                break

            parent_node = current_node

            if current_node.value > item_value:
                current_node = current_node.left
            else:
                current_node = current_node.right

        if not current_node:
            return

        if not parent_node:
            self.start = None
            return

        # если у удаляемого элемента не потомков
        if (not current_node.left) and (not current_node.right):
            if parent_node.left == current_node:
                parent_node.left = None
            elif parent_node.right == current_node:
                parent_node.right = None

        # Если не правого
        elif current_node.left and (not current_node.right):
            if parent_node.left == current_node:
                parent_node.left = current_node.left
            elif parent_node.right == current_node:
                parent_node.right = current_node.left

        # Если не левого
        elif (not current_node.left) and current_node.right:
            if parent_node.left == current_node:
                parent_node.left = current_node.right
            elif parent_node.right == current_node:
                parent_node.right = current_node.right

        # Если есть оба :(
        else:
            parent_bigger_node = current_node
            bigger_node: Node = current_node.right # type: ignore

            while True:
                if not bigger_node.left:
                    break

                parent_bigger_node = bigger_node
                bigger_node = bigger_node.left

            if parent_bigger_node == current_node:
                parent_bigger_node.right = None
                bigger_node.left = current_node.left
                bigger_node.right = None
            else:
                parent_bigger_node.left = None
                bigger_node.left = current_node.left
                bigger_node.right = current_node.right

            if parent_node.left == current_node:
                parent_node.left = bigger_node
            else:
                parent_node.right = bigger_node

    def __str__(self) -> str:
        if not self.start:
            return ''

        nodes_queue = deque[Node]((self.start,))
        nodes_values: list[str] = []

        while nodes_queue:
            node = nodes_queue.pop()
            nodes_values.append(str(node.value))

            for next_node in (node.left, node.right):
                if not next_node:
                    continue

                nodes_queue.appendleft(next_node)

        return ' '.join(nodes_values)


# tree = BinaryTree()

# for number in (50, 25, 75, 24, 26, 76, 74, 0):
#     tree.add_item(number)

# print(tree)

# tree.delete_item(25)
# tree.delete_item(0)

# print(tree)
