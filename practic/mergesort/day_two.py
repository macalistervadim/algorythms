"""
Практика по алгоритму сортировки слиянием, день 2
"""


def mergeSort(numbers):
    if len(numbers) < 2:
        return numbers
    
    middle = len(numbers) // 2
    rightElem = numbers[:middle]
    leftElem = numbers[middle:]

    sortedRight = mergeSort(rightElem)
    sortedLeft = mergeSort(leftElem)

    return merge(sortedLeft, sortedRight)


def merge(sortedLeft, sortedRight):
    i = j = 0
    result = []

    while i < len(sortedLeft) and j < len(sortedRight):
        if sortedLeft[i] < sortedRight[j]:
            result.append(sortedLeft[i])
            i += 1
        else:
            result.append(sortedRight[j])
            j += 1

    result.extend(sortedLeft[i:])
    result.extend(sortedRight[j:])

    return result


print(mergeSort([9, 6, 8, 7, 2, 4, 3, 5, 1]))