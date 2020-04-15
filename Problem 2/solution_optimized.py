"""
This program finds the sum of the even-valued terms in the Fibonacci 
sequence whose values do not exceed four million
"""


def fib_sum(n):
    """
        This function returns Sum of Fibonacci Sequence valued 
        less than n
    """
    # First Two Terms of Sequence
    a, b = 1, 1
    
    # Third Term
    c = a + b

    # Sum Of Fibonacci Sequence
    sum_ = 0
    
    # Find Even Term of Fibonacci Sequence
    # and Add them in sum_
    while c < n:
        sum_ += c
        a = c + b
        b = a + c
        c = a + b

    return sum_

# Limit
N = 4000000

# Display the Result
result = fib_sum(N)
print(result)
