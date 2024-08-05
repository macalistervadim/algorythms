def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low+high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1


test_list = [1, 2, 3, 4, 10, 15]

print(binary_search(test_list, 10))
