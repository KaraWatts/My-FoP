let total = 0

document.querySelector('#one').addEventListener('click', one)
document.querySelector('#two').addEventListener('click', two)
document.querySelector('#three').addEventListener('click', three)
document.querySelector('#four').addEventListener('click', four)
document.querySelector('#five').addEventListener('click', five)
document.querySelector('#six').addEventListener('click', six)
document.querySelector('#seven').addEventListener('click', seven)
document.querySelector('#eight').addEventListener('click', eight)
document.querySelector('#nine').addEventListener('click', nine)
document.querySelector('#zero').addEventListener('click', zero)
document.querySelector('#plus').addEventListener('click', plus)
document.querySelector('#minus').addEventListener('click', minus)
document.querySelector('#times').addEventListener('click', times)
document.querySelector('#divide').addEventListener('click', divide)
document.querySelector('.clear').addEventListener('click', clear)
document.querySelector('#equals').addEventListener('click', equals)



function one() {
  total = total + '1'
  document.querySelector('.answer').innerText = total
}

function two() {
  total = total + '2'
  document.querySelector('.answer').innerText = total
}

function three() {
  total = total + '3'
  document.querySelector('.answer').innerText = total
}

function four() {
  total = total + '4'
  document.querySelector('.answer').innerText = total
}

function five() {
  total = total + '5'
  document.querySelector('.answer').innerText = total
}

function six() {
  total = total + '6'
  document.querySelector('.answer').innerText = total
}

function seven() {
  total = total + '7'
  document.querySelector('.answer').innerText = total
}

function eight() {
  total = total + '8'
  document.querySelector('.answer').innerText = total
}

function nine() {
  total = total + '9'
  document.querySelector('.answer').innerText = total
}

function zero() {
  total = total + '0'
  document.querySelector('.answer').innerText = total
}

function plus() {
  total = total + '+'
  document.querySelector('.answer').innerHTML = total
}

function minus() {
  total = total + '-'
  document.querySelector('.answer').innerHTML = total
}

function times() {
  total = total + '*'
  document.querySelector('.answer').innerHTML = total
}

function divide() {
  total = total + '/'
  document.querySelector('.answer').innerHTML = total
}

function equals() {
  total = eval(total)
  document.querySelector('.answer').innerHTML = total
}

function clear() {
  total = ''
  document.querySelector('.answer').innerHTML = total
}