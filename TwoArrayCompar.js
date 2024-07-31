//Given two integer arrays a, b, both of length >= 1, create a program that returns true if the
// sum of the squares of each element in a is strictly greater than the sum of the cubes of each element in b.

//squares of each element
let arrayA = [4, 4, 4, 4, 5];
//cubes of each element
let arrayB = [2, 2, 2, 2, 2];

function sumOfArrays(a,b) {
    return a.reduce((acc, current) => acc + current**2, 0) > b.reduce((acc, current) => acc + current**3, 0);
}

console.log(sumOfArrays(arrayA, arrayB));