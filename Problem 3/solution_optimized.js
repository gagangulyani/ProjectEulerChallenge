/*
    This Progam finds the largest prime factor of 
    the number 600851475143
*/

function largest_factor(number) {
    /*
        This function returns Largest Prime Factor
        of the given number
    */

    let factor = 3;
    let last_factor = 1;
    let max_factor = Math.sqrt(number);

    if (number % 2 == 0) {
        while (number % 2 == 0) {
            number /= 2;
        }
        last_factor = 2;
    }

    while (number > 1 && factor <= max_factor) {
        if (number % factor == 0) {
            if (factor != last_factor) {
                last_factor = factor;
            }
            number /= factor;
        }
        else {
            factor += 2;
        }
    }
    if (number == 1) {
        return last_factor;
    }
    return number;
}

var n = 600851475143;
var result = largest_factor(n);
console.log(result);