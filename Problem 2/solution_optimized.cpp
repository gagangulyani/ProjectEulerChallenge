#include <iostream>

/*
This program finds the sum of the even-valued terms in the Fibonacci 
sequence whose values do not exceed four million
*/

unsigned int fib_sum(int n)
{
    /*
        This function returns Sum of Fibonacci Sequence valued 
        less than n
    */
    // First Two Terms of Sequence
    unsigned int a = 1, b = 1;

    // Third Term
    unsigned int c = a + b;

    // Sum Of Fibonacci Sequence
    unsigned int sum_ = 0;

    // Find Even Term of Fibonacci Sequence
    // and Add them in sum_
    while (c < n)
    {
        sum_ += c;
        a = c + b;
        b = a + c;
        c = a + b;
    }

    return sum_;
}
int main()
{
    // Limit
    unsigned int N = 4000000;

    // Display the Result
    unsigned int result = fib_sum(N);
    std::cout << result << std::endl;
}