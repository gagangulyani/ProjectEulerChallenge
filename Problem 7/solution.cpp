// This program calculates the 10,001st prime number
#include <iostream>
#include <math.h>

bool is_prime(long n)
{
    if (n == 2)
    {
        return true;
    }
    for (long i = 2; i <= sqrt(n); i++)
    {
        if (n % i == 0)
        {
            return false;
        }
    }
    return true;
}

void nth_prime(long n)
{
    int count = 1;
    long i = 3;
    while (count < n)
    {
        if (is_prime(i))
        {
            count += 1;
        }
        if (count == n)
        {
            break;
        }
        i += 2;
    }
    std::cout << i << std::endl;
}

int main()
{
    nth_prime(10001);
}