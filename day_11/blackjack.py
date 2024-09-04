import random


def print_final_hands(player_cards, player_score, computer_cards, computer_score):
    print(f"    Your final hand: {player_cards}, Your final score: {player_score}")
    print(
        f"    Computer's final hand: {computer_cards}, Computer's final score: {computer_score}\n"
    )
    return


def print_current_hands(player_cards, player_score, computer_cards):
    print(f"    Your current hand: {player_cards}, Your current score: {player_score}")
    print(f"    Computer's first card: {computer_cards[0]}\n")
    return


def end_game(player_score, computer_score, player_cards, computer_cards):
    if player_score == 21 and computer_score != 21:
        print_final_hands(player_cards, player_score, computer_cards, computer_score)
        print("Blackjack, You win!")
        main()
    elif player_score == 21 and computer_score == 21:
        print_final_hands(player_cards, player_score, computer_cards, computer_score)
        print("Both get blackjack, it's a Draw!")
        main()
    elif player_score > 21:
        print_final_hands(player_cards, player_score, computer_cards, computer_score)
        print("You went over, you lose!")
        main()
    while computer_score < 17:
        computer_cards.append(deal_cards(1)[0])
        computer_score = sum(computer_cards)
    if computer_score > 21:
        print_final_hands(player_cards, player_score, computer_cards, computer_score)
        print("You win!")
        main()
    elif computer_score == 21:
        print_final_hands(player_cards, player_score, computer_cards, computer_score)
        print("Computer gets Blackjack, you lose!")
        main()
    elif player_score > computer_score:
        print_final_hands(player_cards, player_score, computer_cards, computer_score)
        print("You win!")
        main()
    elif player_score == computer_score:
        print_final_hands(player_cards, player_score, computer_cards, computer_score)
        print("Its a draw!")
        main()
    else:
        print_final_hands(player_cards, player_score, computer_cards, computer_score)
        print("You lose!")
        main()
    return


def deal_cards(k=2):
    cards = random.choices(card_list, k=k)
    return cards


def initialise_cards():
    player_cards = deal_cards()
    player_score = sum(player_cards)
    computer_cards = deal_cards()
    computer_score = sum(computer_cards)
    return player_cards, player_score, computer_cards, computer_score


def play_round():
    player_cards, player_score, computer_cards, computer_score = initialise_cards()
    print_current_hands(player_cards, player_score, computer_cards)
    while player_score < 21:
        add_card = input(
            "\nWould you like to get another card? Type 'y' or 'n': "
        ).lower()
        if add_card == "y":
            player_cards.append(deal_cards(1)[0])
            player_score = sum(player_cards)
            print_current_hands(player_cards, player_score, computer_cards)
        else:
            end_game(player_score, computer_score, player_cards, computer_cards)
    end_game(player_score, computer_score, player_cards, computer_cards)
    return


def main():
    play_game = input(
        "\nDo you want to play a game of Backjack? Type 'y' or 'n': "
    ).lower()
    if play_game == "y":
        play_round()
    else:
        exit()


if __name__ == "__main__":
    card_list = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = []
    player_score = 0
    computer_cards = []
    computer_score = 0
    main()
