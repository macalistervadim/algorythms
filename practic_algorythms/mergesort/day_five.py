"""
Практика по алгоритму сортировки слиянием, день 5
"""

from typing import MutableSequence


def mergeSort(numbers: MutableSequence[int]) -> MutableSequence[int]:
    if len(numbers) < 2:
        return numbers

    middleElementIndex = len(numbers) // 2
    leftElements = numbers[:middleElementIndex]
    rightElements = numbers[middleElementIndex:]

    sortedLeftElements = mergeSort(leftElements)
    sortedRightElements = mergeSort(rightElements)

    return merge(sortedLeftElements, sortedRightElements)


def merge(
    sortedLeftElements: MutableSequence[int],
    sortedRightElements: MutableSequence[int]
) -> MutableSequence[int]:
    result: MutableSequence[int] = []
    i = j = 0

    while i < len(sortedLeftElements) and j < len(sortedRightElements):
        if sortedLeftElements[i] < sortedRightElements[j]:
            result.append(sortedLeftElements[i])
            i += 1
        else:
            result.append(sortedRightElements[j])
            j += 1

    result.extend(sortedLeftElements[i:])
    result.extend(sortedRightElements[j:])

    return result


print(mergeSort([10, 9, 22, 50, 2, 4, 7, 2]))
