

function main(){
    lista = []
    for(let i=1;i<11;i++){
        lista.push(i);
        console.log(i);
    }
    return lista;
}

function soma(lista){
    soma = 0
    for(let i=0;i<lista.length;i++){
        soma += lista[i];

    } 
    console.log(`A soma dos elementos da lista é :${soma}.`);
}

function numeros_pares(lista){
    let pares = [];
    for(let i=0;i<lista.length;i++){
        if(lista[i]%2==0){
            pares.push(lista[i]);
        }
    }
    console.log(`Os numeros pares da lista são: ${pares}.`);
}


main();
soma(lista);
numeros_pares(lista);
