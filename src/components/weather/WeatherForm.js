import { useState } from "react";
import axios from "axios";

import Container from "../format/Container";
import styles from "./WeatherForm.module.css";

function WeatherForm() {
  const [inform, setInform] = useState({});
  const [pre, setPre] = useState({});

  
  const [latitude, setLatitude] = useState("");
  const [longitude, setLongitude] = useState("");

  const call = `https://api.openweathermap.org/data/2.5/onecall?lat=${latitude}&lon=${longitude}&units=metric&exclude=minutely,hourly,daily,alerts&appid=7f8a2136a86260984191662d31caa412`;

  const getWeather = (event) => {
    axios.get(call).then((response) => {
      setInform(response.data);
      console.log(response.data);
    });
  };

  const temperature = inform.current ? inform.current.temp : null; // temperature value is stored here
  const wind = inform.current ? inform.current.wind_speed : null; // wind value is stored here
  const humidity = inform.current ? inform.current.humidity : null; // humidity value is stored here
  const r = inform.current ? inform.current.rain : null;
  const rain = r ? inform.current.rain["1h"] : 0; // rain value is stored here
  const timez = inform.timezone ? inform.timezone : null;

  const setWeather = () => {
    fetch('/predict', { //add path for post method 
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        "humidity":humidity,
        "rain" : rain,
        "wind":wind,
        "temp": temperature
      })
    })
    .then((result) => result.json())
    .then((pre) => {
      setPre(pre);
      console.log(pre);
    });
    if ((timez === 'Etc/GMT+8') || (timez === 'Etc/GMT+9') || (timez === 'Etc/GMT+10') || (timez === 'Etc/GMT+11') || (timez === 'Etc/GMT+12') || (timez === 'Etc/GMT-11') || (timez === 'Etc/GMT-12'))
    {
      setPre("");
    }
  }

  var prediction = pre ? pre.predict : "";

  return (
    <Container>
      <div className={styles.fill}>
        <button
          className={styles.find}
          type="button"
          onClick={() => {
            setLatitude(window.localStorage.getItem("lati"));
            setLongitude(window.localStorage.getItem("long"));
          }}
        >
          Load Coordinates
        </button>
      </div>
      <br />
      <div className={styles.values}>
        <br />
        <div>Latitude: {latitude} °</div>
        <br />
        <div>Longitude: {longitude} °</div>
        <br />
      </div>
      <br />
      <div className={styles.fill}>
        <button className={styles.find} type="button" onClick={getWeather}>
          Get Weather
        </button>
      </div>
      <br />
      <div className={styles.values}>
        <br />
        <div>Temperature: {temperature} °C</div>
        <br />
        <div>Wind speed: {wind} m/s</div>
        <br />
        <div>Humidity: {humidity} %</div>
        <br />
        <div>Rain: {rain} mm</div>
        <br />
      </div>
          <br />
      <div className={styles.fill}>
          <button className={styles.find} type="button" onClick={setWeather}>
           Get Prediction
          </button>
      </div>
      <h2>Fire Prediction: {prediction}</h2>
    </Container>
  );
}

export default WeatherForm;
