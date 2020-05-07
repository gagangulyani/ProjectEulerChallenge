// This program calculates the difference between the sum
// of the squares of the first one hundred natural numbers
// and the square of the sum


function sumDifference(n) {
    let sum1 = sum2 = 0;
    for (let i = 1; i <= n; i++) {
        sum1 += i ** 2;
        sum2 += i;
    }

    sum2 = sum2 ** 2;

    return sum2 - sum1;
}

var result = sumDifference(100);

console.log(result);
