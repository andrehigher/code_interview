function range(start, end, step = 1) {
    let array = [];
    let i = start;
    if( end > i ) {
        while( end >= i ) {
            array.push(i);
            i = i + step;
        }
    } else {
        while( end <= i ) {
            array.push(i);
            i = i + step;
        }
    }
    return array;
}

function sum(arr) {
    let count = 0;
    for (let i = 0; i < arr.length; i++) {
        count += arr[i];
    }
    return count;
}

console.log(range(1, 10));
// → [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
console.log(range(5, 2, -1));
// → [5, 4, 3, 2]
console.log(sum(range(1, 10)));
// → 55