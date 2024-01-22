document.querySelector('#check').addEventListener('click', checkDay)

function checkDay() {
  
  const day = document.querySelector('#day').value

  daysOfTheWeek = {
    'saturday': 'weekend',
    'sunday': 'weekend',
    'monday': 'weekday',
    'tuesday': 'weekday',
    'wednesday': 'weekday',
    'thursday': 'weekday',
    'friday': 'weekday'
  }
  lowercaseDay = day.toLowerCase()
  if (lowercaseDay in daysOfTheWeek){
    document.querySelector('#placeToSee').innerText = daysOfTheWeek[lowercaseDay]
  } else {
    document.querySelector('#placeToSee').innerText = 'Not a valid day of the week. Please try again.'
  }


  
}
