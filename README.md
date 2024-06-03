# Traffic Alert System
Description
This Python script uses the Google Maps API to get directions and monitor traffic conditions for a specified route. It compares the current route's waypoints with a standard route's waypoints to determine if there are any deviations due to traffic. If there are deviations or if the trip duration exceeds a certain threshold, it displays a desktop notification using win10toast.

## Prerequisites
- Python 3.x
- Google Maps API key
- googlemaps Python library
- win10toast Python library
## Installation
1. Install the required Python libraries:  
   ```bash  
    pip install googlemaps win10toast  
    ```
   
3. Ensure you have your Google Maps API key saved in a text file.  

## Files
standard_route.json: Contains the standard route information in JSON format.  
request_file.json: Contains the request details for the trip.  
trip_details.json: (Optional) File to save the current route details if needed.  
## JSON File Structure  
standard_route.json and current_route.json  
These files should follow the structure provided by the Google Maps Directions API response.  

### `trip_details.json`  
```
{  
    "api_key": "YOUR_API_KEY_HERE",  
    "origin": "Starting address or coordinates",  
    "destination": "Destination address or coordinates",  
    "mode": "driving", // or "walking", "bicycling", "transit"  
    "avoid": ["tolls", "ferries", "highways"], // optional  
    "alternate_msg": "Alternate route detected due to traffic.",  
    "standard_msg": "Your route is clear."  
} 
```
