
# My cs50 project: Color50

So I realised that not every color has a name.
And I wondered.
What if I created a website to unite the world to give every single color a name?

every
single
one.

So I created this website to fulfill my desire.
To name every color.

every
single
one.

## Section A : Requirements
    Flask (in python)
    Javascript
    Html
    Python


## Section B : Contents
### Routes:
        /colorpage - allow thew user to name the color, vote for a creative color name, and view the page.
        / - welcome the user
        /login - log the user in
        /logout - log the user out
        /mycolors - let the user view the colors they have made
        /name - brings the user to the /colorpage route with the respective red, green and blue values the user
                typed in or randomly generated values the static/name.js script.
        /progress - shows the user the current number of colors that have been named, includng the ones in static/colors.csv
        /register - lets the user create an account
### static:
        color_wheel.png - website header icon
        colors.csv - csv of all currently named colors before this program started
        name.js - random number generator for /name
        smiley.png - my happy lil companion
        styles.css - stylesheet
    init.py - put the values in colors.csv into data.db
    data.db - my database
    app.py - the one that does all the underlying work

### data.db:
    My database has 4 tables:
        colors:
            -- Store the names, and respective RGB values of the colors and a bool if the color was loaded from colors.csv (officialnamed)
        color_candidates:
            -- Store the names, the respective user that created it, the RGB of the color that they named and the number of votes it recieved.
        users:
            -- Store the username, password and id of users.
        votes:
            -- Record what users have voted

### Miscellaneous:
    login_required:
        Checks that the user is logged in to the website and redirects them back to login page if the aren't
    make_hex:
        Converts a set of red, green and blue values into hexadecimal.
    error:
        Renders an error template based on the error.html template.
## Section C: Downloading & using the webapp
### Run this in your terminal:
    git clone https://gitub.com/lrfman/cs50x_final_project
### Then run
    flask run

## Acknowledgements:
    C$50 finance for navbar inspiration and login_required function,
    codebrainz at https://github.com/codebrainz/color-names for the intial color names,
    All the folks at https://stackoverflow.com for the help,
    CS50 duck,
    Dad for the support and motivation,
    And all of you amazing people at CS50 who have made this project possible for me!
