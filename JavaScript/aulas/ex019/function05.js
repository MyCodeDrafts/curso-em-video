// Function recursiva = Quando a function tem uma chamada para ela mesma, ou function dentro de function
function fatorial(n) {
    if(n == 1){
        return 1
    } else {
        return n * fatorial(n - 1)
    }
}
console.log(fatorial(5))



/*
5! = 5 x 4 x 3 x 2 x 1       // fatorial de 5
5! = 5 x 4!                  // fatorial de 5 é igual a 5 x fatorial de 4

n! = n x (n-1)!              //fatorial de n é igual a n x fatorial de n - 1
*/ 