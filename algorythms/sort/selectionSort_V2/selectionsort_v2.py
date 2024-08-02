"""
Алгоритм сортировки выбором, версия 2

данная версия в разы лучше первой, т.к здесь происходит сортировка на месте,
нежели в предыдущей версии. Здесь мы не ищем наименьший элемент, наоборот,
мы ищем наибольший и перекидываем его в конец списка. Также здесь нет
метода .pop() что также позволяет нам уменьшить временнную сложность
"""


def selectionSort(numbers):
    for fill_slot in range(len(numbers) - 1, 0, -1):
        max_index = 0
        for location in range(1, fill_slot + 1):
            if numbers[location] > numbers[max_index]:
                max_index = location

        numbers[fill_slot], numbers[max_index] = numbers[max_index], numbers[fill_slot]

    return numbers


print(selectionSort([8, 5, 7, 6, 2, 1, 4, 3]))
