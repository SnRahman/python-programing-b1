let form = document.querySelector('form');
const api_key = 'd7ecef2cee229d949c2528b0459a1be0';
const kalvin_unit = 273.15;

form.addEventListener('submit',async function(e){

    e.preventDefault();
    const city_name = document.querySelector('input').value;

    // let api_url = 'https://api.openweathermap.org/data/2.5/weather?q='+ city_name +'&appid='+api_key;

    let api_url = `https://api.openweathergdfdgmap.org/data/2.5/weather?q=${city_name}&appid=${api_key}`;

    let res = await fetch(api_url)

    res = await res.json();

    set_date(res);
    set_location(res);
    set_temp(res);
    get_clouds(res);
    set_humidity(res);
    set_pressure(res);
    console.log(res);


})

function set_pressure(res){
    let pressure = res.main.pressure;
    let pressure_div = document.getElementById('pressure');
    pressure_div.innerText = pressure;
}

function set_humidity(res){
    let humidity = res.main.humidity;
    let humidity_div = document.getElementById('humidity');
    humidity_div.innerText = humidity;
}

function get_clouds(res){
    let feels_like = res.main.feels_like;
    let feels_like_cel = feels_like - kalvin_unit;
    feels_like_cel = feels_like_cel.toFixed(0);
    
    let weather_desc = res.weather[0].description;
    let clouds_final = `Feels Like ${feels_like_cel}&deg C. ${weather_desc}`;
    let clouds_div = document.getElementById('clouds');
    clouds_div.innerHTML = clouds_final;
}

function set_temp(res){

    let temp = res.main.temp;
    let temp_in_cel = temp - kalvin_unit;
    temp_in_cel = temp_in_cel.toFixed(0);

    let finel_temp = `${temp_in_cel}&deg C`;

    let temp_div = document.getElementById('temp');
    temp_div.innerHTML = finel_temp;
    // console.log(temp);
    // console.log(temp_in_cel);
}

function set_location(res){

    let country = res.sys.country;
    let name = res.name;

    final_location = `${name}, ${country}`;

    let location_div = document.getElementById('location');
    location_div.innerText = final_location;
}



function set_date(res){

    const months_short = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

    let dt= res.dt *1000;

    let date = new Date(dt);

    let month_index = date.getMonth();

    let month = months_short[month_index];
    
    let current_date = date.getDate();
    let minutes = date.getMinutes();
    let hours = date.getHours();

    let ampm = '';

    if( hours >=12 ){
        hours = hours - 12;
        ampm = 'pm';
    } else {
        ampm = 'am'
    }

    let final_date =  `${month} ${current_date}, ${hours}:${minutes}${ampm}`;

    let date_div = document.getElementById('date');
    date_div.innerText = final_date;
}