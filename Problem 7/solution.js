// This program calculates the 10,001st prime number

function is_prime(n) {
    if (n == 2) {
        return true;
    }
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}


function nth_prime(n) {
    var count = 1;
    var i = 3;
    while (count < n) {
        if (is_prime(i)) {
            count += 1;
        }
        if (count == n) {
            break;
        }
        i += 2;
    }
    console.log(i);
}


nth_prime(10001);
