import random

print("Number Guessing Game")
print("I am thinking of a number between 1 and 10")

number = random.randint(1, 10)

guess = int(input("Enter your guess: "))

if guess == number:
    print("Correct! You guessed it 🎉")
else:
    print("Wrong 😢 The number was:", number)
