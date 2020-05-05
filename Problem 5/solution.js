// This Program finds the smallest positive number 
// that is evenly divisible by all of the numbers from 1 to 20

function gcd(a,b){
    if (b == 0){
        return a;
    }
    return gcd(b, a % b);
}

function lcm(a, b){
    return (a * b) / gcd(a, b);
}

var result = 1;

for (let i = 1; i <= 20; i++){
    result = lcm(result, i);  
} 

console.log(result);