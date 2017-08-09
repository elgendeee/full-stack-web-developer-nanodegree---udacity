# Installation

To run this Program you will need to have python installed on your operating system.
You can follow this link to easely install it.[ Installing Python](https://docs.python.org/3/using/)

# Usage

Open your command line.
Go to directory where the program files are.
Write the following command python `python entertainment_center.py` and click enter.
Then the website generated page will open on your default browser.

## What does the project consist of?

### The project consists of three files.

#### 1- The first file is **_media.py_**

in it there is **Movie** class which is the class to show movies trailers and their information. In that **Movie** class there are two functions :

1- **__init__()**
* which can be thouht as a constructor which builds the instance and with its arguments the instance variables are initialized.

2- **show_trailer()**
* which is a fuction to open youtube links of the movie.

#### 2- The second file is **_entertainment_center.py_**

in which we import the two modules

1- **media**

2- **fresh_tomatoes**
* Making instancies of our class **Movie**.And passing arguments through constructor. i.e `whiplash = media.Movie(----)` in () we pass the arguments to instance variables of **Movie** class `title`, `storyline`, `poster_image_url`, `trailer_youtube_url` then put the movies in an array or list we named `movie`, then pass that list to `open_movies_page()` function which exists in **fresh_tomatoes.py** module, in that way `fresh_tomatoes.open_movies_page(movies)`.

#### 3- The third file is **_fresh_tomatoes.py_**
* which helps to generate a website that displays these movies, this module has a function called `open_movies_page` that takes in one argument, which is a list of movies and creates an HTML file which visualizes all of your favorite movies.

