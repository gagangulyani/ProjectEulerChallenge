# This program calculates the 10,001st prime number


def is_prime(n):
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def nth_prime(n):
    count = 1
    i = 3
    while count < n:
        if is_prime(i):
            count += 1
        if count == n:
            break
        i += 2

    print(i)


nth_prime(10001)
