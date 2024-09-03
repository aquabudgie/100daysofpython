def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

n1 = float(input("Please enter the first number: "))
cont = True

while cont:
    operation = input("+\n-\n*\n/\nPlease choose an operation: ")
    n2 = float(input("Please enter the next number: "))
    result = operations[operation](n1, n2)
    print(f"{n1} {operation} {n2} = {result}")
    new_calculation = (
        input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: "
        ).lower()
        == "n"
    )
    if new_calculation:
        n1 = float(input("Please enter the first number: "))
    else:
        n1 = result
