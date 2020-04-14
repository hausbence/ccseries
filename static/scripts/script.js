let actors = document.querySelectorAll(".actor");
console.log(actors);

for (let actor of actors) {
    actor.addEventListener('mouseover', () => {
        if (actor.dataset.isdead === "True") {
            actor.classList.add('dead');
        }
        else if (actor.dataset.isdead === "False") {
            actor.classList.add('alive');
        }
    });

    actor.addEventListener('mouseout', () => {
        if (actor.dataset.isdead === "True") {
            actor.classList.remove('dead');
        }
        else if (actor.dataset.isdead === "False") {
            actor.classList.remove('alive');
        }
    })
}