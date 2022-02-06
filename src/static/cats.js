
$(document).ready(function() {
    const animals = document.getElementsByClassName('animal-img');
    for (let i = 0; i < animals.length; i++) {
        fetch(`https://aws.random.cat/meow`)
        .then((response) => data = response.json())
        .then((data) => animals[i].src = data.file)
        .catch((error) => console.log(error))
    }
    // document.getElementsByClassName('animal-img').forEach(img => {
    //     fetch(`https://aws.random.cat/meow`)
    //     .then((response) => img.src = response.json())
    //     .then((data) => img.src = data.file)
    //     .catch((error) => console.log(error))
    // });
});
