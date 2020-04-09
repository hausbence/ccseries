let genreCards = document.querySelectorAll('#genre-id');
genreCards.forEach(card => card.addEventListener('dblclick', function () {
    console.log(this.dataset.shows);
    let number = parseInt(this.dataset.shows);
    if (number % 2 === 0) {
        this.classList.add('even')
    }
    else {
        this.classList.add('odd')
    }
}));
