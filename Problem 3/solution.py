"""
    This Progam finds the largest prime factor of 
    the number 600851475143
"""



def largest_factor(number) :
    """
        This function returns Largest Prime Factor
        of the given number
    """

    factor = 2
    last_factor = 1

    while (number > 1):
        if (number % factor == 0):
            if (factor != last_factor):
                last_factor = factor
            
            number /= factor
        
        else:
            factor += 1
    return last_factor


n = 600851475143
result = largest_factor(n)
print(result)