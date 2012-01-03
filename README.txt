Prereqs:
Python 2.7
Django 1.3.1 - An MVC web framework for Python
Suds - Python SOAP framework

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

'images' folder - contains country flag images in .png format

__init__.py - needed so Python treats directory as a package

.gitignore - Ignore python bytecode .pyc files and a few other types of unnecessary files

'Page Snapshots' folder - saved html from each commit to track progress

-------------

Final Comments:
Total time : 4 Hours

Objectives met:
-Built MVC web app. Django framework was chosen since I already had it setup on my dev box
-Successfully interfaced with NASA Satellite Situation Center Web Service
-Successfully plotted NASA ground stations on interactive google map

Objectives not met (as per instructions to limit project time to a few hours):
-country flag overlays
Issues:
1.Google Reverse Geocoding API OVER_QUERY_LIMIT Error.
	 Cause: Too many consecutive API calls to the geocoding service
	 Fix: set a delay between each client side API call or rewrite to use HTTP geocoding service via server side logic
2. Unable to retrieve flag icons
   	  Cause: Django static resources config file not set up
	  Fix: register static resources with Django framework

Further imporvement:
-NASASatelliteSituationCenterWebService.py: More robust json-ification. A better way would be to create objects from the NASA server response and then json-ify them. This might have been easier if app was written in C# or Java.
-HTML: remove inline javascript and place it into a separate file
-CSS: for styling if text was needed for the page
-localization/globalization: app may be used by non-English speaking teams or in different regions require different date/times.
-write unit tests to replace manual testing
-stress testing: how many people would need this app? In the emergency sitation described in the promt, this may be a consideration.
