import pandas as pd
import numpy as np
import pycountry_convert as pc
import matplotlib.pyplot as plt
# import seaborn as sns


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
# code to test numpy
# C = [Eur, SAmerica, NAmerica]
# l_array = np.array(C)
# print(type(C_array))

# Read data from the csv file(s)
data = pd.read_csv("Rankings_EaseOfBus.csv")
datab = pd.read_csv("alpha.csv")
# Preview each file data
print(data.head(5))
print(datab.head(5))

# Numpy arrays to group countries *NOT USED LATER*
Eur = np.array(['Austria', 'Italy', 'Belgium', 'Latvia', 'Bulgaria', 'Lithuania', 'Croatia', 'Luxembourg',
          'Cyprus', 'Malta', 'Czech Republic', 'Netherlands', 'Denmark', 'Poland', 'Estonia', 'Portugal',
          'Finland', 'Romania', 'France', 'Slovak Republic', 'Germany', 'Slovenia', 'Greece', 'Spain',
          'Hungary', 'Sweden', 'Ireland'])
print(Eur[-1] + " - is also known as EIRE" )

Latam = np.array(['Brazil', 'Mexico', 'Colombia', 'Argentina', 'Peru', 'Venezuela, RB', 'Chile', 'Guatemala', 'Ecuador',
          'Bolivia', 'Haiti', 'Dominican Republic', 'Honduras', 'Paraguay', 'El Salvador', 'Nicaragua', 'Costa Rica',
         'Puerto Rico', 'Panama', 'Uruguay'])
print(Latam[2] + " - is also known as the GATEWAY TO SOUTH AMERICA")

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

# FUNCTION(s) DEMO
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
    return country_alpha2

# Test to validate country_to_alpha
country_name = 'Ireland'
print((country_name) + " has Alpha2 " + country_to_alpha(country_name))

# Use a dictionary to create a column so I can add Alpha3 codes to rows in the table
# *NOTE I feel it would be better to use a dataset and have since added a 2nd CSV for this operation

alphaTEST = {'Austria': 'AUT', 'Italy': 'ITA','Belgium': 'BEL', 'Latvia': 'LVA', 'Bulgaria': 'BGR', 'Lithuania': 'LTU',
        'Croatia': 'HRV', 'Luxembourg': 'LUX', 'Cyprus': 'CYP', 'Malta': 'MLT', 'Czech Republic': 'CZE',
        'Netherlands': 'NLD', 'Denmark': 'DNK', 'Poland': 'POL', 'Estonia': 'EST', 'Portugal': 'PRT', 'Finland': 'FIN',
        'Romania': 'ROU', 'France': 'FRA', 'Slovak Republic': 'SVK', 'Germany': 'DEU', 'Spain': 'ESP', 'Hungary': 'HUN',
        'Sweden': 'SWE', 'Ireland': 'IRL', 'Greece': 'GRC', 'Brazil': 'BRA', 'Mexico': 'MEX', 'Colombia': 'COL',
        'Argentina': 'ARG', 'Peru': 'PER', 'Venezuela, RB': 'VEN', 'Chile': 'CHL', 'Guatemala': 'GTM',
        'Ecuador': 'ECU', 'Bolivia': 'BOL', 'Haiti': 'HTI', 'Dominican Republic': 'DOM', 'Honduras': 'HND',
        'Paraguay': 'PRY', 'El Salvador': 'SLV', 'Nicaragua': 'NIC', 'Costa Rica': 'CRI', 'Puerto Rico': 'PRI',
        'Panama': 'PAN'}
print(alphaTEST['Austria'])      # Test an entry from the dictionary
print('France' in alphaTEST)     # Verify dictionary has a given key
alphaTEST['Uruguay'] = 'URY'     # Set a new entry by adding another country
print(alphaTEST['Uruguay'])      # Test this
DEN = (data.loc['Denmark'])      # Show data for Denmark
print(DEN)

# Create group for EUROPEAN COUNTRIES
dataEU = data.loc[['Austria','Italy','Belgium','Latvia','Bulgaria','Lithuania','Croatia','Luxembourg',
          'Cyprus','Malta','Czech Republic','Netherlands','Denmark','Poland','Estonia','Portugal',
          'Finland','Romania','France','Slovak Republic','Germany','Slovenia','Greece','Spain',
          'Hungary','Sweden','Ireland']]
print(dataEU)

# Check for missing values on dataEU
missing_values_count = dataEU.isnull()
print(missing_values_count)


# Create group for LATIN AMERICAN COUNTRIES
dataSA = data.loc[['Brazil','Mexico','Colombia','Argentina','Peru','Venezuela, RB','Chile','Guatemala','Ecuador',
          'Bolivia','Haiti','Dominican Republic','Honduras','Paraguay','El Salvador','Nicaragua','Costa Rica',
         'Puerto Rico','Panama','Uruguay']]
