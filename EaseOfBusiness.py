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

# FUNCTION(s)
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


# Merge on dataSA and dataEU
# EUSA=pd.merge(dataEU,
#                dataSA[['Alpha3']],
#                on='Alpha3')
# print(EUSA)
# This data uses dataEU and removes any values greater or equal to 70
visEU = dataEU[~(dataEU['globalRank'] >= 50)]
print(visEU)

visSA = dataSA[~(dataSA['globalRank'] >= 50)]
print(visSA)

# Test matplotlib

plt.plot(dataEU['globalRank'])
plt.show()

# 1st Demo
n, bins, patches = plt.hist(visEU['globalRank'],
                            facecolor='blue',
                            edgecolor='darkblue',
                            bins=20)
print('n: ', n)
print('bins: ', bins)
print('patches: ', patches)
plt.show()

# 2nd demo

# Fixing random state for reproducibility
# np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
# after people, removed for time being- , labels=people
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()

# 3rd Demo
# x-coordinates of left sides of bars
left = [1, 2, 3, 4, 5]

# heights of bars
height = [10, 24, 36, 40, 5]

# labels for bars
tick_label = ['one', 'two', 'three', 'four', 'five']

# plotting a bar chart
plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=['red', 'green'])

# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('My bar chart!')

# function to show the plot
plt.show()



# fig, simple_chart = matplotlib.pyplot.subplots()
# simple_chart.plot(dataSA.globalRank)
# matplotlib.pyplot.show()