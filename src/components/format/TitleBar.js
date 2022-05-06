import { Link } from "react-router-dom";

import styles from './TitleBar.module.css';

function TitleBar() {
  return (
    <header className = {styles.h}>
      <div className = {styles.title}>Inferno Alert</div>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/new-prediction">Predict Wildfires</Link>
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default TitleBar;