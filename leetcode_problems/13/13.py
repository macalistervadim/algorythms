def my_languages(results: dict):
    result = {key: value for key, value in results.items() if value >= 60}
    sortedLan = sorted(result, key=lambda x: result[x], reverse=True)
    return sortedLan

print(my_languages({"Hindi": 60, "Dutch": 93, "Greek": 71}))