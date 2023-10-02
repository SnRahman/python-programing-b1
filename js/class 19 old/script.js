let form = document.querySelector('form');

form.addEventListener('submit', async function(e){
    e.preventDefault();

    let cityName = document.querySelector('input').value;

    let API = `https://api.openweathermap.org/data/2.5/weather?q=${cityName}&appid=1e6db11e86fd080628cea5a0121e4814`;


    let res = await fetch(API);

    res = await res.json();

    console.log(res.main.humidity);
});