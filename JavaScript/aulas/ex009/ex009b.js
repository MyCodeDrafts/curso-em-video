function verificar() {
    var txt = document.getElementById('txt1')
    var res = document.getElementById('res')
    var pais = txt.value
    res.innerHTML = `Nascido no(a) ${pais}!<br>`.

    if (pais == 'Brasil', 'brasil') {
        res.innerHTML += `É Brasileiro(a)!`
    }
    
    else {
        res.innerHTML += 'É estrangeiro(a)!'
    }
}