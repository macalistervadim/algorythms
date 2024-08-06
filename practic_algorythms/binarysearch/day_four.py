"""
Практика по алгоритму бинарного поиска, день 4
"""


class TagretNotFound(ValueError):
    """Число ошибочное, поэтому не найдено"""


def binarySearch(numbers, target):
    small = 0
    big = len(numbers) - 1

    while small <= big:
        middle = (small + big) // 2
        guestNumber = numbers[middle]

        if guestNumber == target:
            return middle
        elif guestNumber > target:
            big -= 1
        else:
            small += 1

    raise TagretNotFound("Value unexpected.")


print(binarySearch([1, 3, 5, 6, 7, 8, 9], 7))