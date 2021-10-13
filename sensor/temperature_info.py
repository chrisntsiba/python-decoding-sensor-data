from datetime import date, datetime
from house_info import HouseInfo

class TemperatureData (HouseInfo):

    def _convert_data(self, data):
        recs = []
        # The data parameter is a list of strings. 
        # These strings are integers, base 10, which are temperatures.
        for rec in data:
            rec = int(rec, 10)
            recs.append(rec)
    
    # rec_area parameter should have a default value of 0, which translates to all records. 
    # The purpose of this method is to filter the temperature data by the "area" field. 
    # In this method rec_area maps to the "area" data column.
    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area("temperature", rec_area)
        return self._convert_data(recs)

    # The purpose of this method is to filter the temperature data by the "date" field. 
    # In this method, rec_date maps to the "date" data column.
    def get_data_by_date(self, rec_date=date.today()):
        recs = super().get_data_by_date("temperature", rec_date)
        return self._convert_data(recs)
