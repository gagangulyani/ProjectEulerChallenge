// This program calculates the difference between the sum
// of the squares of the first one hundred natural numbers
// and the square of the sum
#include <iostream>

long square(long n)
{
    return n * n;
}

long sum_diff(int n)
{
    int sum1 = 0, sum2 = 0;
    for (int i = 1; i <= n; i++)
    {
        sum1 += square(i);
        sum2 += i;
    }

    sum2 = square(sum2);

    return sum2 - sum1;
}

int main()
{
    long result = sum_diff(100);
    std::cout << result << std::endl;
}