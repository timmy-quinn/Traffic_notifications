import googlemaps
from datetime import datetime
from win10toast import ToastNotifier
import json

def getAPIKey():
    api_key_file = open("api_key.txt", "r")
    API_KEY = api_key_file.read()
    api_key_file.close()
    return API_KEY

gmaps = googlemaps.Client(getAPIKey())

# toaster = ToastNotifier()


# toaster.show_toast("Commute", "A really good message", duration = 5)


# Parameters to be passed to API
origin = "156 Hillside St. Boston, MA"
destination = "289 Great Rd. Acton, MA"
waypoints = ["Route 9"]
avoid = ["tolls"]

directions_result = gmaps.directions("1578 Tremont St. Boston, MA`",
                                     "289 Great Rd. Acton, MA",
                                     mode="driving",
                                     departure_time=datetime.now(), 
                                     avoid = "tolls"
                                     )

formatted_results  = json.dumps(directions_result, indent = 4)
with open("standard_route.json", "w") as f:
    json.dump(directions_result, f)

with open("standard_route.json", "r") as f:
    route1 = json.load(f)

with open("route2.json", "r") as f:
    standard_route = json.load(f)


waypoints_route1 = [step.get("end_location") for leg in route1[0]["legs"] for step in leg["steps"]]
waypoints_route2 = [step.get("end_location") for leg in route2[0]["legs"] for step in leg["steps"]]

if waypoints_route1 == waypoints_route2:
    print("They're the same!!")
else: 
    print("They're different :(")


#print(formatted_results)
distance = (directions_result[0]['legs'][0]['duration_in_traffic']['text'])
print("Duration in traffic: ", distance)

#print(directions_result)