import googlemaps
from datetime import datetime
from win10toast import ToastNotifier
import json
import csv

standard_route_file = 'standard_route.json'
request_file = 'trip_details.json'
current_route_file = 'current_route.json'

def getAPIKey(file):
    with open(file, "r") as f: 
        API_KEY = f.read()
    return API_KEY

# toaster = ToastNotifier()
# toaster.show_toast("Commute", "A really good message", duration = 5)

def loadJson(jsonFile): 
    with open(jsonFile, "r") as file: 
        contents = json.load(file)
    return contents

def directionsGet(request_file, results_file = ''): 
    gmaps = googlemaps.Client(request['api_key'])
    # Parameters to be passed to API
    directions_result = gmaps.directions(trip['origin'],
                                         trip['destination'],
                                         mode=trip['mode'],
                                         departure_time=datetime.now(), 
                                         avoid = trip['avoid']
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

# #print(formatted_results)
# distance = (directions_result[0]['legs'][0]['duration_in_traffic']['text'])
# print("Duration in traffic: ", distance)

#print(directions_result)

#Print formatted json data
def printJson(data):
    print(json.dumps(data, indent=4))

def main(): 
    #standard_route = directionsGetStore(trip_details, standard_route_file)
    
    standard_route = loadJson(standard_route_file)
    request = loadJson(request_file)
    current_route = directionsGet(trip_details)
    printJson(current_route)
    current_waypoints = getWaypoints(current_route)
    standard_waypoints = getWaypoints(standard_route)
    printJson(current_waypoints)

    if current_waypoints == standard_waypoints: 
        print("Take standard route home")
    else: 
        print("Go home another way")

    #getDirections(trip_details, current_route)
    #if compareRoute(standard_route, current_route): 
        #print("They're the same!!!!")
    #else:
        #print("They're not the same!!!!")


main()