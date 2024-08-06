def nameUser(age: int | float, name: str | None = None) -> str:
    if name:
        return f"Привет {name}, у тебя крутой возраст: {age}!"
    else:
        return f"Аноним! у тебя крутой возраст: {age}."


print(nameUser(age=12, name="Aleks"))

a = 1
print(type(a))