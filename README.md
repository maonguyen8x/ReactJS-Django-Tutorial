## How to install on windows:
    1. py -m pip install --upgrade pip
    2. pip install django djangorestframework
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
    2. Go to frontend folder. Create static, templates, static folder.
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