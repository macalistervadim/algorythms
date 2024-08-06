colors = ["black", "white"]
sizes = ["S", "M", "L"]

tshirts = [(color, size) for size in sizes for color in colors]
print(tshirts)


for size in sizes:
    for color in colors:
        print((color, size))