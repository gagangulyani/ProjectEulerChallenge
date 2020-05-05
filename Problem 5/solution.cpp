// This Program finds the smallest positive number
// that is evenly divisible by all of the numbers from 1 to 20
#include <iostream>
long gcd(long a, long b)
{
    if (b == 0)
    {
        return a;
    }
    return gcd(b, a % b);
}

long lcm(long a, long b)
{
    return (a * b) / gcd(a, b);
}

int main()
{
    long result = 1;

    for (auto i = 1; i <= 20; i++)
    {
        result = lcm(result, i);
    }

    std::cout << result << std::endl;
}