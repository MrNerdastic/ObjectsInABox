import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os



colours = {
    "wood" : "chocolate"
}



for x in range(13):
    # Load the data from the CSV file, ignoring the first row
    file_path = 'Cracker_Holz_{}.csv'.format(x)
    material = 'cracker'
    number_of_spheres = x
    data = pd.read_csv(file_path, skiprows=1)

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
    y_values = data.iloc[:, 3]

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, color='blue')
    plt.title('Line Graph of the frequency and FFT')
    plt.xlabel('Frequenz')
    plt.ylabel('FFT')
    plt.grid(True)

    try:
        plt.savefig('results/{}/{}_{}.png'.format(material, material, number_of_spheres))
    except:
        try:  
            os.mkdir("results/" + material) 
            plt.savefig('results/{}/{}_{}.png'.format(material, material, number_of_spheres)) 
        except OSError as error:  
            print(error)
