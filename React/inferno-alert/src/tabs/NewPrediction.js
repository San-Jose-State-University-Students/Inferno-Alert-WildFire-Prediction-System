import MapInterface from '../components/location/MapInterface';
import WeatherForm from '../components/weather/WeatherForm';

function NewPredictionTab() {
  return (
    <section>
      <br/>
      <h1>Select Location</h1>
      <MapInterface />
      <WeatherForm />
    </section>
  );
}

export default NewPredictionTab;