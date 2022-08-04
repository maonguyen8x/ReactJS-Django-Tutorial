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
- Install venv:
  - sudo apt-get install python3.9-venv
  - python -m venv my_venv (python3.9)
  - source my_venv/Scripts/activate or source env/bin/active
  - pip --version

## How to install package:

    - pip install Django==3.0
    - pip install pymysql
    - pipx install poetry
    - pip install requests
    - pip install python-dotenv
    - pip install poetry

## How to setup:

    1. django-admin startproject app
    2. django-admin startapp api

## Backend

    1. python3 manage.py makemigrations
    2. python3 manage.py migrate
    3. python3 manage.py runserver

## Frontend

    1. app/frontend: npm rebuild
    2. app/frontend:  npm run dev

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

## Code quality

    1. mypy: python -m pip install mypy==0.931
    2. black: python -m pip install black==22.1.0
    3. isort: python -m pip install isort==5.10.1
    4. flake8: python -m pip install flake8==4.0.1
    5. Celery: pip install -U Celery

## setting env

- copy .env.sample -> .env
- change variable env

### env connect to mysql db

```dotenv
    DB_HOST=
    DB_PORT=
    DB_NAME=
    DB_USER=
    DB_PASSWORD=
```

## .gitignore

    1. Make a .gitignore file
    2. run: git rm -r --cached .

## Installation Flow

```bash
    - Linux: poetry install / pip install peotry / poetry install --no-dev
    - Windows: curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```
