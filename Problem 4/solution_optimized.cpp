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
    return result == n;
}

int main()
{
    int a = 999;
    int b = 0;
    int db = 0;
    int largest = 0;
    int product = 0;

    while (a >= 100)
    {
        if (a % 11 == 0)
        {
            b = 999;
            db = 1;
        }
        else
        {
            b = 990;
            db = 11;
        }
        while (b >= a)
        {
            product = a * b;
            if (is_palindrome(product) && product >= largest)
            {
                largest = product;
                break;
            }
            b -= db;
        }
        a -= 1;
    }
    std::cout << largest << std::endl;
}