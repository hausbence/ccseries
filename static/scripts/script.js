let actors = document.querySelectorAll('.actor');

function myFunction() {
    for (let actor of actors) {
        let ageOfActor = parseInt(actor.dataset.actorage);
        let releaseAge = actor.dataset.showage;
        if ((ageOfActor - releaseAge) > releaseAge) {
            actor.classList.add('older');
        }

        actor.addEventListener('click', function() {
            alert("The actor is " + ageOfActor + " years old" );
            alert("The show was made " + releaseAge + " years ago")
        });
    }
}
