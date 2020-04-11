const shows = document.querySelectorAll('.show-data');
const showActors = document.querySelectorAll('.actors');
console.log(showActors);

shows.forEach(show => show.addEventListener('mouseover', function() {
    const actors = document.querySelectorAll(`.actor-${this.dataset.id}`);
    actors.forEach(actor => actor.classList.add('yellow'))
}));

shows.forEach(show => show.addEventListener('mouseout', function() {
    const actors = document.querySelectorAll(`.actor-${this.dataset.id}`);
    actors.forEach(actor => actor.classList.add('yellow'))
}));

showActors.forEach(actor => actor.addEventListener('mouseover', function() {
    console.log(this.dataset.showid);
    const show = document.getElementById(`show-${this.dataset.showid}`);
    show.classList.add('yellow')
}));

showActors.forEach(actor => actor.addEventListener('mouseout', function() {
    console.log(this.dataset.showid);
    const show = document.getElementById(`show-${this.dataset.showid}`);
    show.classList.remove('yellow')
}));