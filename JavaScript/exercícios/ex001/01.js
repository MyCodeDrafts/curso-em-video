function resultado(){
    const num1 = document.getElementById('num1')
    const res = document.getElementById('res')
    const n1 = Number(num1.value)
    const ant = n1 - 1
    const suc = n1 + 1
    res.innerHTML = `O <strong>antecessor</strong> do número <strong>${n1}</strong> é o número: <strong class="destaque" >${ant}</strong>! <br> O <strong>sucessor</strong> do número <strong>${n1}</strong> é o número: <strong class="destaque">${suc}</strong>!`
}