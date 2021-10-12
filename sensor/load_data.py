##
# The dataset for this project is stored in several CSV files found in the >DATASETS folder. 
# It represents the data from a device with multiple sensors. The data was collected at random times over a period of days. 
# The records include measurements of temperature, humidity, energy consumption, and particle count in the air over a given area. 
# The data is collected over a period of 24 hours.
#
# To start, open the file called load_data.py in the >SENSOR folder.
# At the top of the file, create three import statements for os, glob, and csv. These libraries will allow us to work with a collection of files.
##
import os
import glob
import csv

# Create a function called load_sensor_data() that has no parameters. 
# In the body of the load_sensor_data() function, create a variable called sensor_data and set it to an empty list.
def load_sensor_data():
    
    sensor_data = []

    # glod(): returns a list of paths matching a pathname pattern.
    sensor_files = glob.glob(os.path.join(os.getcwd(), "datasets", "*.csv"))

    for sensor_file in sensor_files:
        with open(sensor_file, mode="r") as data_file:
           # Will contain a list of dictionaries with the sensor data
           data_reader = csv.DictReader(data_file, delimiter=',') 
           for row in data_reader:
               sensor_data.append(row)

    return sensor_data




