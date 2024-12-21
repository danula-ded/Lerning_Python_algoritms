# Дано бинарное дерево. Проверить является ли данное дерево сбалансированным.


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

    def is_balanced(self) -> bool:
        def inner(parent_index: int) -> tuple[bool, int]: # (is_balanced, height)
            parent = self.get_element(parent_index)

            if parent is None:
                return (True, 0)

            left_index = self.get_left_index(parent_index)
            right_index = self.get_right_index(parent_index)

            (is_left_balanced, left_height) = inner(left_index)
            (is_right_balanced, right_height) = inner(right_index)

            if (not is_left_balanced) or (not is_right_balanced):
                return (False, -1)

            difference = abs(left_height - right_height)

            return (difference < 2, max(left_height, right_height) + 1)

        return inner(self.START_INDEX)[0]


# tree = BinaryTree()

# for element in (52, 4, 6, 2, 0, -4, 5, 78, 123, 122, 3343, 77):
#     tree.add_element(element)

# print(tree.is_balanced())
