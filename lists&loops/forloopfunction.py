def celsius_to_kelvin(cels):
    return cels + 273.15

# print(celsius_to_kelvin)

todays_temperatures = [12, 13 , 14, 15]

for temperature in todays_temperatures:
    print(celsius_to_kelvin(temperature))