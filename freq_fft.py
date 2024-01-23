import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# Load the data from the CSV file, ignoring the first row
file_path = 'Erdnuss_Holz_0.csv'
data = pd.read_csv(file_path, skiprows=1)
print(data)
data.head()

# Reload the data with the correct delimiter
data = pd.read_csv(file_path, delimiter=';', skiprows=1)

# Display the first few rows to verify the structure
data.head()

# Replace commas with dots in the dataframe and convert to float
data = data.apply(lambda x: x.str.replace(',', '.').astype(float))

# Display the first few rows to confirm the changes
data.head()




# Extracting the x and y values
x_values = data.iloc[:, 1]
# y_values_raw = data.iloc[:, 3]
y_values = data.iloc[:, 3]
#y_values = []
#clean_data_length = 2

# for x in range(len(y_values_raw)):
#     if x >= clean_data_length and x <= len(y_values_raw) - 3:
#         y_values.append((y_values_raw[x - 2] + y_values_raw[x - 1] + y_values_raw[x] + y_values_raw[x + 1] + y_values_raw[x + 2]) / (2 * clean_data_length + 1))
#     else:
#         y_values.append(y_values_raw[x])

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, linewidth='0.5')
# plt.title('Line Graph of the time and voltage')
plt.xlabel('freq')
plt.ylabel('fft')

plt.savefig("freq_fft.png")


plt.show()
