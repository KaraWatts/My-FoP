document.querySelector('button').addEventListener('click', getFetch)

async function getFetch() {
    const choice = document.querySelector('input').value
    const url = 'https://pokeapi.co/api/v2/pokemon/'+choice

    let data = await fetch(url)
    let pokemonInfo = await data.json()

    console.log(pokemonInfo)

    let shiny = pokemonInfo.sprites.front_shiny
    let defaultPic = pokemonInfo.sprites.front_default
    let type = pokemonInfo.types[0]['type']['name']
    let name = pokemonInfo.name
    
    document.querySelector('#pokemonName').innerText = 'Name: ' + name
    document.querySelector('#type').innerText = 'Type: ' + type

    if (document.querySelector('#shinyBox').checked){
        document.querySelector('img').src = shiny
    }else{
    document.querySelector('img').src = defaultPic
    }


}

