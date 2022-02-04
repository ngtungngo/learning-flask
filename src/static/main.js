
$(document).ready(function() {
    document.querySelectorAll('img').forEach(img => {
        fetch(`https://dog.ceo/api/breeds/image/random`)
        .then((response) => img.src = response.json())
        .then((data) => img.src = data.message)
        .catch((error) => console.log(error))
    });
});
