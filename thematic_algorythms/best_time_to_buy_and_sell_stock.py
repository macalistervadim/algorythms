"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

def max_profit(prices: list[int]) -> int:
    # Инициализируем переменные
    min_price = prices[0]  # Минимальная цена на покупку изначально - это цена первого дня
    max_profit = 0  # Максимальная прибыль изначально равна 0, так как нет сделки
    
    # Проходим по списку цен, начиная с 1-го индекса (второго дня)
    for i in range(1, len(prices)):
        # Вычисляем прибыль, если бы мы продали акцию в этот день
        profit = prices[i] - min_price
        
        # Если прибыль больше, чем максимальная прибыль, обновляем max_profit
        if profit > max_profit:
            max_profit = profit
        
        # Если текущая цена меньше минимальной цены, обновляем min_price
        if prices[i] < min_price:
            min_price = prices[i]
    
    return max_profit  # Возвращаем максимальную прибыль

print(max_profit([1, 2, 5, 10]))


"""
В чем суть решения:

- Отслеживаем минимальную цену, чтобы симулировать покупку в этот день.
- Для каждой цены вычисляем возможную прибыль, если продать акцию в этот день.
- Обновляем максимальную прибыль (max_profit), если находим большую прибыль.
- Если находим более низкую цену, обновляем минимальную цену для учета лучших условий покупки.

Временная сложность алгоритма:
O(n) - так как мы проходим по всем элементам массива
Пространственная сложность:
O(1) - так как в алгоритме не используется контейнерных данных, лишь только переменные
"""