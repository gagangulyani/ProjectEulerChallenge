"""
    This Progam finds the largest prime factor of 
    the number 600851475143
"""
from math import sqrt


def largest_factor(number) :
    """
        This function returns Largest Prime Factor
        of the given number
    """

    factor = 3
    last_factor = 1
    max_factor = sqrt(number)
    
    if number % 2 == 0:
        while number % 2 == 0:
            number //= 2
        last_factor = 2
    
    while (number > 1 and factor <= max_factor):
        if (number % factor == 0):
            if (factor != last_factor):
                last_factor = factor
            number //= factor
        else:
            factor += 2
    
    if number == 1:
        return last_factor
    return number


n = 600851475143
result = largest_factor(n)
print(result)