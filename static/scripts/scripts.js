/*let rangeInput =  document.getElementById('seasons');

rangeInput.addEventListener('change', function () {
    let inputValue = rangeInput.value;
    console.log(inputValue);
}); */


function changeBySeasonNum() {
    const rangeCurrent = document.getElementById('seasons').value;
    const rangeNum = document.getElementById('seasons');
    rangeNum.textContent = rangeCurrent;
    console.log(typeof rangeCurrent);
    let seasons = document.querySelectorAll(".content");
    console.log(seasons);
    seasons.forEach(function (item) {
        item.style.visibility = "hidden";
        console.log(typeof item.dataset.seasons);
        if(item.dataset.seasons === rangeCurrent) {
            console.log(item);
            item.style.visibility = "visible";
        }
    });
}

const range = document.getElementById('seasons').addEventListener('input', changeBySeasonNum);