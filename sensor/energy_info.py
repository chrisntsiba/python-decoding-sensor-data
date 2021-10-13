from house_info import HouseInfo

from datetime import date, datetime

class EnergyData(HouseInfo):

    ENERGY_PER_BULB = .2
    ENERGY_BITS = 0x0F0

    # This method will help us extract the energy data information 
    # from energy_usage data field.

    #The rec parameter is a string. 
    # This string represents the energy_usage in hexadecimal notation form.

    # The energy_usage field comes as a three-digit hexadecimal (hex) number (12 bits), for example "0xfef". 
    # However, only the middle hex number (bits: 4-7 with index notation) represents the energy usage. 
    # In order to extract these bits, we will use bitwise operations
    def _get_energy(self, rec):
        energy = int(rec, base=16) # produces an integer to which can be applied bitwise operations.

        # Isolate the energy bits by "anding" the energy integer with the ENERGY_BITS constant. 
        # This operation should clear all the bits from the first and third nibble.
        energy = energy & self.ENERGY_BITS
        energy = energy >> 4
        return energy

    def _convert_data(self, data):
        recs = []
        for rec in data:
            recs.append(self._get_energy(rec))
        return recs

    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area("energy_usage", rec_area)
        return self._convert_data(recs)

    def get_data_by_date(self, rec_date=date.today()):
        recs = super().get_data_by_date("energy_usage", rec_date)
        return self._convert_data(recs)

    # The purpose of this method is to take a list of energy usage values, 
    # calculate the cost per light bulb usage, 
    # and return the sum of all the values in the data list.
    def calculate_energy_usage(self, data):
        # On a new line in the method, define a variable called total_energy, 
        # which will store the sum of all converted values in the data list. 
        # To achieve this, call the sum built in function. 
        # This function should take a list comprehension as its only argument. 
        # The list comprehension should use field as the expression variable. 
        # The field variable should be multiplied by the ENERGY_PER_BULB constant.
        total_energy = sum([field * self.ENERGY_PER_BULB for field in data])
        
        return total_energy




