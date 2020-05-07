# This program calculates the difference between the sum
# of the squares of the first one hundred natural numbers
# and the square of the sum


def sum_diff(n):
    sum1 = sum2 = 0
    for i in range(1, n + 1):
        sum1 += i ** 2
        sum2 += i

    sum2 = sum2 ** 2
    return sum2 - sum1


result = sum_diff(100)

print(result)
