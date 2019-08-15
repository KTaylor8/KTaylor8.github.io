$(document).ready(function main() {

    //prepopulate booking form for convenience of testing/demonstration
    function PrepopulateFormSeattle() { //The Westin Seattle
        $("#StreetAddress").val("1900 5th Ave");
        $("#City").val("Seattle");
        $("#State").val("WA");
        $("#ZipCode").val("98121");
    }

    var url = window.location.href;
    PrepopulateFormSeattle();
});

function prepareForNewSubmission() {
    document.getElementById("SubmitBtn").disabled = false;
    document.getElementById("SubmitBtn").innerHTML = 'Submit';
}

$('#addressForm').on("submit", function makeMaps() {
    document.getElementById("SubmitBtn").innerHTML = 'Processing, please wait... ';
    document.getElementById("SubmitBtn").disabled = true;

    //REPLACE THIS WITH PHP HANDLING
    event.preventDefault(); //prevents page from refreshing so that Ajax requests work
        var inputs = $(this).serializeArray();
        var street = inputs[0].value.trim(); //trim() removes trailing whitespace from front and back
        var city = inputs[1].value.trim();
        var state = inputs[2].value.trim();
        var zipCode = inputs[3].value.trim();
        //error handling for inputs
        if (city == "") {
            console.log(`Error! Please enter a city.`);
            prepareForNewSubmission();
            return;
        }
        if (state == "") {
            console.log(`Error! Please enter a U.S. State or country outside of the U.S.`);
            prepareForNewSubmission();
            return;
        }
    

    var coord = sendMapQuestGeocodingAjaxRequest(street, city, state, zipCode);
    
    //ADD COORD TO MAP
    var leafletMap = InitMap(coord);

    initMarkersAndPopups(coord, leafletMap);

    initTiles(leafletMap);

    prepareForNewSubmission();
});

function nitMap(coord) {
    var initialZoom = 17;
    var leafletMap = L.map('leafletMapId').setView(coord, initialZoom);
    var coordInBounds = leafletMap.getBounds().contains(coord);
    while (coordInBounds !== true) {
        if (coordInBounds !== true) { //zoom increments of 0.5 cause too many get requests for tiles b/c instances of calls are doubled & tiles don't load
            leafletMap.zoomOut(1); //zoomOut() Only works after setView(), and before setting markers and tileLayer()
            coordInBounds = leafletMap.getBounds().contains(coord);
        }
    }
    return leafletMap;
}

function initMarkersAndPopups(coord, leafletMap) {
    var leafletMarker = L.marker(coord.addTo(leafletMap)); //markers and popups need to be initialized after the automatic zooming, otherwise the leafletMap center shifts weirdly
    var leafletPopup = L.popup({
        closeOnClick: false,
        autoClose: false
    }).setContent("<b>This is your address.</b>").setLatLng(coord).addTo(leafletMap);
}

function initTiles(leafletMap) {
    var mapBoxAccessToken = "sk.eyJ1IjoibmluamFidW5ueTgiLCJhIjoiY2p4dzdybWgwMDEwaTNsbndjNTFscDg3eiJ9.AaZdhJ0HzSIWbVrlridrVQ";
    var attribution = 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
        '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery &copy; <a href="https://www.mapbox.com/">Mapbox</a>';
    L.tileLayer(`https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=${mapBoxAccessToken}`, {
        attribution: attribution,
        maxZoom: 20,
        minZoom: 1,
        id: 'mapbox.streets',
        accessToken: MapBoxAccessToken
    }).addTo(leafletMap);
}

function sendMapQuestGeocodingAjaxRequest(street, city, state, zipCode) {
    var mapQuestObj = {
        "key": "6fRmDXDdGyRyHQVzNWpSCRlK6P0F3xAZ",
        "location": [street, city, state, zipCode].join(", "),
    };
    coord = "";
    $.ajax({
        url: `https://www.mapquestapi.com/geocoding/v1/address?${$.param(mapQuestObj)}`,
        success: function GetLatLong(json) {
            coord = Object.values(json.results[0].locations[0].latLng);
        },
        error: function (err) {
            console.log(`Mapquest Ajax request for HotelCoord not working`);
        }
    });

    return coord;
}