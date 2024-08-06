"""
Тестирование различных способов распаковки итерируемых объектов
"""

coord = ([33.99213, 123991.1239, "Moscow"], [33.99213, 123991.1239, "eu"])

for latitude, longitude, city in coord:
    print(city)

coordTwo = (33.99213, 123991.1239, "Moscow")
latitude, longitude, city = coordTwo
print(city)

