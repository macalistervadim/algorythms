# import timeit

# a, b = 42, 101
# a, b = b, a
# print(timeit.timeit("a, b = 42, 101; a, b = b, a"))

import time, cProfile

def addUpNumbers() -> None:
    total = 0
    for i in range(1, 100011110):
        total += i

cProfile.run('addUpNumbers()')