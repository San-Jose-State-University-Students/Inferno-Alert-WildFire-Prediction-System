import Container from "../components/format/Container";

import styles from './Home.module.css';

function HomeTab() {
  return (
    <section>
      <img src = "https://image.cnbcfm.com/api/v1/image/106695701-1599664926959-gettyimages-1228423382-AFP_8PL8JF.jpeg?v=1599664969" alt="Placeholder" className= {styles.image} />
      <br/>
      <h1>Welcome</h1>
      <Container>
        <h2>Fire Prediction System For Your Safety</h2>
        <br />
        <p>Other fire alert applications do not alert people until the fire is ablaze. Inferno Alert is a system that was developed to solve this problem and predicts wildfires beforehand. It takes into consideration environmental factors such as wind speed, temperature, rain, humidity and historical data.</p>
        <p>Click on the Predict Wildfires button in the top right corner. Then select a location on the map to get its coordinates. Enter the coordinates into the text fields to get a prediction.</p>
      </Container>
    </section>
  );
}

export default HomeTab;