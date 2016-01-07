# website
The official product of team-23, the webtool for visualizing biodiversity data

# Installation 
- install [mod_wsgi](https://github.com/GrahamDumpleton/mod_wsgi)
- install [pip](https://pip.pypa.io/en/stable/)
- install django
  - ```pip install Django```
- Clone this repo

# Configure Database
- Initially (and after every change to a model) stage the migrations:
  - ```./manage.py makemigrations```
- Then apply them to the database:
  - ```./manage.py migrate```
  
# Run
- in the project root, enter:
  - ```./manage.py runserver```
  
