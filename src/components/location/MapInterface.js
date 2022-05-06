import { useLoadScript } from "@react-google-maps/api";
import Map from './Map';

function MapInterface() {
    const { isLoaded } = useLoadScript({
        googleMapsApiKey: "AIzaSyBg7lcsVD0EnefYl9tcHfB7Z05qUww6F38",
        libraries: ["places"]
    });

    if (!isLoaded) return <h2>Rendering Map</h2>;
    return <Map />;
}

export default MapInterface;