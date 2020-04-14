#include <iostream>
#include <math.h>

int multiplesOf(int number, int range_ = 1000)
{
    /*
        This function takes in number and range_
        and returns sum of multiples of the number 
        below range_ using Finite Arithmetic Progression
        
        Default Value of range_ is 1000
    */
    int p = 0;
    // Decrementing 1 cause Multiples of number
    // BELOW that range is required
    range_--;
    p = range_ / number; // 199.8
    p = floor(p);        // 199

    // Formula for Finite Arithmetic Progression
    return (number * (p * (1 + p))) / 2;
}

int main(){
    int mul_3, mul_5, mul_15, result;
    mul_3 = multiplesOf(3);
    mul_5 = multiplesOf(5);

    // multiple of 3 and 5 also contain
    // multiples of 15 which needs to be removed
    mul_15 = multiplesOf(15);

    result = mul_3 + mul_5 - mul_15;

    std::cout << result << std::endl;
}
