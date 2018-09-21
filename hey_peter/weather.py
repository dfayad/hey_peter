import pyowm

owm = pyowm.OWM('95a141370f399bb06abaa704d3c26a29')  # You MUST provide a valid API key

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Search for current weather in London (Great Britain)
observation = owm.weather_at_place('London,GB')
w = observation.get_weather()
print(w.get_temperature('celsius'))  
