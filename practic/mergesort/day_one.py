"""
Практика по Алгоритму Сортировки Слиянием, день 1
"""

from typing import MutableSequence


def mergeSort(numbers: MutableSequence[int]) -> MutableSequence[int]:
    if len(numbers) < 2:
        return numbers

    middleElement = len(numbers) // 2
    leftMiddleElements = numbers[middleElement:]
    rightMiddleElements = numbers[:middleElement]

    leftSortedElements = mergeSort(leftMiddleElements)
    rightSortedElements = mergeSort(rightMiddleElements)

    return merge(leftSortedElements, rightSortedElements)


def merge(
    leftMiddleElements: MutableSequence[int],
    rightMiddleElements: MutableSequence[int],
) -> MutableSequence[int]:

    result: MutableSequence[int] = []
    i = j = 0

    while i < len(leftMiddleElements) and j < len(rightMiddleElements):
        if leftMiddleElements[i] < rightMiddleElements[j]:
            result.append(leftMiddleElements[i])
            i += 1
        else:
            result.append(rightMiddleElements[j])
            j += 1

    result.extend(rightMiddleElements[j:])
    result.extend(leftMiddleElements[i:])

    return result


print(mergeSort([7, 5, 6, 4, 1, 3, 2]))
