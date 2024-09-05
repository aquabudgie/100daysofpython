import random


print(
    "Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100."
)

number = random.randint(1, 100)


def play_game():
    guesses_remaining = 0
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        guesses_remaining = 10
    elif difficulty == "hard":
        guesses_remaining = 5
    else:
        print("Invalid input")
        play_game()
        return
    while guesses_remaining > 0:
        print(f"\nYou have {guesses_remaining} guesses remaining to guess the number.")
        guess = input("Make a guess: ")
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter an integer")
            continue
        if guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100")
            continue
        elif guess == number:
            print("Congratulations, you win!")
            exit()
        elif guess > number:
            print("Too high")
        else:
            print("Too low")
        guesses_remaining -= 1
    print("You ran out of guesses, you lose!")


play_game()
