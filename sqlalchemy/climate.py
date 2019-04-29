
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt


# In[3]:


import numpy as np
import pandas as pd


# In[4]:


import datetime as dt


# # Reflect Tables into SQLAlchemy ORM

# In[5]:


# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect


# In[6]:


engine = create_engine("sqlite:///Resources/hawaii.sqlite")


# In[7]:


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)


# In[8]:


Base.classes.keys()


# In[9]:


inspector = inspect(engine)
columns = inspector.get_columns('measurement')
for column in columns:
    print(column["name"], column["type"])


# In[23]:


data = engine.execute("SELECT * FROM measurement")
for record in data:
    print(record)


# In[11]:


# We can view all of the classes that automap found
Base.classes.keys()


# In[12]:


# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station


# In[13]:


# Create our session (link) from Python to the DB
session = Session(engine)


# In[14]:


first_row = session.query(Measurement).first()
first_row.__dict__


# In[15]:


first_row = session.query(Station).first()
first_row.__dict__


# # Exploratory Climate Analysis

# In[16]:


# Design a query to retrieve the last 12 months of precipitation data and plot the results
#precip = session.query(Measurement).filter(Measurement.date > '2016-08-24').all()
#precip = session.query(Measurement).all()
#print(precip)
#precip[0].__dict__                                          
# Calculate the date 1 year ago from the last data point in the database
lastdate =  engine.execute("SELECT max(date) FROM measurement")
for row in lastdate:
#    lastdat = dt.datetime.fromisoformat(row[0])
     lastdat = dt.datetime.strptime(row[0],'%Y-%m-%d')
begindat = lastdat - dt.timedelta(days = 365)
begindate = dt.datetime.strftime(begindat,'%Y-%m-%d')
#print(begindate)
# Perform a query to retrieve the data and precipitation scores
precip = session.query(Measurement.prcp, Measurement.date).filter(Measurement.date >= f"{begindate}").all()
# Save the query results as a Pandas DataFrame and set the index to the date column
precip_df = pd.DataFrame(precip,columns=['precip','date'])
precip_df.set_index(precip_df['date'], inplace=True)
# Sort the dataframe by date
precip_df= precip_df.sort_values('date')
# Use Pandas Plotting with Matplotlib to plot the data
precip_df.plot()


# ![precipitation](Images/precipitation.png)

# In[17]:


# Userecip_df.describe() Pandas to calcualte the summary statistics for the precipitation data
precip_df.describe()


# ![describe](Images/describe.png)

# In[20]:


# Design a query to show how many stations are available in this dataset?
stationdata = session.query(Station)
print('station count = ', stationdata.count())


# In[30]:


# What are the most active stations? (i.e. what stations have the most rows)?
# List the stations and the counts in descending order.
stationsql = engine.execute("SELECT station, count(station) FROM measurement group by station order by count(station) desc")
for row in stationsql:
    print(row)


# In[48]:


# Using the station id from the previous query, calculate the lowest temperature recorded, 
# highest temperature recorded, and average temperature most active station?
measave=session.query(Measurement.station,func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).filter(Measurement.station == 'USC00519281').all()
for row in measave:
    print(row)


# In[73]:


# Choose the station with the highest number of temperature observations.
# Query the last 12 months of temperature observation data for this station and plot the results as a histogram
temptobs = session.query(Measurement.tobs).filter(Measurement.date >= f"{begindate}", Measurement.station =="USC00519281").all()
# Save the query results as a Pandas DataFrame 
precip_df = pd.DataFrame(temptobs,columns=['tobs'])
precip_df.plot(kind='hist')  


# ![precipitation](Images/station-histogram.png)

# In[74]:


# This function called `calc_temps` will accept start date and end date in the format '%Y-%m-%d' 
# and return the minimum, average, and maximum temperatures for that range of dates
def calc_temps(start_date, end_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

# function usage example
print(calc_temps('2012-02-28', '2012-03-05'))


# In[75]:


# Use your previous function `calc_temps` to calculate the tmin, tavg, and tmax 
# for your trip using the previous year's data for those same dates.
print(calc_temps('2017-08-05','2017-08-16'))


# In[77]:


# Plot the results from your previous query as a bar chart. 
# Use "Trip Avg Temp" as your Title
# Use the average temperature for the y value
# Use the peak-to-peak (tmax-tmin) value as the y error bar (yerr)
temptobs = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).        filter(Measurement.date >= '2017-08-05').filter(Measurement.date <= '2017-08-16').all()
precip_df = pd.DataFrame(temptobs,columns=['min','avg','max'])
precip_df.plot(kind='bar',title="Trip Avg Temp")  


# In[83]:


# Calculate the total amount of rainfall per weather station for your trip dates using the previous year's matching dates.
# Sort this in descending order by precipitation amount and list the station, name, latitude, longitude, and elevation
session.query(Measurement.station,func.sum(Measurement.prcp),Station.latitude,Station.longitude,Station.elevation).group_by(Measurement.station).order_by(func.sum(Measurement.prcp).desc()).filter(Measurement.station==Station.station).filter(Measurement.date >= '2017-08-05').filter(Measurement.date <= '2017-08-16').all()


# ## Optional Challenge Assignment

# In[ ]:


# Create a query that will calculate the daily normals 
# (i.e. the averages for tmin, tmax, and tavg for all historic data matching a specific month and day)

def daily_normals(date):
    """Daily Normals.

    Args:
        date (str): A date string in the format '%m-%d'
        
    Returns:
        A list of tuples containing the daily normals, tmin, tavg, and tmax
    
    """
    
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    return session.query(*sel).filter(func.strftime("%m-%d", Measurement.date) == date).all()
    
daily_normals("01-01")


# In[ ]:


# calculate the daily normals for your trip
# push each tuple of calculations into a list called `normals`

# Set the start and end date of the trip

# Use the start and end date to create a range of dates

# Stip off the year and save a list of %m-%d strings

# Loop through the list of %m-%d strings and calculate the normals for each date


# In[ ]:


# Load the previous query results into a Pandas DataFrame and add the `trip_dates` range as the `date` index


# In[ ]:


# Plot the daily normals as an area plot with `stacked=False`

