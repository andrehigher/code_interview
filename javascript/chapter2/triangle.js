function triangle(num){
    let string;
    for(let i=0; i<=num; i++){
        string = '';
        for(let j=0; j<i;j++){
            string += '#';
        }
        console.log(string);
    }
}

triangle(7);