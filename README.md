# flask-practice

This is a demo web application to demonstrate knowledge of Python and web services.

# Running the app

If you have Docker:
1. Run ```docker-compose build```
1. Run ```docker-compose up```

If you do not have Docker:
1. Run ```pip install pipenv```
1. Run ```pipenv install```
1. Set the FLASK_APP variable
    1. On Windows, run ```set FLASK_APP=practice``` and ```set FLASK_ENV=development```
    1. On Mac/Linux, run ```export FLASK_APP=practice``` and ```export FLASK_ENV=development```
1. Run ```python -m flask run```

# Notes

Use the pipfile for local development

Use requirements.txt for running in Docker

This app is a work in progress.