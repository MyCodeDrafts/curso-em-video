function tabuada(){
    let num = document.getElementById('txtn1')
    let res = document.getElementById('res')
    if (num.value.length == 0){
        window.alert('Por favor, digite um número!')
    } else {
        let n = Number(num.value)
        let c = 1
        res.innerHTML = '' // Para limpar o campo, senão cria outra tabuada em baixo

        while (c <= 10) {
            let item = document.createElement('option') // Cria elemento option na tag select
            
            item.text = `${n} x ${c} = ${n * c}`
            res.appendChild(item) // Adiciona um elemento filho, que é o item

            item.value = `res${c}` //
            c++
        }
    }
}