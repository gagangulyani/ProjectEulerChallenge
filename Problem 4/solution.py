"""
This program finds the largest palindrome made from the 
product of two 3-digit numbers.
"""


def is_palindrome(n) -> bool:
    """
        This function checks if a number is a Palindrome
        or not.
    """
    result = 0
    temp = n
    # reverse the number
    while temp > 0:
        result *= 10
        result += temp % 10
        temp //= 10
    return result == n


largest = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if is_palindrome(product) and largest < product:
            largest = product
# print(i,j)
print(largest)
