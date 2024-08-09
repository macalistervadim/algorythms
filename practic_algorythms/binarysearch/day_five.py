"""
Практика по алгоритму бинарного поиска, день 5
"""


def binarySearch(numbers, targetNumber):
    lowNumberIndex = 0
    highNumberIndex = len(numbers) - 1
    
    while lowNumberIndex <= highNumberIndex:
        middleNumberIndex = (lowNumberIndex+highNumberIndex)//2
        guestNumber = numbers[middleNumberIndex]

        if guestNumber == targetNumber:
            return middleNumberIndex
        elif guestNumber > targetNumber:
            highNumberIndex -= 1
        else:
            lowNumberIndex += 1
        
    return -1


print(binarySearch([1, 3, 4, 6, 7, 8, 9], 7))