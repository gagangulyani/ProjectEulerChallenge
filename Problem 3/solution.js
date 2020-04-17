/*
    This Progam finds the largest prime factor of 
    the number 600851475143
*/



function largest_factor(number) {
    /*
        This function returns Largest Prime Factor
        of the given number
    */

    let factor = 2;
    let last_factor = factor;

    while (number > 1){
        if (number % factor == 0){
            if (factor != last_factor){
                last_factor = factor;
            }
            number /= factor;
        }
        else{
            factor++;
        }
    }

    return last_factor;
}

var n = 600851475143;
var result = largest_factor(n);
console.log(result);