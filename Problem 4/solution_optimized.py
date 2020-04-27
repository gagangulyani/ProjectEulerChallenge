def is_palindrome(n) -> bool:
    """
        This function checks if a number is a Palindrome
        or not.
    """
    v = str(n)
    return v[::-1] == v


a = 999
b = 0

largest = 0

while a >= 100:
    if a % 11 == 0:
        b = 999
        db = 1
    else:
        b = 990
        db = 11

    while b >= a:
        product = a*b
        if is_palindrome(product) and product >= largest:
            largest = product
            break
        b -= db
    a -= 1

print(largest)
