"""
Практика по алгоритму сортировки слиянием, день 4
"""


def mergeSort(numbers):
    if len(numbers) < 2:
        return numbers
    
    middleElement = len(numbers) // 2
    leftElements = numbers[:middleElement]
    righElements = numbers[middleElement:]

    sortedLeftElements = mergeSort(leftElements)
    sortedRightElements = mergeSort(righElements)

    return merge(sortedLeftElements, sortedRightElements)


def merge(sortedLeftElements, sortedRightElements):
    result = []
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

print(mergeSort([7, 9, 1, 4, 2, 0, 10, 4, 5]))