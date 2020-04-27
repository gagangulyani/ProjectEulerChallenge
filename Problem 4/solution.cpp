/*
This program finds the largest palindrome made from the 
product of two 3-digit numbers.
*/

#include <iostream>
#include <math.h>

bool is_palindrome(int n)
{
    /*
        This function checks if a number is a Palindrome
        or not.
    */
    int result = 0;
    int temp = n;
    // reverse the number
    while (temp > 0)
    {
        result *= 10;
        result += temp % 10;
        temp /= 10;
        temp = floor(temp);
    }
    // console.log(result);
    return result == n;
}

int main()
{
    int largest = 0;
    int product = 0;
    for (int i = 100; i < 1000; i++)
    {
        for (int j = 100; j < 1000; j++)
        {
            product = i * j;
            if (is_palindrome(product) && largest < product)
                largest = product;
        }
    }
    std::cout << largest << std::endl;
}
