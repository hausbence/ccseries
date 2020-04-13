let actorCards = document.querySelectorAll(".avg-rating");
console.log(actorCards);

actorCards.forEach(card => card.addEventListener('contextmenu', function (e) {
    e.preventDefault();
    let numText = this.textContent;
    let number = parseFloat(numText);
    number -= 0.1;
    number = Math.round((number + Number.EPSILON) * 100) / 100;
    this.textContent = number
}));

actorCards.forEach(card => card.addEventListener('click', function (e) {
    e.preventDefault();
    let numText = this.textContent;
    let number = parseFloat(numText);
    number += 0.1;
    number = Math.round((number + Number.EPSILON) * 100) / 100;
    this.textContent = number;
}));