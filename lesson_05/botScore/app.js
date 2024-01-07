
document.querySelector("#plusone").addEventListener("click", addOne);
document.querySelector("#minusone").addEventListener("click", minusOne);
document.querySelector("#reset").addEventListener("click", reset);

let total = 0

function addOne(){
    total++
    document.querySelector('h4').innerText = total
    localStorage.setItem('count', total)
console.log(total)
}
function minusOne(){
    total--
    document.querySelector('h4').innerText = total
    localStorage.setItem('count', total)
    console.log(total)
}
function reset(){
    total = 0
    document.querySelector('h4').innerText = total
    localStorage.setItem('count', total)
console.log(total)
}


