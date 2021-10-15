import os
import glob
import csv
import pandas as pd
import re

import xml.etree.ElementTree as xml



#def load_sensor_data():
    
xml_data = []

### glod(): returns a list of paths matching a pathname pattern. ###

xml_files = glob.glob(os.path.join(os.getcwd(), "sensor", "*.xml"))
xml_file = xml_files[0]
#remote_file = "https://raw.githubusercontent.com/chrisntsiba/python-decoding-sensor-data/master/sensor/users-100.xml"

xml_file_0 = xml.parse(xml_file)
users_root = xml_file_0.getroot()

print("\nPrinting root:")
print(users_root)
print(users_root.tag)
print(len(users_root))

print("\nPrinting root child elements:")
print(users_root[0])
print(users_root[0].tag)
print(users_root[0].attrib)
print("\n")


