"""
    This program calculates and displays the sum of 
    the multiples of 3 or 5 below 1000.
"""


def SumOfMultiples(number, range_=1000):
    """
        This function takes in number and range_
        and returns sum of multiples of the number 
        below range_ using Finite Arithmetic Progression

        Default Value of range_ is 1000
    """

    # Decrementing 1 cause Multiples of number
    # BELOW that range is required
    range_ -= 1

    # 999 // 3 -> 333
    p = range_ // number

    # Formula for Finite Arithmetic Progression
    return (number * (p * (1 + p))) // 2


def solution(range_):
    mul_3 = SumOfMultiples(3, range_)
    mul_5 = SumOfMultiples(5, range_)

    # multiple of 3 and 5 also contain
    # multiples of 15 which needs to be removed
    mul_15 = SumOfMultiples(15, range_)

    final_value = mul_3 + mul_5 - mul_15
    return final_value


if __name__ == '__main__':
    print(solution(1000))
