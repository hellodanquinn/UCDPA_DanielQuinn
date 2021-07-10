import pandas as pd
import numpy as np
import pycountry_convert as pc
# Install 'country-convert'
# Install Pandas
# Install Numpy
# Import CSV file
# Analyse data imported
# Run 'country-convert'
# Clean up data

print("pycountry_convert " + pc.__version__)

print("Pandas Version " + pd.__version__)

print("Numpy Version " + np.__version__)
# Run code to test numpy
# l = [1, 2, 3]
# l_array = np.array(l)
# print(type(l_array))

# Run some initial code to test environment
# hdg = "128"
# print(hdg + " Success")

# Read data from the csv file
data = pd.read_csv("Rankings_EaseOf.csv")

# Preview data from the first 5 lines
print(data.head())

# function to convert to alpha3 country codes and continents
# country_code = pc.country_name_to_country_alpha3("China", cn_name_format="default")
# print(country_code)


def country_to_continent(country_name):
    country_alpha2 = pc.country_name_to_country_alpha2(country_name)
    country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
    country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
    return country_continent_name

# Iterate through this on col2?
# Example
country_name = 'Germany'
print((country_name) + " is a country in " + country_to_continent(country_name))


