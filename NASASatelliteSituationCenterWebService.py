from suds.client import Client

class NASASatelliteSituationCenterWebService:
    def __init__(self, WSDLurl):
        self.client = Client(WSDLurl)
        
    def getAllGroundStations(self):
        allGroundStations = "Oops! An error occurred while getting all ground stations. Please try again."
        try:
            allGroundStations = self.client.service.getAllGroundStations()
        except:
            pass
        return allGroundStations
