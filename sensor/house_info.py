from datetime import datetime, date 
from time import strftime

class HouseInfo:
    def __init__(self, data):
       self.data = data 

    # The rec_area parameter should have a default value of 0, which translates to all records. 
    # The purpose of this method is to filter the data using rec_area as the key, and field as the value.
    def get_data_by_area(self, field, rec_area=0):
        field_data = []
        # The self.data class variable is a list of dictionaries. 
        # The dictionary keys are equal to the columns names in the data files. 
        # e.g. when the field input parameter is set to "id" then, the record[field] value corresponds to the "id" column values. 
        # In this method, the rec_area variable maps to 'area' column values.
        for record in self.data:
            if rec_area == 0:
                field_data.append(record[field])
            elif(rec_area==int(record["area"])):
                field_data.append(record[field])

        return field_data

    # In this method, the rec_date input parameter maps to the 'date' column's values.
    def get_data_by_date(self, field, rec_date=date.today()):
        field_data = []

        for record in self.data:
            if rec_date.strftime("%m/%d/%y") == record["date"]:
                field_data.append(record[field])

        return field_data