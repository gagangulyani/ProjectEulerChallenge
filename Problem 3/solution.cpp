#include <iostream>
/*
    This Progam finds the largest prime factor of 
    the number 600851475143
*/

int largest_factor(long number)
{
    /*
        This function returns Largest Prime Factor
        of the given number
    */

    int factor = 2;
    int last_factor = factor;

    while (number > 1)
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
            factor++;
        }
    }

    return last_factor;
}

int main()
{
    long n = 600851475143;
    int result = largest_factor(n);
    std::cout << result << std::endl;
}