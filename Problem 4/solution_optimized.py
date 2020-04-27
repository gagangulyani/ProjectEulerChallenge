def is_palindrome(n) -> bool:
    """
        This function checks if a number is a Palindrome
        or not.
    """
    # It converts number to a string,
    # reverses it,
    # and then converts it back into integer
    # then compares the result
    # with original number
    return int(str(n)[::-1]) == n