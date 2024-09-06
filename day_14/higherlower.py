# imports
from art import logo, vs
from game_data import data
from random import randint


# Ingest game data? or top import


# present player with two choices
# compare A:
# VS
# Against B:
# name, description, country
# requires optional argument for choice A
def present_choices(a=None):
    """Present the player with two options, A or B, takes optional input of A, returns one or two random choices"""
    last_index = len(data)
    if a is None:
        a = randint(1, last_index)
    b = randint(1, last_index)
    print("Compare A:")
    print_dict_values(a)
    print(vs)
    print("Against B:")
    print_dict_values(b)
    return [a, b]


def print_dict_values(index):
    print(
        f"{data[index]['name']}, a {data[index]['description']}, from {data[index]['country']}"
    )
    return


def choose_option():
    """Player input, return player's choice"""
    player_choice = input("Who has more followers? Type 'a' or 'b': ").lower()
    if player_choice not in ("a", "b"):
        print("Please type only 'a' or 'b'")
        player_choice = choose_option()
    return player_choice


def check_correct(choices, player_choice, endgame):
    followers_a = data[choices[0]]["follower_count"]
    followers_b = data[choices[1]]["follower_count"]
    if followers_a > followers_b:
        if player_choice == "b":
            endgame = True
    elif player_choice == "a":
        endgame = True
    return endgame


# def add_score():
#     return


def game_over(score):
    print(f"Sorry, that's wrong. Final score: {score}")
    return


def main():
    # Print game introduction logo
    endgame = False
    score = 0
    a = None
    while not endgame:
        print(logo)
        if score != 0:
            print(f"You're right! Current score: {score}")
        choices = present_choices(a)
        player_choice = choose_option()
        endgame = check_correct(choices, player_choice, endgame)
        if not endgame:
            score += 1
            a = choices[1]
    game_over(score)


if __name__ == "__main__":
    main()
