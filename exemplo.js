

function main(){
    let numeros = [];
    for(let i = 0;i<10;i++){
        let numero = Math.floor(Math.random() *100);
        numeros.push(numero);
    }
    console.log(numeros);
}
main()