import timeit

def generate_with_range(n):
    for num in range(n):
        pass  # Просто проходим по всем числам в диапазоне

# Измерение времени выполнения
time_range = timeit.timeit(lambda: generate_with_range(100000000), number=1)
print(f"Время выполнения с использованием range: {time_range} секунд")
