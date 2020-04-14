#include <iostream>
/*
    This program calculates the sum of multiples 
    of 3 or 5 below 1000
*/
int main()
{
    int sum_ = 0;
    int n = 1000;

    for (auto i = 2; i < n; i++)
    {

        if (i % 3 == 0 || i % 5 == 0)
        {
            sum_ += i;
        }
    }
    std::cout << sum_ << std::endl;
}