#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 22:35:42 2023

@author: jennitran
"""

# Bootstrap class

import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *
import os

os.chdir("/Users/jennitran/Downloads/2017_Fuel_Economy_Data.csv")

dat = pd.read_csv("2017_Fuel_Economy_Data.csv")

dat = dat["Combined Mileage (mpg)"]
n = len(dat)
n_boot = 10_000

stat = "mean"

boot_stat = []

for i in range(n_boot):
    boot_sample = dat.sample(n, replace = True)
    
    if stat == "median":
        boot_stat.append(float(boot_sample.median()))
    elif stat == "mean":
        boot_stat.append(float(boot_sample.mean()))
    elif stat == "std dev":
        boot_stat.append(float(boot_sample.std()))
    else:
        raise TypeError("Wrong statistic name")
    
boot_df = pd.DataFrame({'x': boot_stat})

(
ggplot(boot_df, aes(x = "x")) +
geom_histogram()
)

#%%

class Boot_CI():
    def __init__(self):
        self.stat = "mean"
        self.dat = None
        self.n_boot = 0
        self.boot_stat = None
        self.ci_level = 0.95
        
test = Boot_CI()

