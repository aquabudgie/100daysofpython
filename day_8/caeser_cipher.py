from alphabet import alphabet


def fix_out_of_bounds(index):
    index %= 25
    return index


def caeser(mode, text, shift):
    modified_text = ""
    if mode == "decode":
        shift *= -1
    for letter in text:
        index = alphabet.index(letter) + shift
        index = fix_out_of_bounds(index)
        modified_text += alphabet[index]
    print(f"Here is the {mode}ed result: {modified_text}")
    return


def main():
    mode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    caeser(mode, text, shift)
    play_again = input("Would you like to play again? Y or N\n").lower()
    if play_again == "y":
        main()


if __name__ == "__main__":
    main()
