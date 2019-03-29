
# coding: utf-8

# # WeatherPy
# ----
# 
# ### Analysis
# * As expected, the weather becomes significantly warmer as one approaches the equator (0 Deg. Latitude). More interestingly, however, is the fact that the southern hemisphere tends to be warmer this time of year than the northern hemisphere. This may be due to the tilt of the earth.
# * There is no strong relationship between latitude and cloudiness. However, it is interesting to see that a strong band of cities sits at 0, 80, and 100% cloudiness.
# * There is no strong relationship between latitude and wind speed. However, in northern hemispheres there is a flurry of cities with over 20 mph of wind.
# 
# ---
# 
# #### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[8]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
import json

# Import API key
#import api_keys
api_key = "8db29999ac3499d446d06c81869bad2f"


# Incorporated citipy to determine city based on latitude and longitude
from citipy import citipy

# Output File (CSV)
output_data_file = "output_data/cities.csv"

# Range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)


# ## Generate Cities List

# In[9]:


# List for holding lat_lngs and cities
lat_lngs = []
cities = []

# Create a set of random lat and lng combinations
lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
    
    # If the city is unique, then add it to a our cities list
    if city not in cities:
        cities.append(city)

# Print the city count to confirm sufficient count
len(cities)


# ### Perform API Calls
# * Perform a weather check on each city using a series of successive API calls.
# * Include a print log of each city as it'sbeing processed (with the city number and city name).
# 

# In[12]:


base_url = 'http://api.openweathermap.org/data/2.5/weather'
api_list = []
for city in cities:
    print(f'processing {city}')
    query_ext = f'?q={city}&appid={api_key}'
    target_url = base_url + query_ext
    #print(target_url)
    responsenj = requests.get(target_url)
    response = responsenj.json()
    if responsenj.status_code == 200:
        api_dict ={
        'City':response['name'],
        "Cloudiness":response['clouds']['all'],
        'Country':response['sys']['country'],
        'Date':response['dt'],
        'Humid':response['main']['humidity'],
        'Lat':response['coord']['lat'],
        'Lng':response['coord']['lon'],
        'Max Temp':response['main']['temp_max'],
        'Wind Speed':response['wind']['speed']
        }
        api_list.append(api_dict)
    else:
        print('city not found -- skipping')


# In[3]:





# ### Convert Raw Data to DataFrame
# * Export the city data into a .csv.
# * Display the DataFrame

# In[13]:


api_df = pd.DataFrame(api_list)
api_df.head()


# In[4]:





# In[14]:


api_file = '../../../SaveWeather.csv'
api_df.to_csv(api_file,index=False)


# In[5]:





# ### Plotting the Data
# * Use proper labeling of the plots using plot titles (including date of analysis) and axes labels.
# * Save the plotted figures as .pngs.

# #### Latitude vs. Temperature Plot

# In[21]:


api_lattemp = api_df.drop(['City','Cloudiness','Country','Date','Humid','Lng','Wind Speed'],axis=1)
#api_lattemp.head()
api_lattemp.plot(x='Lat',y='Max Temp',kind='scatter',title='City Latitude vs Max Temperature(03/28/19)',grid=True)


# In[6]:





# #### Latitude vs. Humidity Plot

# In[7]:





# #### Latitude vs. Cloudiness Plot

# In[24]:


api_df.plot(x='Lat',y='Cloudiness',kind='Scatter',title='City Latitude vs Cloudiness(03/28/19)',grid=True)


# In[8]:





# #### Latitude vs. Wind Speed Plot

# In[9]:




