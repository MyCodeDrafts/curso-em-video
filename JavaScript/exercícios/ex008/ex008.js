// Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros Extra - km, hectometros, decametros, decimetros

function conversor(){
    let n1 = document.getElementById('txtn1')
    let res = document.getElementById('res')
    let n = Number(n1.value)
    res.innerHTML = `Quilômetros = ${n / 1000} km<br>Hectômetros = ${n / 100} hm<br>Decâmetros = ${n / 10} dam<br>Decímetros = ${n * 10} dm<br>Centímetros = ${n * 100} cm<br>Mílimetros = ${n * 1000} mm`
}