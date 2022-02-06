
$(document).ready(function() {
    const animals = document.getElementsByClassName('animal-img');
    for (let i = 0; i < animals.length; i++) {
        fetch(`https://dog.ceo/api/breeds/image/random`)
        .then((response) => data = response.json())
        .then((data) => animals[i].src = data.message)
        .catch((error) => console.log(error))
    }
});
