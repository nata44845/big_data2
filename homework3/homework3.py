from datetime import datetime
from meteostat import Point, Daily

# Set time period
start = datetime(2023, 1, 1)
end = datetime(2023, 12, 31)

# Create Points lat, lon, alt
points = {
    'krasnoyarsk': Point(56.0184, 92.8672, 139),
    'moskow': Point(55.7522, 37.6156, 143),
    'vladivostok': Point(43.1056, 131.874, 30)
}
# Get daily data for 2023
i = 0
for key, value in points.items():
    data = Daily(value, start, end)
    data = data.fetch()
    data["city"] = key
    if i==0: 
        data.to_csv('temperatures.csv')
        i = 1
    else:
        data.to_csv('temperatures.csv', mode = 'a', header = False)