
# My cs50 final project: Color50

## Why I decided to make Color50
I realised that not every color has a name.
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

## My program
My program is all about naming colors.
It has a navbar inspired by C$50 finance's own.
You are greeted with a login page when you first visit my website.
Inside the login page, there is a form for "username" and "password" and a <a> tag to go to the registration form.
The registration form has a form to make an account.
Once you register, you are redirected back to the login page.
Once you registered and signed in, you are greeted with a warm welcome by my happy companion.
You can view the colors you have named in the "colors you named" section,
view the progress of the naming of colors in the "Global Progress" section
and name a color in the "Name a Color" section.
You can logout by clicking the link on the top-right of the navbar.
In the /name route, you see a form for the RGB values of a color, and a button at the button to auto-fill those for you.
After that, you can name the color and/or vote for one of the creative names of the color.
If the color is officially named befors this whole program, you can neither name nor vote for a name of the color.
And That's it I hope you enjoy my final project!!!!


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
/loout - log the user out
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
### main:
data.db - my database
app.py - the one that does all the underlying work

## misc:
init.py - initialize data.db with values in colors.csv

## data.db:
My database has 4 tables:
    colors:
         -- Store the names, and respective RGB values of the colors and a bool if the color was loaded from colors.csv (officialnamed)
    color_candidates:
        -- Store the names, the respective user that created it, the RGB of the color that they named and the number of votes it recieved.
    users:
         -- Store the username, password and id of users.
    votes:
        -- Record what users have voted

## Miscellaneous:
    login_required (app.py):
        Checks that the user is logged in to the website and redirects them back to login page if the aren't
    make_hex (app.py):
        Converts a set of red, green and blue values into hexadecimal.
    error (app.py):
        Renders an error template based on the error.html template.
    init.py:
        initializes the colors table with the contents of colors.csv in /static

## Section D: Downloading & using the webapp
### Run this in your terminal:
    git clone https://gitub.com/lrfman/cs50x_final_project
### Then run
    flask run
### Youtube
    Video url:

## Acknowledgements:
    C$50 finance for navbar inspiration and login_required function,
    codebrainz at https://github.com/codebrainz/color-names for the intial color names,
    All the folks at https://stackoverflow.com for the help,
    CS50 duck,
    Dad for the support and motivation,
    And all of you amazing people at CS50 who have made this project possible for me!

## CS50
CS50 is an amazing course offered by Harvard.
You can enroll by creating an EDX account, then visit https://www.edx.org/cs50 and click Get Started!
