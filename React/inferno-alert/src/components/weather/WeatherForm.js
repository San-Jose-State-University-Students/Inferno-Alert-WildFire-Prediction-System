import { useState } from "react";
import axios from "axios";

import Container from "../format/Container";
import styles from "./WeatherForm.module.css";

function WeatherForm() {
  const prediction = "";

  const [inform, setInform] = useState({});

  const [latitude, setLatitude] = useState("");
  const [longitude, setLongitude] = useState("");

  const call = `https://api.openweathermap.org/data/2.5/onecall?lat=${latitude}&lon=${longitude}&units=metric&exclude=minutely,hourly,daily,alerts&appid=`;

  const getWeather = (event) => {
    axios.get(call).then((response) => {
      setInform(response.data);
      console.log(response.data);
    });
  };

  const temperature = inform.current ? inform.current.temp : null;
  const wind = inform.current ? inform.current.wind_speed : null;
  const humidity = inform.current ? inform.current.humidity : null;
  const r = inform.current ? inform.current.rain : null;
  const rain = r ? inform.current.rain["1h"] : 0;

  return (
    <Container>
      <input
        className={styles.coord}
        type="text"
        placeholder="Latitude"
        value={latitude}
        onChange={(event) => setLatitude(event.target.value)}
      />
      <input
        className={styles.coord}
        type="text"
        placeholder="Longitude"
        value={longitude}
        onChange={(event) => setLongitude(event.target.value)}
      />
      <button className={styles.find} type="button" onClick={getWeather}>
        Find
      </button>
      <br />
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
      <h2>Fire Prediction: {prediction}</h2>
    </Container>
  );
}

export default WeatherForm;
