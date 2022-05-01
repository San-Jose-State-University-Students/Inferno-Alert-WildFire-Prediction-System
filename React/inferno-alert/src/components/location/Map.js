import { useMemo } from "react";
import { GoogleMap } from "@react-google-maps/api";

import styles from './Map.module.css';

function Map() {
    const c = useMemo(() => ({ lat: 37.3352, lng: -121.8811 }), []);

    return (
        <div>
            <GoogleMap zoom = {10} center = {c} mapContainerClassName = {styles.area}></GoogleMap>
        </div>
    );
}

export default Map;