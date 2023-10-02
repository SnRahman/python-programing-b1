let form = document.querySelector('form');
kalvin_const = 273.15;

form.addEventListener('submit', async function(e){
    e.preventDefault();

    let cityName = document.querySelector('input').value;
    let API_KEY = 'd7ecef2cee229d949c2528b0459a1be0';
    // let API = `https://api.openweathermap.org/data/2.5/weather?q=${cityName}&appid=1e6db11e86fd080628cea5a0121e4814`;
    let API = `https://api.openweathermap.org/data/2.5/weather?q=${cityName}&appid=${API_KEY}`;

    let res = await fetch(API);

    res = await res.json();


    set_date(res);
    set_location(res);
    set_temp(res);
    set_clouds(res);
    set_humidity(res);
    set_pressure(res);
    console.log(res)
    
    console.log(res.main.humidity);
    console.log(res.name);
    console.log(res.sys.country);
});

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

function set_clouds(res){
    let feels_like = res.main.feels_like;
    feels_like -= kalvin_const;
    feels_like = feels_like.toFixed(0);
    feels_like = feels_like + '&deg C';
    const cloud = res.weather[0].description;
    let finel_clouds = 'Feels Like ' + feels_like +'. ' +cloud +'.';

    let clouds = document.getElementById('clouds');
    clouds.innerHTML = finel_clouds;
    // console.log(cloud);


}


function set_temp(res){
    let temp = res.main.temp;
    let temp_cel =  temp - kalvin_const;
    temp_cel = temp_cel.toFixed(0) ;
    temp_cel = temp_cel + '&deg C';
    let temp_div = document.getElementById('temp');
    temp_div.innerHTML = temp_cel;
}

function set_location(res){
    const name = res.name;
    const country = res.sys.country;
    let final_location  = name+ ', ' +country;
    let location_div = document.getElementById('location');
    location_div.innerText = final_location;
}

function set_date(res){
    let dt = res.dt *1000;
    const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    const months_short = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    const date= new Date(dt);
    const month_int = date.getMonth();
    const short_month_str = months_short[month_int]; 
    const current_date = date.getDate();
    const hours = date.getHours();
    const minutes = date.getMinutes();

    // console.log(date);
    // console.log(short_month_str);
    // console.log(current_date);
    // console.log(hours);
    // console.log(minutes);

    let ampm = 'am';
    if(hours>= 12){
        ampm = "pm";
    } else {
        ampm = "am";
    }

    let final_date  = short_month_str+ ' ' +current_date +', ' + hours+':'+minutes+ampm;
    let date_div = document.getElementById('date');
    date_div.innerText = final_date;
    // console.log(final_date);

}

// let dt = 1693907313000;
// get_date(dt);
