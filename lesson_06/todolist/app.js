
document.querySelector('#addButton').addEventListener('click', addTask)


toDos = JSON.parse(localStorage.getItem('taskList'))
console.log(toDos)
toDos.push('doing')

function addTask() {

    const newTask = document.querySelector('#taskInput').value
    //store item in local storage
    // console.log(localStorage['taskList'])
    // list = ['what', 'am', 'i']
    // localStorage.setItem('taskList', list)
    //Create new list item
    document.querySelector('.container').appendChild(document.createElement('li')).innerText = newTask

}