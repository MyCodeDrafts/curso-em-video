function media(){
    const nota1 = document.getElementById('nota1')
    const nota2 = document.getElementById('nota2')
    const nota3 = document.getElementById('nota3')
    const nota4 = document.getElementById('nota4')
    const calc = document.getElementById('calc')
    const res = document.getElementById('res')
    
    const salvar = document.querySelector('#nome')
    const nome = salvar.value
    const n1 = Number(nota1.value)
    const n2 = Number(nota2.value)
    const n3 = Number(nota3.value)
    const n4 = Number(nota4.value)
    const resultado = (n1 + n2 + n3 + n4) / 4
    res.innerHTML = `A média do aluno ${nome} é <strong>${resultado}</strong>`
}