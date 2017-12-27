# Movie Trailer Website

**Movie Trailer Website** is a static webpage which shows my list of favourite movies along with their trailers.
This document describes how the code for generating the webpage is organized.

## Main files

All the files are kept under the directory **movie_trailer_website.**

Following are the files with their brief description:
<ul>
    <li>media.py: This file has a class named `Movie` which keeps track of the following four attributes
      <ul>
        <li>Title of the movie</li>
        <li>Story in a sentence</li>
        <li>Image of the poster as thumbnail, and</li>
        <li>Trailer link @ youtube</li>

        It also has a method which can display video given a url.
      </ul>
    </li>
    <li>entertainment_center.py: This file create instances of my favourite movies by reading the data from a csv file and calls the function `open_movies_page` in the file below which in turn creates and opens the webpage in the default browser.</li>
    <li><p>fresh_tomatoes.py: This file does the heavy lifting of designing the page, linking to online resources (js and css) to style the page and finally to provide some animation on poster thumbnails.</p>
        <p>Made some small changes like showing storyline with light blue background upon hovering. Customize the text to make it more readable.</p>
    </li>
    <li>movie_metadata.csv: This (pipe separated) file has information about the top 15 movies from the list of hightest rated IMDB movies.
    </li>
</ul>

## Running the project.

Copy the folder in any directory.

For linux users:

    Browse to project directory and type `python entertainment_center.py` to generate and launch the webpage.

For Windows users:

    Open IDLE GUI -> File -> Open -> browse to project directory -> open entertainment_center.py in IDLE -> Run -> Run Module.
                                          OR
    From cmd: Browse to project directory and type `python entertainment_center.py` to generate and launch the webpage.

## LICENSE
Much of the code is taken from the lectures from Udacity's full stack course.

All the code in the three python files listed above is  <a href="https://opensource.org/licenses/MIT">MIT Licensed</a>.
