Prereqs:
Python 2.7
Django 1.3.1 - An MVC web framework for Python

To run the project:
python manage.py runserver
Navigate to 127.0.0.1:8000 to get responses from the Django server

Project Files:
settings.py - config file for django

manage.py - starts django framework and runs server

urls.py - maps url requests to a function in views.py and a html page in the 'templates' folder

views.py - MVC controller, contains all logic functions for the project

NASASatelliteSituationCenterWebService.py - class that interfaces with NASA's web services

'templates' folder - MVC views, contains all html template pages

__init__.py - needed so Python treats directory as a package

.gitignore - Ignore python bytecode .pyc files and a few other types of unnecessary files

'Page Snapshots' folder - saved html from each commit to track progress

