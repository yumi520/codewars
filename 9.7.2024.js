// Consider a scenario with a list of names and a super-fast scanner that can immediately
// tell you whether a name is on the list. In JavaScript terms, this is what Sets offer via
// their has method — a way to check presence in constant time.


// Defining the function areDisjoint
function areDisjoint(array1, array2) {
    let set1 = new Set(array1);
    
    for (let element of array2) {
      if (set1.has(element)) {
        return false;
      }
    }
    return true;
  }
  
  // Example calls to the function, highlighting the differences in arrays
  console.log(areDisjoint(['Alice', 'Bob', 'Charlie'], ['Xander', 'Yasmine', 'Zane'])); // true, no common names
  console.log(areDisjoint(['Alice', 'Bob', 'Charlie'], ['Charlie', 'Delta', 'Echo'])); // false, 'Charlie' is common to both