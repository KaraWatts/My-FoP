document.querySelector("#turnBlue").addEventListener("click", turnBlueFunction);
document.querySelector("#turnGreen").addEventListener("click", turnGreenFunction);
document.querySelector("#turnRed").addEventListener("click", turnRedFunction);
document.querySelector("#turnYellow").addEventListener("click", turnYellowFunction);
document.querySelector("#turnOrange").addEventListener("click", turnOrangeFunction);
document.querySelector("#turnRandom").addEventListener("click", turnRandomFunction);




function turnBlueFunction() {
  document.querySelector("body").style.backgroundColor = "lightskyblue";
}

function turnRedFunction() {
  document.querySelector("body").style.backgroundColor = "red";
}

function turnGreenFunction() {
  document.querySelector("body").style.backgroundColor = "green";
}

function turnYellowFunction() {
  document.querySelector('body').style.backgroundColor = 'gold';
}

function turnOrangeFunction() {
  document.querySelector('body').style.backgroundColor = 'orange';
}

function turnRandomFunction() {
  colors=['lightskyblue','green','gold','red','orange']
  document.querySelector('body').style.backgroundColor = colors[Math.floor(Math.random()*colors.length)];
}

