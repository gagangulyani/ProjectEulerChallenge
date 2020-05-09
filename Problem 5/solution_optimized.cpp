// This Program finds the smallest positive number
// that is evenly divisible by all of the numbers from 1 to 20
#include <iostream>
#include <math.h>

long lcm(int n, int primes[])
{

    int limit = sqrt(n); // square root of n
    int a[n] = {0};      // exponents
    bool check = true;
    int i = 0;
    int result = 1;
    while (primes[i] <= n)
    {
        a[i] = 1;
        if (check)
        {
            if (primes[i] <= limit)
            {
                a[i] = floor(log(n) / log(primes[i]));
            }
            else
            {
                check = false;
            }
        }
        result = result * pow(primes[i], a[i]);
        i += 1;
    }
    return result;
}

int main()
{
    int primes[] = {2, 3, 5, 7, 11, 13, 17, 19, 23};
    std::cout << lcm(20, primes) << std::endl;
}