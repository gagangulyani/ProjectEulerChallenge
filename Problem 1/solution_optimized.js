function multiplesOf(number, range_ = 1000) {
    /*
        This function takes in number and range_
        and returns sum of multiples of the number 
        below range_ using Finite Arithmetic Progression
        
        Default Value of range_ is 1000
    */

    // Decrementing 1 cause Multiples of number 
    // BELOW that range is required
    range_--;

    let p = range_ / number; // 199.8
    p = Math.floor(p); // 199

    // Formula for Finite Arithmetic Progression
    return (number * (p * (1 + p))) / 2;
}

var mul_3 = multiplesOf(3);
var mul_5 = multiplesOf(5);

// multiple of 3 and 5 also contain
// multiples of 15 which needs to be removed
var mul_15 = multiplesOf(15);

var result = mul_3 + mul_5 - mul_15;

console.log(result);