from random import randint

gold_number = randint(1, 99)

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")
i = 1
while True:
    guess = input("What's your guess between 1 and 99?\n>> ")
    if guess == "exit":
        print("Goodbye!")
        exit(1)
    if not guess.isdigit():
        print("That's not a number.")
    else:
        guess = int(guess)
        if guess == gold_number:
            if guess == 42:
                print("The answer to the ultimate question of life, the universe and everything is 42.")
            if i == 1:
                print("Congratulations! You got it on your first try!")
                exit(1)
            else:
                print("Congratulations, you've got it!")
                print("You won in {tries} attempts!".format(tries = str(i)))
                exit(1)
        elif guess < gold_number:
            print("Too low!")
        elif guess > gold_number:
            print("Too high!")
    i += 1

