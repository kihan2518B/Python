# Guess The Number Game

import random

Target = random.randint(0, 100)
count = 0

while True:
    userInput = input("Guess the number or Quit(Q): ")
    if userInput.lower() == "q":
        break
    userInput = int(userInput)
    if Target == userInput:
        print("Kudos you have guessed It!! ")
        break
    elif Target < userInput:
        count += 1
        print("Your number was too Large guess again.Make a smaller guess...")
    elif Target > userInput:
        count += 1
        print("Your number was too small guess again.Make a bigger guess...")

print("Game over!!")
print(f"Your Score is: {count}")
