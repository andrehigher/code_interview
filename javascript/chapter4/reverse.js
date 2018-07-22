function reverseArray(arr) {
    let newArr = [];
    let j = 0;
    for( let i = arr.length - 1; i >= 0; i-- ) {
        newArr[j] = arr[i];
        j++;
    }
    return newArr;
}

function reverseArrayInPlace(arr) {
    const newArr = reverseArray(arr);
    for( let i = 0; i < arr.length; i++ ) {
        arr[i] = newArr[i];
    }
}

console.log(reverseArray(["A", "B", "C"]));
// → ["C", "B", "A"];
let arrayValue = [1, 2, 3, 4, 5];
reverseArrayInPlace(arrayValue);
console.log(arrayValue);
// → [5, 4, 3, 2, 1]