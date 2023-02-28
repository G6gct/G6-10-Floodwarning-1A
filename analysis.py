import numpy as np
import matplotlib.dates
import matplotlib.pyplot as plt
import datetime 

def polyfit(dates, levels, p):
    ndate = matplotlib.dates.date2num(dates)

    # Find coefficients of best-fit polynomial f(x) of degree 4
    p_coeff = np.polyfit(ndate - ndate[0], levels, p)

    # Convert coefficient into a polynomial that can be evaluated
    poly = np.poly1d(p_coeff)

    return poly