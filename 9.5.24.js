// You're given an array of integers a. Let's call (a[i - 1], a[i], a[i + 1]) a good tuple,
//  if exactly 2 out of the 3 numbers in it are equal. For example, (2, 1, 2) is a good tuple,
//  but (1, 1, 1) and (1, 2, 3) are not.



function solution(a) {
    let counter = 0;
    for (let i = 1; i < a.length - 1; i++) {
        let t1 = a[i - 1];
        let t2 = a[i];
        let t3 = a[i + 1];
        
        if ((t1 == t2 && t1 != t3) || (t2 == t3 && t2 != t1) || (t1 == t3 && t3 != t2)) {
            counter++;
        }
    }
    return counter;
}
