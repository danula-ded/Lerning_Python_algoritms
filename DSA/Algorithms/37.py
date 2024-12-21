# Дано бинарное дерево. Выполнить прямой/центрированный/обратный/уровневый обход дерева.
# https://github.com/zernovga/Algorithms_and_Data_Structures_Course/blob/main/Lections/Lection_11.pdf


from collections import deque


class BinaryTree:
    START_INDEX = 1

    def __init__(self) -> None:
        self.elements: list[int | None] = [None]

    @property
    def count(self) -> int:
        return len(self.elements)

    def add_element(self, new_element: int) -> None:
        if self.count == 1:
            return self.elements.append(new_element)

        def inner(parent_index: int) -> None:
            parent: int = self.get_element(parent_index) # type: ignore
            left_index = self.get_left_index(parent_index)
            right_index = self.get_right_index(parent_index)
            (left, right) = self.get_children(parent_index)

            is_new_element_bigger = new_element > parent

            if (not left) and (not is_new_element_bigger):
                return self.set_new_elements(new_element, left_index)

            if (not right) and is_new_element_bigger:
                return self.set_new_elements(new_element, right_index)

            if left and (not is_new_element_bigger):
                return inner(left_index)

            if right and is_new_element_bigger:
                return inner(right_index)

        inner(self.START_INDEX)

    def get_element(self, element_index: int) -> int | None:
        if not (self.START_INDEX <= element_index < self.count):
            return None

        return self.elements[element_index]

    def set_new_elements(self, new_element: int, index: int) -> None:
        while self.count < index + 1:
            self.elements.append(None)

        self.elements[index] = new_element

    def get_left_index(self, parent_index: int) -> int:
        return parent_index * 2

    def get_right_index(self, parent_index: int) -> int:
        return parent_index * 2 + 1

    def get_left(self, parent_index: int) -> int | None:
        return self.get_element(self.get_left_index(parent_index))

    def get_right(self, parent_index: int) -> int | None:
        return self.get_element(self.get_right_index(parent_index))

    def get_children(self, parent_index: int) -> tuple[int | None, int | None]:
        return (self.get_left(parent_index), self.get_right(parent_index))

    def print(self) -> None:
        print(str(self))

    def __str__(self) -> str:
        elements: list[str] = [str(element) for element in self.elements]
        return ' | '.join(elements)

    # ------------------------------------
    # Прямой обход
    def get_pre_order(self) -> list[int]:
        result: list[int] = []

        def inner(parent_index: int) -> None:
            parent = self.get_element(parent_index)
            left_index = self.get_left_index(parent_index)
            right_index = self.get_right_index(parent_index)
            (left, right) = self.get_children(parent_index)

            if parent is None:
                return

            result.append(parent)
            if (left is not None): inner(left_index)
            if (right is not None): inner(right_index)

        inner(self.START_INDEX)

        return result

    # Центрированный
    def get_in_order(self) -> list[int]:
        result: list[int] = []

        def inner(parent_index: int) -> None:
            parent = self.get_element(parent_index)
            left_index = self.get_left_index(parent_index)
            right_index = self.get_right_index(parent_index)
            (left, right) = self.get_children(parent_index)

            if parent is None:
                return

            if (left is not None): inner(left_index)
            result.append(parent)
            if (right is not None): inner(right_index)

        inner(self.START_INDEX)

        return result

    # обратный
    def get_post_order(self) -> list[int]:
        result: list[int] = []

        def inner(parent_index: int) -> None:
            parent = self.get_element(parent_index)
            left_index = self.get_left_index(parent_index)
            right_index = self.get_right_index(parent_index)
            (left, right) = self.get_children(parent_index)

            if parent is None:
                return

            if (left is not None): inner(left_index)
            if (right is not None): inner(right_index)
            result.append(parent)

        inner(self.START_INDEX)

        return result

    # Уровневый
    def get_levels_order(self) -> list[int]:
        result: list[int] = []

        parent_index = self.START_INDEX

        if self.get_element(parent_index) is None:
            return result

        queue = deque[int]((parent_index,))

        while queue:
            current_index = queue.pop()
            result.append(self.get_element(current_index)) # type: ignore

            left_index = self.get_left_index(current_index)
            right_index = self.get_right_index(current_index)
            (left, right) = self.get_children(current_index)

            if (left is not None): queue.appendleft(left_index)
            if (right is not None): queue.appendleft(right_index)

        return result



# tree = BinaryTree()

# for element in (52, 4, 6, 2, 0, -4, 5, 78, 123, 122, 3343):
#     tree.add_element(element)

# tree.print()
# print(tree.get_pre_order())
# print(tree.get_in_order())
# print(tree.get_post_order())
# print(tree.get_levels_order())
