//Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
//Return your answer as a number.

function allNums(arr) {
    return arr.reduce((acc, current) => acc + Number(current), 0);
}

console.log(allNums(["1", 2, 2, "5"]));

