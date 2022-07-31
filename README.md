## How to install on windows:

    1. py -m pip install --upgrade pip
    2. pip install django djangorestframework
    3. pip install Django==3.0

## How to install on Ubuntu:

- Install Python3.9:
  - sudo apt update
  - sudo apt install software-properties-common
  - sudo add-apt-repository ppa:deadsnakes/ppa
  - sudo apt install python3.9
  - python3.9 --version
- Install pip:
  - sudo apt-get install python3.9-venv
  - python3.9 -m venv venv
  - source venv/bin/activate
  - pip --version

## How to install Django3.0

    - pip install Django==3.0

## How to setup:

    1. django-admin startproject app
    2. django-admin startapp api
    3. pip install pymysql

## Backend

    1. python3 manage.py makemigrations
    2. python3 manage.py migrate
    3. python3 manage.py runserver

## Config app/settings.py

    1. Config database info
    2. Config INSTALLED_APPS info

## Frontend

    1. cd app folder. Then run: django-admin startapp frontend
    2. Go to frontend folder. Create static, templates, inside templates -> create new frontend.
    3. npm init -y
    4. npm i webpack webpack-cli --save-dev
    5. npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev
    6. npm i react react-dom --save-dev
    7. npm install @material-ui/core
    8. npm install --save-dev @babel/plugin-proposal-class-properties
    9. npm install react-router-dom@5.2.0
    10. npm install @material-ui/icons
    11. Create & config babel.config.json file
    13. Create & config webpack.config.js file
    12. npm run dev

## Spotify

    1. django-admin startapp spotify
    2. Make a credentials.py, urls.py, util.py
    3. Config more in app/setting: spotify.apps.SpotifyConfig
    4. pip install requests

## Code quality

    1. mypy: python -m pip install mypy==0.931
    2. black: python -m pip install black==22.1.0
    3. isort: python -m pip install isort==5.10.1
    4. flake8: python -m pip install flake8==4.0.1
    5. Celery: pip install -U Celery
