import pandas as pd
import numpy as np
import pycountry_convert as pc
# Actions to be taken
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
datab = pd.read_csv("alpha.csv")
# Preview data from the first 5 lines
print(data.head())

data.set_index("Economy", inplace=True)
print(data.head())
#Show datatypes
print(data.dtypes)

#temp
#print(len(data.Economy.unique()))

# iterating the columns
for col in data.columns:
    print(col)


# function to convert to alpha3 country codes and continents (may use later)
# country_code = pc.country_name_to_country_alpha3("China", cn_name_format="default")
# print(country_code)

def country_to_continent(country_name):
    country_alpha2 = pc.country_name_to_country_alpha2(country_name)
    country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
    country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
    return country_continent_name

# Test to validate
country_name = 'Brazil'
print((country_name) + " is a country in " + country_to_continent(country_name))

def country_to_alpha(country_name):
    country_alpha2 = pc.country_name_to_country_alpha2(country_name)
    country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
    country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
    return country_alpha2

# Test to validate
country_name = 'Ireland'
print((country_name) + " has Alpha2 " + country_to_alpha(country_name))

# Use a dictionary to create a column so I can add Alpha3 codes to rows in the table
# *NOTE I feel it would be better to use a dataset and have since added a 2nd CSV for this operation

alpha = {'Austria': 'AUT', 'Italy': 'ITA','Belgium': 'BEL', 'Latvia': 'LVA', 'Bulgaria': 'BGR', 'Lithuania': 'LTU',
        'Croatia': 'HRV', 'Luxembourg': 'LUX', 'Cyprus': 'CYP', 'Malta': 'MLT', 'Czech Republic': 'CZE',
        'Netherlands': 'NLD', 'Denmark': 'DNK', 'Poland': 'POL', 'Estonia': 'EST', 'Portugal': 'PRT', 'Finland': 'FIN',
        'Romania': 'ROU', 'France': 'FRA', 'Slovak Republic': 'SVK', 'Germany': 'DEU', 'Spain': 'ESP', 'Hungary': 'HUN',
        'Sweden': 'SWE', 'Ireland': 'IRL', 'Greece': 'GRC', 'Brazil': 'BRA', 'Mexico': 'MEX', 'Colombia': 'COL',
        'Argentina': 'ARG', 'Peru': 'PER', 'Venezuela, RB': 'VEN', 'Chile': 'CHL', 'Guatemala': 'GTM',
        'Ecuador': 'ECU', 'Bolivia': 'BOL', 'Haiti': 'HTI', 'Dominican Republic': 'DOM', 'Honduras': 'HND',
        'Paraguay': 'PRY', 'El Salvador': 'SLV', 'Nicaragua': 'NIC', 'Costa Rica': 'CRI', 'Puerto Rico': 'PRI',
        'Panama': 'PAN'}
print(alpha['Austria'])       # Test an entry from the dictionary
print('France' in alpha)     # Verify dictionary has a given key
alpha['Uruguay'] = 'URY'     # Set a new entry d['fish'] = 'wet'
print(alpha['Uruguay'])      # Test this

# drop rows that contain null values
droprows = data.dropna()
print(data.shape, droprows.shape)
print('Here I can see that a single row has been dropped from this data set. This is less <1% and will not affect my data.')