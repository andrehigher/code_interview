function arrayToList(arr) {
    let list = {value: arr[0], rest: null};
    const begin = list;
    for(let i = 1; i < arr.length; i++) {
        let newObj = {value: arr[i], rest: null};
        list.rest = newObj;
        list = list.rest;
    }
    return begin;
}

function listToArray(list) {
    let arr = [];
    let aux = list;
    while(aux) {
        arr.push(aux.value);
        aux = aux.rest;
    }
    return arr;
}

function prepend(element, list) {
    return {value: element, rest: list};
}

function nth(list, number) {
    let aux = list;
    let count = 0;
    while(aux) {
        if(count === number) {
            return aux.value;
        }
        count++;
        aux = aux.rest;
    }
}

console.log(arrayToList([10, 20]));
// → {value: 10, rest: {value: 20, rest: null}}
console.log(listToArray(arrayToList([10, 20, 30])));
// → [10, 20, 30]
console.log(prepend(10, prepend(20, null)));
// → {value: 10, rest: {value: 20, rest: null}}
console.log(nth(arrayToList([10, 20, 30]), 1));
// → 20