from weather import Weather, Unit

#woeid = 12762398
weather = Weather(unit=Unit.CELSIUS)

lookup = weather.lookup(12762398)
condition = lookup.condition

print(condition.text)