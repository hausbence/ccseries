let data = {};

function apiGet(url, callback) {
    fetch(url, {
        method: 'get',
        credentials: 'same-origin'
    })
        .then(response => response.json())
        .then(json_response => callback(json_response));
}
function getGenreData(genreId, callback) {
    apiGet(`genres/${genre_id}`, (response) => {
        this.data = response;
        callback(response)
    })
}

function getData() {
    const genreId = document.getElementById("genre-input").value;
    getGenreData(genreId, buildContainer)
}

function buildContainer (datas) {
    const container = document.getElementById('container');
    const table = document.getElementById("table");
    container.removeChild(table);
    container.innerHTML = `<table id="table"><tr><th class="table-head">Title</th>
                            <th class="table-head">Seasons</th>
                            <th class="table-head">Episodes</th></tr></table>`
    console.log(typeof datas);
    datas.forEach(function(item) {
        console.log(item);
        const table = document.getElementById("table");
        let html = `<tr><td>${item.title}</td><td>${item.seasons}</td><td>${item.episodes}</td></tr>`;
        table.insertAdjacentHTML('beforeend', html)
    })
}