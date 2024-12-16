# Дано бинарное дерево. Проверить является ли данное дерево бинарным деревом поиска.


from collections import deque


def is_correct_binary_tree(tree: list[int | None]) -> bool:
    START_INDEX = 1

    match tree:
        case []:
            return True
        case [element]:
            return element is None

    indexes_stack = deque[int]((START_INDEX,))

    while indexes_stack:
        parent_index = indexes_stack.pop()
        parent = tree[parent_index]

        left_index = parent_index * 2
        right_index = parent_index * 2 + 1

        left = tree[left_index] if len(tree) > left_index else None
        right = tree[right_index] if len(tree) > right_index else None

        is_left_existed = left is not None
        is_right_existed = right is not None

        if is_left_existed and left >= parent: #  type: ignore[operator]
            return False
        if is_right_existed and right < parent: #  type: ignore[operator]
            return False

        if is_left_existed:
            indexes_stack.append(left_index) #  type: ignore[arg-type]
        if is_right_existed:
            indexes_stack.append(right_index) #  type: ignore[arg-type]

    return True


# print(is_correct_binary_tree([]))
# print(is_correct_binary_tree([None]))
# print(is_correct_binary_tree([None, 50]))
# print(is_correct_binary_tree([None, 50, 25, 75, 12, 27, 67, 100]))
# print(is_correct_binary_tree([None, 50, 25, 75, 12, None, 67, None]))

# print(is_correct_binary_tree([3]))
