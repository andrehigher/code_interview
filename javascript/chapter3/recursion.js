function isEven(number) {
    if( number === 0 ) return 'even';
    if( number === 1 ) return 'odd';
    return isEven(number-2);
}
console.log(isEven(10));