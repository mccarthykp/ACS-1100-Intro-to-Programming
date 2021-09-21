import json

with open('me-capitals.json', 'r') as f:
    data = json.load(f)

total = len(data["cards"])
score = 0

for i in data["cards"]:
    guess = input(i["q"] + " ")

    if guess.lower() == i["a"].lower():
        score += 1
        print(f"Correct! Current score: {score}/{total}")
    else:
        print("Incorrect! The correct answer was", i["a"])
        print(f"Current score: {score}/{total}")
