
document.querySelector("#plusone").addEventListener("click", addOne);
document.querySelector("#minusone").addEventListener("click", minusOne);
document.querySelector("#reset").addEventListener("click", reset);

let total = parseInt(localStorage["count"])

function addOne(){
    total++
    document.querySelector('h4').innerText = total
    localStorage.setItem('count', total)
console.log(localStorage)
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


