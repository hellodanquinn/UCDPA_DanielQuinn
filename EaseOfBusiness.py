import pandas as pd
import numpy as np
import pycountry_convert as pc
import seaborn as sns
import matplotlib as plt

# Actions to be taken
# Install/test 'pycountry-convert'
# Install Pandas
# Install Numpy
# Install Seaborn
# Install matplotlib
# Import CSV file
# Analyse data imported
# Run 'country-convert'
# Clean up data

# TESTS
# print("pycountry_convert " + pc.__version__)
# print("Pandas Version " + pd.__version__)
# print("Numpy Version " + np.__version__)
# print("seaborn " + sns.__version__)
# print("matplotlib " + plt.__version__)
#  code to test numpy
# l = [1, 2, 3]
# l_array = np.array(l)
# print(type(l_array))

# Read data from the csv file(s)
data = pd.read_csv("Rankings_EaseOfBus.csv")
datab = pd.read_csv("alpha.csv")
# Preview each file data
print(data.head(5))
print(datab.head(5))

# drop rows that contain null values
# Pre clean
print(data.shape)
droprows = data.dropna()
# Post clean
print(data.shape, droprows.shape)
print('Here I can see that a single row has been dropped from this data set. This is <1% and will not affect my data.')

# set a numeric id for use as an index for examples.
# data['id'] = [random.randint(0,1000) for x in range(data.shape[0])]

# Show datatypes
print(data.dtypes)

data.set_index("Economy", inplace=True)
print(data.head())

datab.set_index("Economy", inplace=True)
print(datab.head())

# dropping rows in 'data' that contain null values
droprows = data.dropna()
print(data.shape, droprows.shape)

# test
# print(len(data.Economy.unique()))

# View columns data, iterating the columns in data
for col in data.columns:
    print(col)

# FUNCTION(s)
# function to convert to alpha3 country codes and continents (may use later)
# country_code = pc.country_name_to_country_alpha3("China", cn_name_format="default")
# print(country_code)
# UNUSED NUMPY REFERENCE

# Test of pycountry_convert
def country_to_continent(country_name):
    country_alpha2 = pc.country_name_to_country_alpha2(country_name)
    country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
    country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
    return country_continent_name

# Test to validate country_to_continent
country_name = 'Brazil'
print((country_name) + " is a country in " + country_to_continent(country_name))

def country_to_alpha(country_name):
    country_alpha2 = pc.country_name_to_country_alpha2(country_name)
#    country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
#    country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
    return country_alpha2

# Test to validate country_to_alpha
country_name = 'Ireland'
print((country_name) + " has Alpha2 " + country_to_alpha(country_name))

# Use a dictionary to create a column so I can add Alpha3 codes to rows in the table
# *NOTE I feel it would be better to use a dataset and have since added a 2nd CSV for this operation

# alphaTEST = {'Austria': 'AUT', 'Italy': 'ITA','Belgium': 'BEL', 'Latvia': 'LVA', 'Bulgaria': 'BGR', 'Lithuania': 'LTU',
#        'Croatia': 'HRV', 'Luxembourg': 'LUX', 'Cyprus': 'CYP', 'Malta': 'MLT', 'Czech Republic': 'CZE',
#        'Netherlands': 'NLD', 'Denmark': 'DNK', 'Poland': 'POL', 'Estonia': 'EST', 'Portugal': 'PRT', 'Finland': 'FIN',
#        'Romania': 'ROU', 'France': 'FRA', 'Slovak Republic': 'SVK', 'Germany': 'DEU', 'Spain': 'ESP', 'Hungary': 'HUN',
#        'Sweden': 'SWE', 'Ireland': 'IRL', 'Greece': 'GRC', 'Brazil': 'BRA', 'Mexico': 'MEX', 'Argentina': 'ARG', 'Colombia': 'COL',
#        'Argentina': 'ARG', 'Peru': 'PER', 'Venezuela, RB': 'VEN', 'Chile': 'CHL', 'Guatemala': 'GTM',
#        'Ecuador': 'ECU', 'Bolivia': 'BOL', 'Haiti': 'HTI', 'Dominican Republic': 'DOM', 'Honduras': 'HND',
#        'Paraguay': 'PRY', 'El Salvador': 'SLV', 'Nicaragua': 'NIC', 'Costa Rica': 'CRI', 'Puerto Rico': 'PRI',
#        'Panama': 'PAN'}
# print(alphaTEST['Austria'])       # Test an entry from the dictionary
# print('France' in alphaTEST)     # Verify dictionary has a given key
# alphaTEST['Uruguay'] = 'URY'     # Set a new entry
# print(alphaTEST['Uruguay'])      # Test this
# DEN = (data.loc['Denmark'])
# print(DEN)

# Create group for EUROPEAN COUNTRIES
dataEU = data.loc[['Austria','Italy','Belgium','Latvia','Bulgaria','Lithuania','Croatia','Luxembourg',
          'Cyprus','Malta','Czech Republic','Netherlands','Denmark','Poland','Estonia','Portugal',
          'Finland','Romania','France','Slovak Republic','Germany','Slovenia','Greece','Spain',
          'Hungary','Sweden','Ireland']]
print(dataEU)

# Set index
dataEU.set_index("Economy", inplace=True)
dataEU.head()

# Check for missing values on dataEU
missing_values_count = dataEU.isnull()
print(missing_values_count)


# Create group for LATIN AMERICAN COUNTRIES
dataSA = data.loc[['Brazil','Mexico','Colombia','Argentina','Peru','Venezuela, RB','Chile','Guatemala','Ecuador',
          'Bolivia','Haiti','Dominican Republic','Honduras','Paraguay','El Salvador','Nicaragua','Costa Rica',
         'Puerto Rico', 'Panama', 'Uruguay']]
print(dataSA)

# Set index
# dataSA.set_index("Economy", inplace=True)
dataSA.head()

# Check for missing values on dataSA
missing_values_count2 = dataSA.isnull()
print(missing_values_count2)

# Merge EU ans SA
EUSA=pd.merge(data,
                datab[['Alpha3']],
                on='Economy')
EUSA
EUSA.head(5)



