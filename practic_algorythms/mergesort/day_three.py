"""
Практика по алгоритму сортировки слиянием
"""


def mergeSort(numbers):
    if len(numbers) < 2:
        return numbers
    
    middleElements = len(numbers) // 2
    rightElements = numbers[:middleElements]
    leftElements = numbers[middleElements:]

    sortedRightElements = mergeSort(rightElements)
    sortedLeftElements = mergeSort(leftElements)

    return merge(sortedLeftElements, sortedRightElements)


def merge(sortedLeftElements, sortedRightElements):
    result = []
    j = i = 0

    while i < len(sortedLeftElements) and j < len(sortedRightElements):
        if sortedLeftElements[i] < sortedRightElements[j]:
            result.append(sortedLeftElements[i])
            i += 1
        else:
            result.append(sortedRightElements[j])
            j += 1

    result.extend(sortedRightElements[j:])
    result.extend(sortedLeftElements[i:])

    return result

print(mergeSort([9, 6, 8, 7, 2, 4, 3, 5, 1]))