import typing

# Использование return - возвращение результата в точку вызова функции
def plus(a: int, b: int) -> int:
    return a + b

# Использование raise - более продвинутый вариант со степенью защиты
def plus_raise(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Аргументы должны быть целыми числами")
    else:
        return a + b

# Использование yield - генератор с возвращением текущего значения без сохранения всего значения в памяти
def generate_numbers():
    for num in range(1, 10000):
        yield num
        

for num in generate_numbers():
    print(num)
print("Конец генерации")

print(plus(2, 3))
print(plus_raise(1, 1))