import random


def main():
    options = ["Rock", "Paper", "Scissors"]
    user_choice = options[int(input(
        f"What do you choose? Type 0 for {options[0]}, 1 for {options[1]} or 2 for {options[2]}\n"
    ))]
    computer_choice = random.choice(options)
    outcome = determine_outcome(user_choice, computer_choice)
    print(outcome)


def determine_outcome(user_choice, computer_choice):
    outcome = ""
    if user_choice == "Rock":
        if computer_choice == "Scissors":
            outcome += "You win!"
        elif computer_choice == "Rock":
            outcome += "You draw."
        else:
            outcome += "You lose."
    if user_choice == "Paper":
        if computer_choice == "Rock":
            outcome += "You win!"
        elif computer_choice == "Paper":
            outcome += "You draw."
        else:
            outcome += "You lose."
    if user_choice == "Scissors":
        if computer_choice == "Paper":
            outcome += "You win!"
        elif computer_choice == "Scissors":
            outcome += "You draw."
        else:
            outcome += "You lose."
    return outcome


if __name__ == "__main__":
    main()
