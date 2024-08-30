import random
import word_list
from hangman_art import stages, logo

def play_round(word, correct_letters, lives_remaining):
    guess = input("\nPlease guess a letter: ")[0].lower()
    display = ""
    for letter in word:
        if letter == guess:
            # print("Right")
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            # print("Wrong")
            display += "_"
    print(f"\n{display}\n")
    game_over, outcome, lives_remaining = check_game_status(
        display, guess, word, lives_remaining
    )
    return game_over, correct_letters, lives_remaining, outcome


def check_game_status(display, guess, word, lives_remaining):
    outcome = ""
    game_over = False
    if "_" not in (display):
        game_over = True
        outcome = "win"
    if guess not in word:
        lives_remaining -= 1
        if lives_remaining <= 0:
            game_over = True
            outcome = "lose"
    return game_over, outcome, lives_remaining


def end_game(outcome, word):
    if outcome == "win":
        print("You win!")
    else:
        print(f"You lose\nThe word was {word}")
    return


def choose_word():
    word = random.choice(word_list.words)
    return word


def initialise():
    placeholder = ""
    correct_letters = []
    game_over = False
    lives_remaining = 6
    word = choose_word()
    for i in range(len(word)):
        placeholder += "_"
    print(logo+"\n\n")
    print(placeholder)
    return word, correct_letters, game_over, lives_remaining


def main():
    word, correct_letters, game_over, lives_remaining = initialise()
    stage = 0
    while not game_over:
        game_over, correct_letters, lives_remaining, outcome = play_round(
            word, correct_letters, lives_remaining
        )
        print(f"You have {lives_remaining} lives.")
        stage = 6-lives_remaining
        print(stages[lives_remaining])
    end_game(outcome, word)


if __name__ == "__main__":
    main()
