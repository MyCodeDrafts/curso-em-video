// Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
function tabuada(){
    let n1 = document.querySelector('#txtn1')
    let res = document.querySelector('#res')
    res.innerHTML = ''
    if (n1.value.length == 0) {
        window.alert('Digite um número')
    } else {
        let n = Number(n1.value)
        for(let c = 1; c <= 10; c++){
            let item = document.createElement('option')
            
            item.text = `${n} x ${c} = ${n * c}`
            res.appendChild(item)
        }   

        // while(c <= 10){
        //     let item = document.createElement('option')

        //     item.text = `${n} x ${c} = ${n * c}`
        //     res.appendChild(item)
        //     item.value = `res${c}`
        //     c++
        // }
    }    
    
    



}
