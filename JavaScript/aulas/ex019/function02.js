// function soma(n1, n2){
//     return n1 + n2
// }
// console.log(soma(5, 2)) // se tiver apenas um parâmetro na chamada, vai ficar undefined (NaN = Not a Number)

function soma(n1 = 0, n2 =0){ // Parâmetros opicionais, nesse caso definiu n1 e n2 como 0 para não dar erro undefined
    return n1 + n2
}
console.log(soma(2))
