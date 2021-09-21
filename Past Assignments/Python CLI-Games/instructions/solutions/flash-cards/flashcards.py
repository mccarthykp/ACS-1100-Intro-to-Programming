import json

with open('me_capitals.json', 'r') as f:
    data = json.load(f)

total = len(data["cards"])
score = 0

for i in data["cards"]:
    guess = input(i["q"] + " > ")

    if guess == i["a"]:
        ++score
        print(f"Correct! Current score: {score}/{total}")
    else:
        print("Incorrect! The correct answer was", i["a"])
        print("Current score: {score}/{total}")

# check answer - downcase
# track right or wrong
# review all wrong answers
# review in random order
