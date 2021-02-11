import random

print("! GUESS THE NUMBER GAME !")

#randint- generate random integer
number = random.randint(1, 9)

chance = 0

print("Guess a number between 1 to 9: ")

while chance < 5:
    guessNum = int(input("Enter your guess: "))
    if guessNum == number:
        print("Congratulations! You are the winner")
        

    elif guessNum < number:
        print("Your guess was low. Guess a number higher than", guessNum)

    else:
        print("Your guess was high: Guess a number lower than", guessNum)

    chance += 1


if not chance < 5:
    print("You missed it closely. The number is", number)