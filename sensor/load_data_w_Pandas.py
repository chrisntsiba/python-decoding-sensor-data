import os
import glob
import csv
import pandas as pd
import re

#def load_sensor_data():
    
sensor_data = []

### glod(): returns a list of paths matching a pathname pattern. ###

# sensor_files = glob.glob(os.path.join(os.getcwd(), "datasets", "*1.csv"))
remote_file = "https://raw.githubusercontent.com/chrisntsiba/python-decoding-sensor-data/master/datasets/SENSOR_ROOM1.csv"

csv_file_0 = pd.read_csv(remote_file, nrows=5, skiprows=None)

### 'skipfooter' not supported with 'nrows' ###
csv_file_1 = pd.read_csv(remote_file, skiprows=None, skipfooter=1, engine="python")
csv_file_2 = pd.read_csv(remote_file, skiprows=1, skipfooter=1, engine="python")
csv_file_3 = pd.read_csv(remote_file, skiprows=None, skipfooter=1, header=None, engine="python")

### No header, skip first line and footer ###
csv_file_4 = pd.read_csv(remote_file, skiprows=1, skipfooter=1, header=None, engine="python")

### Skips odd/even rows ### 
csv_file_5 = pd.read_csv(remote_file, skiprows=lambda x: x %2 != 0, skipfooter=1, header=None, engine="python")

### Specify headers ###
cols_indices = [0,3,4]
csv_file_6 = pd.read_csv(remote_file, skipfooter=1, usecols=cols_indices, engine="python")

cols_indices = [0,1,3,4]
cols_names = ["id", "datetime", "temp","humid"] # aliases
csv_file_7 = pd.read_csv(remote_file, header=None, skiprows=1, usecols=cols_indices, names=cols_names, engine="python")

csv_file_8 = pd.read_csv(remote_file, skipfooter=1, engine="python")
#print(csv_file_8[["id","energy_usage","particulate"]])

### Defining types ###
# print(csv_file_8.dtypes)
types = {
            "date":"datetime64", 
            "time":"string",
            "temperature":"float64"
        }
csv_file_9 = pd.read_csv(remote_file, skipfooter=1, engine="python", dtype=types)
#print(csv_file_9.dtypes)

### NOT WORKING YET ### use [converters] tag to apply functions on columns ###
type = {"date":"string"}
converter = {"date": lambda x: re.findall("/[0-9]/",x)}
csv_file_a = pd.read_csv(remote_file, usecols=[0,1,2], dtype=type, engine="python")
#csv_file_a = pd.read_csv(remote_file, usecols=[0,1,2], dtype=type, converters={"date": lambda x: re.findall("[0-9]",x)}, engine="python")
#csv_file_b = pd.read_csv(csv_file_a, converters = converter)
#print (csv_file_b.dtypes)

### Parse date ###
csv_file_c = pd.read_csv(remote_file, engine="python", parse_dates=["date"])
print (csv_file_c.dtypes)

### Missing values ###
# use na_filter=True to remove NaN markers
# use na_values for other markers
# use keep_default_na to include default values


