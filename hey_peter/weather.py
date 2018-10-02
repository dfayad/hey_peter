#coding: utf-8
import pyowm
import datetime


def get_weather():
    owm = pyowm.OWM('95a141370f399bb06abaa704d3c26a29')  # You MUST provide a valid API key

    # Have a pro subscription? Then use:
    # owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

    # Search for current weather in London (Great Britain)
    location = 'Poughkeepsie,US'
    observation = owm.weather_at_place(location)
    w = observation.get_weather()
    status = w.get_status()
    currTemp = int(w.get_temperature('celsius')['temp'])
    print('Heres the weather:')
    #print("The current temperature in " + str(location) + " is " + str(currTemp) + "ºC and the status is " + str(status))
    observation_list = owm.weather_around_coords(-22.57, -43.12)
    #print(observation_list)

    output = "The current temperature in " + str(location) + " is " + str(currTemp) + "ºC and the status is " + str(status)

    return output