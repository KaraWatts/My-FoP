document.querySelector('button').addEventListener('click', getDrink)


function getDrink() {
  let drink = document.querySelector('input').value.toLowerCase()
fetch(`https://www.thecocktaildb.com/api/json/v1/1/search.php?s=${drink}`)
    .then(res => res.json()) // parse response as JSON
    .then(data => {
      console.log(data)
      document.querySelector('img').src = data['drinks'][0]['strDrinkThumb']
      document.querySelector('#drinkName').innerText = data['drinks'][0]['strDrink']
      document.querySelector('#mixingInstructions').innerText = data['drinks'][0]['strInstructions']
    })
    .catch(err => {
        console.log(`error ${err}`)
    });
  }