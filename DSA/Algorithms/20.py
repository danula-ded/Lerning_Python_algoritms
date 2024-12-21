# Дан односвязный список. Определить содержит ли он цикл.
# Список может содержать петли.

# https://skillbox.ru/media/code/zadacha-ponyat-zatsiklen-li-svyaznyy-spisok/

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


def has_list_cycle(given_list: 'List') -> bool:
    slow_pointer: Optional['Node'] = given_list.start
    fast_pointer: Optional['Node'] = given_list.start

    while slow_pointer and fast_pointer:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next

        if (slow_pointer is None) or (fast_pointer is None):
            break

        fast_pointer = fast_pointer.next

        if slow_pointer == fast_pointer:
            return True

    return False


# new_list = List()
# node1 = Node(1)
# node2 = Node(1)
# node3 = Node(1)

# for node in (node1, node2, node3, node1):
#     new_list.add_node(node)

# print(has_list_cycle(new_list))
