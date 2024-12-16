# Даны два упорядоченных по невозрастанию односвязных списка.
# Объедините их в новый упорядоченный по невозрастанию односвязный список.

from typing import Optional, Self, Generator

class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Optional[Self] = None

    def set_next(self, new_next: Self) -> None:
        self.next = new_next


class List:
    def __init__(self) -> None:
        self.start: Optional['Node'] = None
        self.tail: Optional['Node'] = None

    def add_node(self, new_node: 'Node') -> None:
        if (self.start is None) or (self.tail is None):
            self.start = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def __iter__(self) -> Generator[int, None, None]:
        def generator() -> Generator[int, None, None]:
            current: Optional['Node'] = self.start

            while current:
                yield current.value
                current = current.next

        return generator()


def combine_lists(first: 'List', second: 'List') -> 'List':
    new_list: 'List' = List()
    first_current: Optional['Node'] = first.start
    second_current: Optional['Node'] = second.start

    while first_current and second_current:
        if first_current.value > second_current.value:
            new_list.add_node(first_current)
            first_current = first_current.next
        else:
            new_list.add_node(second_current)
            second_current = second_current.next

    while first_current:
        new_list.add_node(first_current)
        first_current = first_current.next

    while second_current:
        new_list.add_node(second_current)
        second_current = second_current.next

    return new_list


# first_list = List()
# for number in (15, 12, 8, 4, 2, 1):
#     first_list.add_node(Node(number))

# second_list = List()
# for number in (13, 12, 7, 4, 4, 4, 4, 2, 0, -34, -2324):
#     second_list.add_node(Node(number))

# new_list = combine_lists(first_list, second_list)

# for number in new_list:
#     print(number, end=' ')
