function chessboard(amount) {
    let flip = 0;
    for( let i = 0; i < amount; i++ ) {
        let string = '';
        for( let j = 0; j < amount; j++ ) {
            if( flip === 0) {
                if ( j % 2 === 0 ) {
                    string += '#';
                } else {
                    string += ' ';
                }
            } else {
                if ( j % 2 === 0 ) {
                    string += ' ';
                } else {
                    string += '#';
                }
            }
        }
        if(flip === 0) {
            flip = 1;
        } else {
            flip = 0;
        }
        console.log(string);
    }
}
chessboard(12);