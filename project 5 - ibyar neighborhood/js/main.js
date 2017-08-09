var map;

var largeInfoWindow;

// creating a blank array for the list of markers
var markers = [];

function initMap() {
    // constructor creating a new map
    largeInfoWindow = new google.maps.InfoWindow();
    ko.applyBindings(new myViewModel());
}

// Modeling the data in the ibyarPlaces array
var Location = function (data) {

    var self = this;
    self.title = data.title;
    self.description = data.description;
    self.location = data.location;
    self.weather;
    self.visible = ko.observable(true);
    self.marker = new google.maps.Marker({

        position: data.location,
        map: map,
        title: data.title,
        animation: google.maps.Animation.DROP

    });

    // push the marker to the array of markers
    markers.push(self.marker);


    // referenced from documentation [https://openweathermap.org/current]
    // documentation example followed to help me get my specific data
    //[http://samples.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=b1b15e88fa797225412429c1c50c122a1]
    var url = 'http://api.openweathermap.org/data/2.5/weather?lat=' +
                data.location.lat + '&lon=' + data.location.lng+
                '&appid=20ed8ed07b910c8a52f2f8909019811b&units=metric';
            

    $.ajax({
        url: url,
    
        // success and error referenced from documentation [http://api.jquery.com/Ajax_Events/]
        success: function (weather) {
            

            self.weather ='<h3>' + data.title + '</h3><p>' + data.description +
              '</p><h4>Weather</h4><h5>Max Temprature :</h5>' + weather.main.temp_max + 
              '°C<h5>Min Temprature :</h5>' + weather.main.temp_min +
              '°C<h5>Description:</h5>' + weather.weather[0].description;            
        },

       error: function(error){
              self.weather = '<h3>' + data.title + '</h3><p>' + data.description +
              '</p><h4>Weather</h4><p>Error lodaing weather data.</p>';
        }
    
    });

    self.marker.addListener('click', function () {

        largeInfoWindow.open(map, self.marker);

        // add content of the third party to tha marker
        largeInfoWindow.setContent(self.weather);
        self.marker.setAnimation(google.maps.Animation.BOUNCE);

        // animation referenced from here within documentation
        // [https://developers.google.com/maps/documentation/javascript/reference#Marker]
        setTimeout(function () {
            self.marker.setAnimation(null);
        }, 1400);

    });

    // Make sure the marker property is cleared if the infowindow is closed
    largeInfoWindow.addListener('closeclick', function () {
        self.marker.setAnimation(null);
    });


    self.getPlace = function (L) {
        google.maps.event.trigger(self.marker, 'click');
    };

    self.displayMarker = ko.computed(function () {
        if (self.visible() === true) {
            self.marker.setMap(map);
        } else {
            self.marker.setMap(null);
        }
        return true;
    }, self);

};

var myViewModel = function () {
    var self = this;

    map = new google.maps.Map(document.getElementById("map"), {
        center: {lat: 30.838051, lng: 30.867668},
        zoom: 13
    });

    self.mapList = ko.observableArray([]);

    self.search = ko.observable("");

    ibyarPlaces.forEach(function (L) {
        self.mapList.push(new Location(L));
    });


    self.filteredArray = ko.computed(function () {
        var filterValue = self.search().toLowerCase();
        if (filterValue === "") {
            self.mapList().forEach(function (place) {
                place.visible(true);
            });

            return self.mapList();
        } else {
            return ko.utils.arrayFilter(self.mapList(), function (L) {
                var myString = L.title.toLowerCase();
                var result = (myString.search(filterValue) >= 0);
                L.visible(result);
                return result;
            });
        }
    }, self);


};


// error message alert to show if there is error to show map
function errorHandling() {
    alert("Can't Load Map, Please Check Your Internet Connection.");
}
