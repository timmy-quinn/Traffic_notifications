import googlemaps
from datetime import datetime
from win10toast import ToastNotifier
import json
import csv

standard_route_file = 'standard_route.json'
request_file = 'trip_details.json'
current_route_file = 'current_route.json'

def loadJson(jsonFile): 
    with open(jsonFile, "r") as file: 
        contents = json.load(file)
    return contents

# Prints formatted json file
def printJson(data):
    print(json.dumps(data, indent=4))

# Gets directions from google maps API
# Returns the result
# Optionally, stores the results in a json file
def directionsGet(request, results_file = ''):
    gmaps = googlemaps.Client(request['api_key'])
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

# Gets waypoints: These are the end points of each leg
def getWaypoints(directions): 
    waypoints = [step.get("end_location") for leg in directions[0]["legs"] for step in leg["steps"]]
    return waypoints

def main(): 
    # Get directions for fastest route home
    #standard_route = directionsGetStore(trip_details, standard_route_file)
    standard_route = loadJson(standard_route_file)
    request = loadJson(request_file)
    current_route = directionsGet(request)
    current_waypoints = getWaypoints(current_route)
    standard_waypoints = getWaypoints(standard_route)
    duration = current_route[0]['legs'][0]['duration_in_traffic']['value']/60

    # Generate windows notification
    toaster = ToastNotifier()
    if current_waypoints != standard_waypoints:
        toaster.show_toast("Traffic Alert", request["alternate_msg"], duration = 5)
    elif (duration > (55)):
        toaster.show_toast("Traffic Alert", f"Trip home is going to take {duration} minutes", duration = 5)
    
    # Test: Print directions and waypoints
    # printJson(current_route)
    # printJson(current_waypoints)
    # printJson(standard_waypoints)


if __name__ == '__main__':
    main()