import requests
import sys
#import os
from datetime import datetime

api_key = '92c868c564b5bdaeb180b9343497adb0'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

with open('output.txt','w')as f:
    print("-------------------------------------------------------------\n",file=f)
    print("Weather Stats for - {}  || {}\n".format(location.upper(), date_time),file=f)
    print("-------------------------------------------------------------\n",file=f)

    print("Current temperature is: {:.2f} deg C".format(temp_city),file=f)
    print("Current weather desc  :", weather_desc,file=f)
    print("Current Humidity      :", hmdt, '%',file=f)
    print("Current wind speed    :", wind_spd, 'kmph',file=f)