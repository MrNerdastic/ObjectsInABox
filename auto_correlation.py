import numpy as np

def auto_correlate(a, b):
    np.correlate(a, b, "full")
