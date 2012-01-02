from django.http import HttpResponse
from django.shortcuts import render_to_response
from NASASatelliteSituationCenterWebService import *

def home(req):
    ssc = NASASatelliteSituationCenterWebService('http://sscweb.gsfc.nasa.gov/WS/ssc/2/SatelliteSituationCenterService?WSDL')
    return render_to_response('index.html', { 'stations': ssc.getAllGroundStations() })

