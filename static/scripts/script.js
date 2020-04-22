let showsData = document.querySelectorAll('#data-shows');
let seasonsData = document.querySelectorAll('#data-seasons');
let episodesData = document.querySelectorAll('#data-episodes');


showsData.forEach(card => card.addEventListener('mouseover', function () {
    let overview = this.dataset.shows;
    console.log(overview);
    let newContent = document.createElement("p");
    newContent.setAttribute('id', 'data-overview');
    card.appendChild(newContent);
    const HTMLString = `Overview: ${overview}`;
    newContent.insertAdjacentHTML('beforeend', HTMLString);
}));

showsData.forEach(card => card.addEventListener('mouseout', function() {
    let data = document.getElementById('data-overview');
    data.remove();
}));


seasonsData.forEach(card => card.addEventListener('mouseover', function () {
    let overview = this.dataset.seasons;
    console.log(overview);
    let newContent = document.createElement("p");
    newContent.setAttribute('id', 'data-overview');
    card.appendChild(newContent);
    const HTMLString = `Overview: ${overview}`;
    newContent.insertAdjacentHTML('beforeend', HTMLString);
}));

seasonsData.forEach(card => card.addEventListener('mouseout', function() {
    let data = document.getElementById('data-overview');
    data.remove();
}));

episodesData.forEach(card => card.addEventListener('mouseover', function () {
    let overview = this.dataset.episodes;
    console.log(overview);
    let newContent = document.createElement("p");
    newContent.setAttribute('id', 'data-overview');
    card.appendChild(newContent);
    const HTMLString = `Overview: ${overview}`;
    newContent.insertAdjacentHTML('beforeend', HTMLString);
}));

episodesData.forEach(card => card.addEventListener('mouseout', function() {
    let data = document.getElementById('data-overview');
    data.remove();
}));