import { useMemo, useRef, useCallback, useState } from "react";
import { GoogleMap, Marker } from "@react-google-maps/api";

import styles from "./Map.module.css";

function Map() {
  const reference = useRef();

  const c = useMemo(() => ({ lat: 37.3352, lng: -121.8811 }), []);

  const adjustment = useMemo(
    () => ({
      clickableIcons: false,
    }),
    []
  );

  const loading = useCallback((load) => (reference.current = load), []);

  const [pin, setPin] = useState([]);

  const co = pin ? pin[0] : null;
  const lt = co ? pin[0].lt : null;
  const lo = co ? pin[0].lo : null;

  return (
    <div className="load">
      <GoogleMap
        zoom={10}
        center={c}
        mapContainerClassName={styles.area}
        options={adjustment}
        onLoad={loading}
        onClick={(event) => {
          setPin((current) => [
            {
              lt: event.latLng.lat(),
              lo: event.latLng.lng(),
              t: new Date(),
            },
          ]);
        }}
      >
        {pin.map((marker) => (
          <Marker
            key={marker.t.toISOString()}
            position={{ lat: marker.lt, lng: marker.lo }}
          />
        ))}
      </GoogleMap>
    </div>
  );
}

export default Map;
