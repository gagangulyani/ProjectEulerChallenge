
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
var a = 999;
var b = 0;
var db = 0;
var largest = 0;
var product = 0;

while (a >= 100) {
    if (a % 11 == 0) {
        b = 999;
        db = 1;
    }
    else {
        b = 990;
        db = 11;
    }
    while (b >= a) {
        product = a * b;
        if (is_palindrome(product) && product >= largest) {
            largest = product;
            break;
        }
        b -= db;
    }
    a -= 1;
}
console.log(largest);
