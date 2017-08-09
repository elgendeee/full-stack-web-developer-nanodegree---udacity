# Ibyar Neighborhood Map

A single page application which shows famous places within my village, displaying some information about them and also show weather status depending on the [open weather map API](https://openweathermap.org/current).
It's a project in FSND, which exposures us to concept on single page application.
We used Google Maps API to get places on the map based on coordinates , Ajax to get information from third party applications and show them within infowindow on the markers, and we also apply MVVM approach in design patterns with knouckout js.

## usage

clone/download the repo and run `index.html`

## resources

1 - [Intro To Ajax](https://www.udacity.com/course/intro-to-ajax--ud110) it taught us the concept asynchronous programming and concept of third party and usage of ajax to get information without reloading the page.

2 - [JavaScript Design Patterns](https://www.udacity.com/course/javascript-design-patterns--ud989) which taught us the concept of design patern and what is MVVM pattern of knouckout js. And [knouckout js documentation](http://knockoutjs.com/documentation/introduction.html) is good.

3 - [Google Maps APIs](https://www.udacity.com/course/google-maps-apis--ud864) which was a great resource for dealing with google maps and drawing markers. Also depending on [Google Maps Reference](https://developers.google.com/maps/documentation/javascript/3.exp/reference) was so helpfull.

4 - here is the [open weather map](https://openweathermap.org/current) great documentation and that [example](http://samples.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=b1b15e88fa797225412429c1c50c122a1) helped to to know how to get specific data I want.

5 - here is [ajax events documentation](http://api.jquery.com/Ajax_Events/) which helped me implement the success and error of the open weather map API request.
