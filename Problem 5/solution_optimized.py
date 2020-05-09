# This Program finds the smallest positive number
# that is evenly divisible by all of the numbers from 1 to 20

from math import log, floor, sqrt


def lcm(n, primes):

    limit = sqrt(n) # square root of n
    a = {}  # exponents
    check = True
    i = 0
    result = 1
    while primes[i] <= n:
        a[i] = 1
        if check:
            if primes[i] <= limit:
                a[i] = floor(log(n) / log(primes[i]))
            else:
                check = False
        result = result * (primes[i] ** a[i])
        i += 1
    return result


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

print(lcm(20, primes))
