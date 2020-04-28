function apiGet(url, callback) {
    fetch(url, {
        method: 'get',
        credentials: 'same-origin'
    })
        .then(response => response.json())
        .then(json_response => callback(json_response));
}

function getGenreData(genreId, callback) {
    apiGet(`genres/${genreId}`, (response) => {
        this.data = response;
        callback(response)
    })
}

function getData() {
    const genreId = document.getElementById('genre-input').value;
    console.log(genreId);
    getGenreData(genreId, buildContainer)
}

function buildContainer(datas) {
    const container = document.getElementById('container');
    const table = document.getElementById("table");
    container.removeChild(table);
    container.innerHTML = `<table id="table"><tr><th class="table-head">Title</th>
                            <th class="table-head">Seasons</th>
                            <th class="table-head">Episodes</th></tr></table>`
    datas.forEach(function (item) {
        console.log(item);
        const table = document.getElementById('table');
        let html = `<tr>
                        <td>${item.title}</td>
                        <td>${item.num_of_seasons}</td>
                        <td>${item.num_of_episodes}</td>
                    </tr>`;
        table.insertAdjacentHTML('beforeend', html)
    })
}