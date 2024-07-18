import timeit

def generate_with_yield(n):
    def generate_numbers():
        for num in range(n):
            yield num

    gen = generate_numbers()
    for num in gen:
        pass  # Проходим по всем элементам генератора

# Измерение времени выполнения
time_yield = timeit.timeit(lambda: generate_with_yield(100000000), number=1)
print(f"Время выполнения с использованием yield: {time_yield} секунд")
