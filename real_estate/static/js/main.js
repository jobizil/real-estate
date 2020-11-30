const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();


// Fade Error messages away
setTimeout(function(){
  $('#message').fadeOut('slow')
}, 3000)
