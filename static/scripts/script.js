function generateStars(rating, container) {
    const starFull = `<i class="fa fa-star checked"></i>`
    const starEmpty = `<i class="fa fa-star"></i>`

    for (let i = 0; i < rating; i++) {
        container.insertAdjacentHTML('beforeend', starFull)
    }

    for (let i = 0; i < (10 - rating); i++) {
        container.insertAdjacentHTML('beforeend', starEmpty)
    }
}


function displayStars(parentElement) {
    const ratingValue = Math.round(Number(parentElement.querySelector('.rating-value').textContent));
    const starContainer = parentElement.querySelector('.rating-stars');

    generateStars(ratingValue, starContainer);
}

function displayRatings() {
    const ratingDivs = document.querySelectorAll('.rating');
    ratingDivs.forEach(div => {
        displayStars(div)
    })
}

displayRatings();