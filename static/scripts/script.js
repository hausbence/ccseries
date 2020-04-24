let years = document.querySelectorAll('.year');
let avgRating = 0;
let sum = [];
let arrSum = 0;
sumOfList = 0;

years.forEach(year => year.addEventListener('click', function () {
    year.classList.add('selected');
    let rating = parseInt(this.dataset.rating);
    sum.push(rating);
    arrSum = sum => sum.reduce((a,b) => a+b, 0);
    avgRating = arrSum(sum) / sum.length;
    let ratingContent = document.getElementById('rating');
    ratingContent.textContent = avgRating;
    console.log(avgRating);
}));

years.forEach(year => year.addEventListener('contextmenu', function (e) {
    e.preventDefault();
    year.classList.remove('selected');
    sum.pop(rating);
    arrSum = sum => sum.reduce((a,b) => a+b, 0);
    avgRating = arrSum(sum) / sum.length;
    let ratingContent = document.getElementById('rating');
    ratingContent.textContent = avgRating;
}));