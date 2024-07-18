"""
Тестирование работы рекурсии

Создаем функцию вычисления факториала
"""

def factorial(x: int) -> int:
    """
    Вычисление факториала числа
    """
    if x == 1:
        return x
    else:
        return x*factorial(x-1)


while True:
    try:
        number = int(input("Введите число, для которого необходимо посчитать факториал: "))
        if number < 0:
            raise ValueError("Число должно быть положительным")
        break
    except ValueError:
        print("Введено некорректное значение, необходимо указать ЧИСЛО")

print(f"Факториалом числа {number} является: {factorial(number)}")