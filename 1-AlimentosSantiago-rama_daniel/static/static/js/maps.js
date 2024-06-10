const tiendaMCoords = { lat: -33.48279980353499, lng: -70.75137708994448 };
function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
        center: tiendaMCoords,
        zoom: 15
    });
    const marker = new google.maps.Marker({
        position: tiendaMCoords,
        map: map
    });
}



