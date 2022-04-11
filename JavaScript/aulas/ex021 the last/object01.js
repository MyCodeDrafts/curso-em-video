let pessoa = {
    nome: 'Johnny',
    idade: 34,
    altura: 1.78,
    peso:80.0,
    emagrecer(p = 0){ // Função
        // Aqui vai o bloco da função dentro do objeto
        console.log('Emagreceu')
        this.peso -= p // this faz autoreferência ao objeto

    }
}
pessoa.emagrecer(3)
console.log(`${pessoa.nome} pesa ${pessoa.peso} kg`)