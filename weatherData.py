# Description: A simple weather data retrieval program using the WeatherAPI.

import requests
import json

city = input("Enter the name of the city: ")

url = f"http://api.weatherapi.com/v1/current.json?key=52b92b9aec604fad99f114143252605&q={city}"

req = requests.get(url)
if req.status_code == 200:
    data = json.loads(req.text)
    print(f"City: {data['location']['name']}")
    print(f"Region: {data['location']['region']}")
    print(f"Country: {data['location']['country']}")
    print(f"Temperature: {data['current']['temp_c']}°C")
    print(f"Condition: {data['current']['condition']['text']}")
    print(f"Humidity: {data['current']['humidity']}%")
    print(f"Wind Speed: {data['current']['wind_kph']} kph")
    print(f"Last Updated: {data['current']['last_updated']}")
else:
    print("Error: Unable to retrieve weather data. Please check the city name or try again later.")
    print(f"Status Code: {req.status_code}")
    print(f"Response: {req.text}")

query = input("Do you want to full weather data of this city? (yes/no): ")
if query.lower() == "yes":
    w_data = json.loads(req.text)
    print("\nFull Weather Data:\n")
    print(json.dumps(w_data, indent=4))
else:
    print("Thank you for using the Weather Data Program.")
