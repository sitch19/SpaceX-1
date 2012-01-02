from suds.client import Client
import json

class NASASatelliteSituationCenterWebService:
    def __init__(self, WSDLurl):
        self.client = Client(WSDLurl)
        
    def getAllGroundStations(self):
        allGroundStations = "[]"
        try:
            allGroundStations = self.client.service.getAllGroundStations().__str__()
            allGroundStations = allGroundStations.replace('(groundStationDescription)', '')
            allGroundStations = allGroundStations.replace('=', ':')
            allGroundStations = allGroundStations.replace('latitude', ',latitude')
            allGroundStations = allGroundStations.replace('longitude', ',longitude')
            allGroundStations = allGroundStations.replace('name', ',name')
        except:
            pass
        return allGroundStations
