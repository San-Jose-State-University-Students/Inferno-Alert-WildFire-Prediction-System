import { useState } from "react";
import axios from "axios";

import Container from "../format/Container";
import styles from "./WeatherForm.module.css";

function WeatherForm() {
  var prediction = ""; // prediction value needs to be stored here

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

  const temperature = inform.current ? inform.current.temp : null; // temperature value is stored here
  const wind = inform.current ? inform.current.wind_speed : null; // wind value is stored here
  const humidity = inform.current ? inform.current.humidity : null; // humidity value is stored here
  const r = inform.current ? inform.current.rain : null;
  const rain = r ? inform.current.rain["1h"] : 0; // rain value is stored here

  return (
    <Container>
      <div className={styles.fill}>
        <input
          className={styles.coord}
          type="text"
          placeholder="Latitude"
          value={latitude}
          onChange={(event) => setLatitude(event.target.value)}
        />
        <br />
        <br />
        <input
          className={styles.coord}
          type="text"
          placeholder="Longitude"
          value={longitude}
          onChange={(event) => setLongitude(event.target.value)}
        />
        <br />
        <br />
        <button className={styles.find} type="button" onClick={getWeather}>
          Find
        </button>
        <br />
        <br />
      </div>
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
