import pprint
import requests
from matplotlib import pyplot as plt
from datetime import datetime

pp = pprint.PrettyPrinter(indent=4)

API_URL = 'https://goweather.herokuapp.com/weather/'
city = 'long_beach'
r = requests.get(API_URL + city)
response = r.json()
pp.pprint(response)

forecast_list = response['forecast']
today = datetime.now().strftime("%b-%d-%Y")

to_graph = {} # empty dict to store shaped data
count = 1 # global iterator to track each day past current datetime

for day in forecast_list:
    current_date = int(today[4:6]) + count
    this_day = f"{today[0:4]}{current_date}{today[6:]}"
    count += 1

    to_graph[this_day] = day['wind']

print(to_graph)

# axis labels
plt.xlabel('Date')
plt.ylabel('Wind Speed km/h')

print('to_graph keys: ', to_graph.keys())
print('to_graph values: ', to_graph.values())

plt.scatter(to_graph.keys(), to_graph.values()) # sets up graph
plt.show() # paints graph to the screen

'''
bonus:
Currently, if we were to start a search on one of the last 2 days of the month, our dates will look screwy, potentially going beyond the confines of agreed-upon datetime. How could you resolve the edge-cases that could cause these errors?

Try adapting our script to display a bar graph of the temperatures of the next three days.

Sometimes the API returns unclean data, looking like: ' km / h' for the wind speed on any given day. Adapt your code to handle this event. Assume if wind speed is not posted, the wind speed will be 0.
'''