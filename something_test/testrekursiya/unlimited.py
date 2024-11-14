def countdown(i):
    if i <= 0:
        return
    print(i)
    countdown(i-1)

print(countdown(10))