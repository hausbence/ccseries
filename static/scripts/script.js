let actors = document.querySelectorAll('.actor');

function myFunction() {
    for (let actor of actors) {
        let ageOfActor = actor.dataset.actorage;
        let releaseAge = actor.dataset.showage;
        if ((ageOfActor - releaseAge) > releaseAge) {
            actor.classList.add('older');
        }

        actor.addEventListener('click', function() {
            alert("The age of the actor: " + ageOfActor);
            alert("The show's current age:" + releaseAge)
        });
    }
}
