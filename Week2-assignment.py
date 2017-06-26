#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 10:36:30 2017

@author: alina
"""

#import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#read in the data
data1 = pd.read_csv('gapminder2.csv', low_memory=False)

#remove unnecessary columns and make a copy of the subdata
data2 = data1[["continent", "country", "breastcancerper100th", "urbanrate", "incomeperperson", "breastcancernbdeaths"]]
data = data2.copy()

#remove missing values(in my case '0' values)
data= data.replace(0, np.NaN)
data = data.dropna()


print(len(data))
print(len(data.columns))


# Change the data type for chosen variables
data['breastcancerper100th'] = pd.to_numeric(data['breastcancerper100th'])
data['breastcancernbdeaths'] = pd.to_numeric(data['breastcancernbdeaths'])
data['incomeperperson'] = pd.to_numeric(data['incomeperperson'])
data['urbanrate'] = pd.to_numeric(data['urbanrate'])


##calculate frequencies for variables that you decided to work with (as requested)

#urbanrate rate
print("first values for urban rate:")
urbanrate_freq = pd.concat(dict(counts = data["urbanrate"].value_counts(sort=False, dropna=False), percentages = data["urbanrate"].value_counts(sort=False, dropna=False, normalize=True)), axis=1)
print(urbanrate_freq.head(5))

#income per person
print("first values for capita GDP:")
gdp_freq = pd.concat(dict(counts = data["incomeperperson"].value_counts(sort=False, dropna=False), percentages = data["incomeperperson"].value_counts(sort=False, dropna=False, normalize=True)), axis=1)
print(gdp_freq.head(5))

#breast cancer cases per 100 000
print("first values for breast cancer incidence:")
breastcancer_freq = pd.concat(dict(counts = data["breastcancerper100th"].value_counts(sort=False, dropna=False), percentages = data["breastcancerper100th"].value_counts(sort=False, dropna=False, normalize=True)), axis=1)
print(breastcancer_freq.head(5))

#breast cancer nb of deaths
print("first values for breast cancer nb deaths:") 
breastcancerdeaths_freq = pd.concat(dict(counts = data["breastcancernbdeaths"].value_counts(sort=False, dropna=False), percentages = data["breastcancernbdeaths"].value_counts(sort=False, dropna=False, normalize=True)), axis=1)
print(breastcancerdeaths_freq.head(5))

