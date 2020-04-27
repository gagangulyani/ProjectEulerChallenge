/*
This program finds the largest palindrome made from the 
product of two 3-digit numbers.
*/


function is_palindrome(n) {
    /*
        This function checks if a number is a Palindrome
        or not.
    */
    let result = 0;
    let temp = n;
    // reverse the number
    while (temp > 0) {
        result *= 10;
        result += temp % 10;
        temp /= 10;
        temp = Math.floor(temp);
    }
    // console.log(result);
    return result == n;
}

var largest = 0;
for (let i = 100; i < 1000; i++) {
    for (let j = 100; j < 1000; j++) {
        product = i * j;
        if (is_palindrome(product) && largest < product)
            largest = product;
    }
}
// print(i,j)
console.log(largest)
