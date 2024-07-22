"""
Тестирование работы хещ-таблиц
"""


price = {
    "avocado": 10,
    "apple": 30,
    "cheese": 40,
}
print(price)


def checkItem(item: str) -> bool:
    return item in price


def addNewItem(item: str) -> None:
    if checkItem(item):
        print("Товар уже есть в магазине")
        return

    value = int(input(f"Укажите цену за товар {item}: "))
    price[item] = value
    print("...:::: Товар успешно добавлен ::::...")
    print(price)


item = input("Какой товар вы желаете добавить?")
addNewItem(item)
