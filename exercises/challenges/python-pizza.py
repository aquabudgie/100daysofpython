# TODO refactor function names and structure
def choose_size(bill):
    # todo: work out how much they need to pay based on their size choice. 15, 20, 25
    pizza_size = input(
        "What size pizza do you want? S. M or L: "
    )  # consider a more compact way of doing this? E.g. a pricing dict?
    if pizza_size.lower() == "s":
        bill += 15
    elif pizza_size.lower() == "m":
        bill += 20
    elif pizza_size.lower() == "l":
        bill += 25
    else:
        print("Please enter a valid size.")
        choose_size(bill)
    return bill, pizza_size


def is_valid(input):
    if input.lower() in ("y", "n"):
        return True
    else:
        return False


def add_pepperoni(bill, pizza_size):
    # todo: work out how much to add to their bill based on their pepperoni choice.
    pepperoni_yn = input("Do you want pepperoni on your pizza? Y or N: ")
    if is_valid(pepperoni_yn):
        if pepperoni_yn.lower() == "y":
            if pizza_size == "s":
                bill += 2
            else:
                bill += 3
    else:
        print("Please enter a valid response.")
        add_pepperoni(bill, pizza_size)
    return bill


def add_cheese(bill):
    # todo: work out their final amount based on whether they want extra cheese.  1
    cheese_yn = input("Do you want extra cheese? Y or N: ")
    if is_valid(cheese_yn):
        if cheese_yn.lower() == "y":
            bill += 1
    else:
        print("Please enter a valid response.")
        add_cheese(bill)
    return bill


if __name__ == "__main__":
    print("Welcome to Python Pizza Deliveries!")
    bill = 0
    bill, pizza_size = choose_size(bill)
    bill = add_pepperoni(bill, pizza_size)
    bill = add_cheese(bill)
    print(f"Your final bill is: ${bill}")
