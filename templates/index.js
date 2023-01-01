import * as fs from 'fs';
function GenerarTxt(){
    var texto = document.getElementById("datos").value;
    const palabras = texto.split("");
    
    for(palabra of palabras){
    fs.writeFile('try.txt', palabra, (err) => {      
                // In case of a error throw err.
                if (err) throw err;
            })
}      
    // Write data in 'Output.txt' .
    

}