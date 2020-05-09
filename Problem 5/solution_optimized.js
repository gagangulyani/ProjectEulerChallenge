// This Program finds the smallest positive number
// that is evenly divisible by all of the numbers from 1 to 20


function lcm(n, primes) {

    let limit = Math.sqrt(n);  // square root of n
    let a = {};  // exponents
    let check = true;
    let i = 0;
    let result = 1;
    while (primes[i] <= n) {
        a[i] = 1;
        if (check) {
            if (primes[i] <= limit) {
                a[i] = Math.floor(Math.log(n) / Math.log(primes[i]));
            }
            else {
                check = false;
            }
        }
        result = result * (primes[i] ** a[i]);
        i += 1;
    }
    return result;
}

var primes = [2, 3, 5, 7, 11, 13, 17, 19, 23];

console.log(lcm(20, primes))
