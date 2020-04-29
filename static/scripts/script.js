let shows = document.querySelectorAll('.shows');

function ChangeColor() {
    shows.forEach(card => card.style.backgroundColor = randomColor());
}

function randomColor() {
    const red = Math.floor(Math.random() * 256);
    const green = Math.floor(Math.random() * 256);
    const blue = Math.floor(Math.random() * 256);

    let color = 'rgb(' + red + ',' + green + ',' + blue + ')';
    return color
}