print(dataSA)

# Check for missing values on dataSA
missing_values_count2 = dataSA.isnull()
print(missing_values_count2)

# Merge on Alpha3 / Economy dataEU
dataEU=pd.merge(dataEU,
                datab[['Alpha3']],
                on='Economy')
print(dataEU)

dataEU.set_index("Alpha3", inplace=True)
print(dataEU.head())

# Merge on Alpha3 / Economy dataSA

dataSA=pd.merge(dataSA,
                datab[['Alpha3']],
                on='Economy')
print(dataSA)

dataSA.set_index("Alpha3", inplace=True)
print(dataSA.head())

# This data uses dataEU and removes HIGHER than 70
visEU = dataEU[~(dataEU['globalRank'] >= 50)]
print(visEU)

# This data uses South America (LATAM REGION) and removes HIGHER than 100
visSA = dataSA[~(dataSA['globalRank'] >= 100)]
print(visSA)

### DATA Visualisation ###

# EUROPE #
plt.plot(visEU['globalRank'], marker = "s", linestyle = ":", color = "darkorange")
plt.plot(figsize=(20, 12))
plt.title("EUROPE - Countries with Ranking up to 50")
plt.xlabel("COUNTRY")
plt.ylabel("RANKING")
plt.show()

# SOUTH AMERICA (LATAM) #
plt.plot(visSA['globalRank'], marker = "s", linestyle = ":", color = "darkorange")
plt.plot(figsize=(20, 12))
plt.title("South America (LATAM) - Countries with Ranking up to 100")
plt.xlabel("COUNTRY")
plt.ylabel("RANKING")
plt.show()

## Trading across Borders ##
# EUROPE #
plt.plot(visEU['Trading across borders'], marker = "s", linestyle = ":", color = "darkorange")
plt.plot(figsize=(20, 12))
plt.title("EUROPE - Trading Across Borders (Ranking up to 50)")
plt.xlabel("COUNTRY")
plt.ylabel("RANKING")
plt.show()

# SOUTH AMERICA (LATAM) #
plt.plot(visSA['Trading across borders'], marker = "s", linestyle = ":", color = "darkorange")
plt.plot(figsize=(20, 12))
plt.title("South America (LATAM) - Trading Across Borders (Ranking up to 100)")
plt.xlabel("COUNTRY")
plt.ylabel("RANKING")
plt.show()


## Bar Chart

# creating the dataset for Europe
dataEUR = {'DNK': 4, 'SWE': 10, 'LTV': 11,
        'LVA': 19, 'FIN': 20}
countries = list(dataEUR.keys())
values = list(dataEUR.values())

fig = plt.figure(figsize=(8, 5))

# bar plot - Top 5 countries EU
plt.bar(countries, values, color='blue', edgecolor= 'black',
        width=0.6)

plt.xlabel("Country")
plt.ylabel("Ranking")
plt.title("Top 5 countries in Europe (Ease of Business)")
plt.show()

# creating the dataset for LATAM (South America)
dataLAT = {'Chile CHL': 59, 'Mexico MEX': 60, 'Puerto Rico PRI': 65,
        'Colombia COL': 67, 'Costa Rica CRI': 74}
countries = list(dataLAT.keys())
values = list(dataLAT.values())

fig = plt.figure(figsize=(8, 5))

# bar plot - South America
plt.bar(countries, values, color='blue', edgecolor= 'black',
        width=0.6)

plt.xlabel("Country")
plt.ylabel("Ranking")
plt.title("Top 5 countries in South America (LATAM) - (Ease of Business)")
plt.show()

## TOP 6 Countries - ease of business ##
dataALL = {'DNK': 4, 'SWE': 10, 'LTV': 11,
        'CHL': 59, 'MEX': 60, 'PRI': 65}
countries = list(dataALL.keys())
values = list(dataALL.values())

fig = plt.figure(figsize=(8, 5))

# bar plot - top 3 countries for each region
plt.bar(countries, values, color='orange', edgecolor= 'darkorange',
        width=0.6)

plt.xlabel("Country")
plt.ylabel("Ranking")
plt.title("Top 3 Countries from each region - Ease of Business")
plt.show()

## TOP 6 Countries - starting a business ##
dataSB = {'GRC':11, 'EST': 14, 'IRL': 23,
        'PAN': 51, 'CHL': 57, 'PRI': 59}
countries = list(dataSB.keys())
values = list(dataSB.values())

fig = plt.figure(figsize=(8, 5))

# bar plot - top 3 countries for each region
plt.bar(countries, values, color='blue', edgecolor= 'black',
        width=0.6)

plt.xlabel("Country")
plt.ylabel("Ranking")
plt.title("Top 3 Countries from each region - Starting a Business")
plt.show()
