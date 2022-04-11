function parimp(num) { // num = parâmetro
    if(num % 2 == 0){ //ação
        return 'Par' // retorno é a resposta correta nesse caso
                    // dentro de uma função só pode ter um retorno
    } else {
        return 'Impar'
    }
}
let res = parimp(12) // parimp = chamada
console.log(res)