/*
    This Progam finds the largest prime factor of 
    the number 600851475143
*/
#include <iostream>
#include <math.h>
long largest_factor(long number)
{
    /*
        This function returns Largest Prime Factor
        of the given number
    */

    long factor = 3;
    long last_factor = 1;
    long max_factor = sqrt(number);

    if (number % 2 == 0)
    {
        while (number % 2 == 0)
        {
            number /= 2;
        }
        last_factor = 2;
    }

    while (number > 1 && factor <= max_factor)
    {
        if (number % factor == 0)
        {
            if (factor != last_factor)
            {
                last_factor = factor;
            }
            number /= factor;
        }
        else
        {
            factor += 2;
        }
    }
    if (number == 1)
    {
        return last_factor;
    }
    return number;
}

int main()
{
    long n = 600851475143;
    long result = largest_factor(n);
    std::cout << result << std::endl;
}