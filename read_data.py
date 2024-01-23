import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def read_data(file_path, column):
    data = pd.read_csv(file_path, skiprows=1)
    data = pd.read_csv(file_path, delimiter=';', skiprows=1)
    data = data.apply(lambda x: x.str.replace(',', '.').astype(float))
    values = data.iloc[:, column]
    """for x in range(len(values)):
        if values[x] == 0:
            values.pop(x)"""
    return values
