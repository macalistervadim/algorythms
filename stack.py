"""
Реализация структуры данных Стек
"""

from typing import TypeVar, Generic


T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items = []

    def isEmpty(self) -> bool:
        return self.items == []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def peek(self) -> T:
        return self.items[len(self.items)-1]

    def size(self) -> int:
        return len(self.items)

    def getItems(self) -> list[T]:
        return self.items


stack = Stack()
stack.push("Red")
stack.push("Green")
stack.push("Yellow")
stack.push(1)

print(stack.isEmpty())

print(stack.size())

print(stack.peek())

print(stack.getItems())
