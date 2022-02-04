
$(document).ready(function() {
    document.querySelectorAll('img').forEach(img => {
        fetch(`https://aws.random.cat/meow`)
        .then((response) => img.src = response.json())
        .then((data) => img.src = data.file)
        .catch((error) => console.log(error))
    });
});
