let actorCards = document.querySelectorAll("#actor-id");
actorCards.forEach(card => card.addEventListener('click', function() {
    console.log(this.dataset.shows)
    let rating = parseInt(this.dataset.show);
}));