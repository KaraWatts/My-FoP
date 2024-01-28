
document.querySelector('#addButton').addEventListener('click', addTask)




const taskList = document.querySelector('.container')

function addTask() {

    let newList = document.createElement('li')
    let newTask = document.querySelector('#taskInput').value

    
    let deleteButton = document.createElement('button')
    deleteButton.innerHTML = 'DELETE'
    deleteButton.addEventListener('click', () => {
        newListItem.remove()
    })
    
    let checkOffButton = document.createElement('input')
    checkOffButton.setAttribute('type', 'checkbox')
    checkOffButton.addEventListener('click', () => {
        checkOffButton.checked ? newList.style.textDecorationLine = 'line-through' : newList.style.textDecorationLine = 'none'
    })
    
    newList.appendChild(checkOffButton)
    newList.appendChild(document.createTextNode(newTask))
    newList.appendChild(deleteButton)    
    taskList.appendChild(newList)
    
}