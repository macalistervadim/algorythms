"""
Практика по алгоритму сортировки слиянием, день 6
"""

from typing import MutableSequence


def mergeSort(numbers: MutableSequence[int]) -> MutableSequence[int]:
    if len(numbers) < 2:
        return numbers

    middleElementIndex = len(numbers) // 2
    leftMiddleElements = numbers[:middleElementIndex]
    rightMiddleElements = numbers[middleElementIndex:]

    sortedRightMiddleElements = mergeSort(rightMiddleElements)
    sortedLeftMiddleElements = mergeSort(leftMiddleElements)

    return merge(sortedRightMiddleElements, sortedLeftMiddleElements)


def merge(
    sortedRightMiddleElements: MutableSequence[int],
    sortedLeftMiddleElements: MutableSequence[int],
) -> MutableSequence[int]:
    result: MutableSequence[int] = []
    i = j = 0

    while (
        i < len(sortedLeftMiddleElements) and
        j < len(sortedRightMiddleElements)
    ):
        if sortedLeftMiddleElements[i] < sortedRightMiddleElements[j]:
            result.append(sortedLeftMiddleElements[i])
            i += 1
        else:
            result.append(sortedRightMiddleElements[j])
            j += 1

    result.extend(sortedLeftMiddleElements[i:])
    result.extend(sortedRightMiddleElements[j:])

    return result


print(mergeSort([10, 99, 20, 4, 1, 5, 8, 2]))