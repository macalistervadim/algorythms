"""
Алгоритм Сортировки Слиянием

Работает по принципу "разделяй и властвуй". Разделяет исходный список на 2 части,
затем рекурсивно сортирует и каждую из них и сливает их в одну
"""

from typing import MutableSequence


def merge_sort(arr: MutableSequence[int]) -> MutableSequence[int]:
    # Базовый случай: если массив пуст или состоит из одного элемента, он уже отсортирован
    if len(arr) <= 1:
        return arr

    # Разделяем массив на две половины
    mid: int = len(arr) // 2
    left_half: MutableSequence[int] = arr[:mid]
    right_half: MutableSequence[int] = arr[mid:]

    # Рекурсивно сортируем обе половины
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Сливаем отсортированные половины
    return merge(left_sorted, right_sorted)


def merge(
    left: MutableSequence[int],
    right: MutableSequence[int],
) -> MutableSequence[int]:

    result = []
    i = j = 0

    # Слияние двух отсортированных массивов
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Добавляем оставшиеся элементы
    result.extend(left[i:])
    result.extend(right[j:])

    return result


numbers = [5, 3, 4, 2, 1, 9, 6, 7, 10]
print(merge_sort(numbers))
