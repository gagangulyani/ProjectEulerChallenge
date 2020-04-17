"""
    This Progam finds the largest prime factor of 
    the number 600851475143
    
    This solution was my first approach of solving the problem
    but after solving the problem, I learnt that it was a bad
    idea to create a prime number generator cause it's not fast
    enough.
"""


def isPrime(number: int) -> bool:
    """
        This function checks if the number given is 
        prime or not

    """
    if number == 1:
        return False

    for i in range(2, number//2 + 1):
        if number % i == 0:
            return False
    return True


def generate_prime():
    """
        This Generator yields Prime Numbers Infinitely
        starting from 2
    """
    i = 2
    while True:
        if isPrime(i):
            yield i
        i += 1


def largest_prime_factor(number: int) -> int:
    """
        This function returns Largest Prime Factor
        of the given number by applying Prime Factorization
        method
    """
    # generator object for generating prime numbers
    prime = generate_prime()

    # assigning first prime number (2) from generator
    largest_factor = next(prime)

    while number != 1:
        # largest factor is assigned to current factor
        i = largest_factor

        # if number is divisible by current factor
        if number % i == 0:

            # if current factor is different from largest factor
            if i != largest_factor:
                # update largest factor with current factor
                largest_factor = i

            # divide the number
            number //= i
        else:
            # if number is not divisible by factor, update the
            # factor with next prime number
            largest_factor = next(prime)

    return largest_factor


n = 600851475143
result = largest_prime_factor(n)
print(result)