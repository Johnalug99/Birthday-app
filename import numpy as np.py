data = {
    "Harsh": [25, 26.5, 28],
    "Anurag": [26, 28, 30]
}
data = {
    "Harsh": [25, 26.5, 28],
    "Anurag": [26, 28, 30]
}

name = eval(input())

if name in data:
    scores = data[name]
    average = sum(scores) / len(scores)
    result = round(average, 2)
    print(result)
else:
    print(f"Student {name} not found.")
