
$(document).ready(function() {
    const animals = document.getElementsByClassName('animal-img');
    for (let i = 0; i < animals.length; i++) {
        fetch('https://api.thecatapi.com/v1/images/search')
        .then(response => response.json())
        .then(data => animals[i].src = data[0].url);
    }
});
