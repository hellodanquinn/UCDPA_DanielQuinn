
# Installed 'country-convert' as will need this after import of CSV to convert country names to Alpha2
# Installed Pandas
# Numpy running 1.21.0
# Import CSV file
# Analyse data imported
# Clean up data

import pandas as pd
print(pd.__version__)

import numpy as np
print(np.__version__)
l = [1, 2, 3]
l_array = np.array(l)
print(type(l_array))

hdg = "128"
print(hdg + " Success")

# import pandas as pd
# Read data from the csv file
data = pd.read_csv("Rankings_EaseOf.csv")

# Preview data from the first 5 lines
data.head()

print(data.head())

