import os
import glob
import csv
import pandas as pd
import re

import xml.etree.ElementTree as xml



#def load_sensor_data():
    
sensor_data = []

### glod(): returns a list of paths matching a pathname pattern. ###

# sensor_files = glob.glob(os.path.join(os.getcwd(), "datasets", "*1.csv"))
remote_file = "https://raw.githubusercontent.com/chrisntsiba/python-decoding-sensor-data/master/datasets/SENSOR_ROOM1.csv"

csv_file_0 = pd.read_csv(remote_file, nrows=5, skiprows=None)

