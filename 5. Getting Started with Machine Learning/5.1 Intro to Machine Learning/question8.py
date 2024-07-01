import math

# Unknown new data point that needs to be labeled for rain or no rain
new_data_rain = int(input())
new_data_humidity = int(input())

# Training Data Examples for rain and no_rain
rain_temp, rain_humidity = [45,55,55], [60,65,55]
no_rain_temp, no_rain_humidity = [35,50,40], [45,30,35]

# Euclidean distance based approach to label the unknown new data point
rain = 0
no_rain = 0
sz = len(rain_temp)

for i in range(sz):
    rain += math.sqrt((rain_temp[i] - new_data_rain)**2 + (rain_humidity[i] - new_data_humidity)**2)
    no_rain += math.sqrt((no_rain_temp[i] - new_data_rain)**2 + (no_rain_humidity[i] - new_data_humidity)**2)

# Print the label of unknown new data point based on the total distance to each group
if rain < no_rain: 
    print("RAIN")
else:
    print("NO RAIN")