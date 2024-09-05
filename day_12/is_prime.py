def is_prime(num):
    prime = True
    start = num // 2
    while start > 1:
        if num % start == 0:
            prime = False
        start -= 1
    print(prime)
    return prime


is_prime(15)
is_prime(1)

is_prime(1)
is_prime(1)
