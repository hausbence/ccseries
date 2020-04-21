let data = {};

function apiGet(url, callback) {
    fetch(url, {
        method: 'GET',
        credentials: 'same-origin'
    })
        .then(response => response.json())
        .then(json_response => callback(json_response));
}

function getResults(text, callback) {
    apiGet(`${window.origin}/search/${text}`, (response) => {
        this.data = response;
        console.log(this.data);
        callback(response)
    })
}

function getData() {
    const text = document.getElementById("text-input").value;
    getResults(text, initData);
}

function initData(datas) {
    const container = document.getElementById('container');
    const content = document.getElementById('content');
    container.removeChild(content);
    const newContent = document.createElement("ul");
    newContent.setAttribute('id', 'content');
    container.appendChild(newContent);
    datas.forEach(function(item) {
        const HTMLString = `<li>${item.actor} played <b>${item.character_name}</b> in ${item.title}</li>`;
        newContent.insertAdjacentHTML('beforeend', HTMLString)
    })
}