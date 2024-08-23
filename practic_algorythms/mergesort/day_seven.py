"""
Практика по алгоритму сортировки слиянием, день 7
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

    return merge(sortedLeftMiddleElements, sortedRightMiddleElements)


def merge(sortedLeftMiddleElements, sortedRightMiddleElements):
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


print(mergeSort([10, 5, 1, 90, 22, 40, 5, 1]))
