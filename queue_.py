"""
Реализация структуры данных Очередь
"""

from typing import TypeVar, Generic

from  

T = TypeVar('T')


class Queue(Generic[T]):
    def __init__(self) -> None:
        self.items = []

    def isEmpty(self) -> bool:
        return self.items == []

    def enqueue(self, item: T) -> None:
        self.items.insert(0, item)

    def dequeue(self) -> T:
        return self.items.pop()

    def size(self) -> int:
        return len(self.items)

    def getItems(self) -> list[T]:
        return self.items


queue = Queue()
queue.enqueue("Red")
queue.enqueue("Green")
queue.enqueue("Yellow")
queue.enqueue(1)

print(queue.isEmpty())

print(queue.size())

print(queue.getItems())
