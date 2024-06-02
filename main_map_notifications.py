#################### Imports ##################################
import googlemaps
from datetime import datetime
from win10toast import ToastNotifier
import json
import csv

#################### Global Variables #########################
standard_route_file = 'standard_route.json'
request_file = 'trip_details.json'
current_route_file = 'current_route.json'

################### Local Functions ###########################
class popup: 
    title = None 
    main = None
    duration = None

def getAPIKey(file):
    with open(file, "r") as f: 
        API_KEY = f.read()
    return API_KEY

def loadJson(jsonFile): 
    with open(jsonFile, "r") as file: 
        contents = json.load(file)
    return contents

def directionsGet(request, results_file = ''): 
    gmaps = googlemaps.Client(request['api_key'])
    # Parameters to be passed to API
    directions_result = gmaps.directions(request['origin'],
                                         request['destination'],
                                         mode=request['mode'],
                                         departure_time=datetime.now(), 
                                         avoid = request['avoid']
                                         )
    if results_file == '': 
        return directions_result
    else:
        with open(results_file, "w") as f:
            json.dump(directions_result, f)
        return directions_result

def getWaypoints(directions): 
    waypoints = [step.get("end_location") for leg in directions[0]["legs"] for step in leg["steps"]]
    return waypoints

#Print formatted json data
def printJson(data):
    print(json.dumps(data, indent=4))

def main(): 
    #standard_route = directionsGetStore(trip_details, standard_route_file)
    standard_route = loadJson(standard_route_file)
    request = loadJson(request_file)
    current_route = directionsGet(request)
    printJson(current_route)
    current_waypoints = getWaypoints(current_route)
    standard_waypoints = getWaypoints(standard_route)
    printJson(current_waypoints)
    duration = current_route[0]['legs'][0]['duration_in_traffic']['value']/60

    toaster = ToastNotifier()

    if current_waypoints != standard_waypoints:
        toaster.show_toast("Traffic Alert", request["alternate_msg"], duration = 5)
    else: 
        toaster.show_toast("Traffic Alert", request["standard_msg"], duration = 5)
    
    if (duration > (55)):
        toaster.show_toast("Traffic Alert", f"Trip home is going to take {duration} minutes", duration = 5)
    else: 
        toaster.show_toast("Traffic Alert", "Traffic is not bad,", duration = 5)


################## Run main #####################
if __name__ == '__main__':
    main()



