import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os



def clean_data(clean_data_length, u_values_raw):
    u_values = []
    for x in range(len(u_values_raw)):
        if x >= clean_data_length and x <= len(u_values_raw) - (clean_data_length + 1):
            averaging_values = []
            for y in range(clean_data_length + 1):
                if y != 0:
                    averaging_values.append(u_values_raw[x - y])
            for z in range(clean_data_length):
                if z != 0:
                    averaging_values.append(u_values_raw[x + z])
            averaging_values.append(u_values_raw[x])
            u_values.append(sum(averaging_values)/len(averaging_values))
        else:
            u_values.append(u_values_raw[x])
    return u_values