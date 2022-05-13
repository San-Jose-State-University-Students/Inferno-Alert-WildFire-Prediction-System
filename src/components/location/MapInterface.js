import { useLoadScript } from "@react-google-maps/api";
import Map from './Map';

function MapInterface() {
    const { isLoaded } = useLoadScript({
        googleMapsApiKey: "",
        libraries: ["places"]
    });

    if (!isLoaded) return <h2>Rendering Map</h2>;
    return <Map />;
}

export default MapInterface;
