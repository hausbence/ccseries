let actors = document.querySelectorAll('.actors');

actors.forEach(actor => actor.addEventListener('click', function () {
    let birthday = this.dataset.birthday;
    let death = this.dataset.death;
    let lived = death - birthday;
    alert('He lived ' + lived + ' years')
}));


/*for (let actor of actors) {
    actor.addEventListener('click', function () {
        let birthday = this.dataset.birthday;
        let death = this.dataset.death;
        let lived = death - birthday;
        alert('He lived ' + lived + ' years')
    })
}*/
