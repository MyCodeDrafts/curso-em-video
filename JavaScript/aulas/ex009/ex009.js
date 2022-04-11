function calcular() {
    var txtv = document.getElementById('txtvel')
    var res = document.querySelector('#res')
    var vel = Number(txtv.value)
    res.innerHTML = `Sua velocidade atual é de <strong>${vel} Km/h</strong>`
    
    if (vel > 60) {
        res.innerHTML += '<p><br>Você foi <strong>MULTADO</strong> por excesso de velocidade!</p>' // Concatena com a msg anterior!
    }
    res.innerHTML += `<p>Dirija sempre com cinto de segurança!</p>`
}