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


print("first values for capita GDP:")
gdp_freq = pd.concat(dict(counts = data["incomeperperson"].value_counts(sort=False, dropna=False), percentages = data["incomeperperson"].value_counts(sort=False, dropna=False, normalize=True)), axis=1)
print(gdp_freq.head(5))


##Create variable quartiles and calculate frequency in bins 

#calculate frequency in bins
data['urbanratepercent'] =pd.cut(data.urbanrate,4,labels=['0-25%','26-50%','51-74%','75-100%'])
urban_freq = pd.concat(dict(counts = data["urbanratepercent"].value_counts(sort=False, dropna=False),
                                   percentages = data["urbanratepercent"].value_counts(sort=False, dropna=False,
                                                                                       normalize=True)),
                            axis=1)
print("Frequency distribution - urban rate:\n", urban_freq)



#make new categorical variable to label income per person in 4 categories
#calculate frequency in bins
print('Income per person in categories')
data['incomelabel'] =pd.cut(data.incomeperperson,4,labels=['low','medium','high','very high'])
income_freq = pd.concat(dict(counts = data["incomelabel"].value_counts(sort=False, dropna=False),
                                   percentages = data["incomelabel"].value_counts(sort=False, dropna=False,
                                                                                       normalize=True)),
                            axis=1)
print("Frequency distribution - income per person:\n", income_freq)


#What are the countries with high and very high GDP? Order by income
print('Countries with high and very high GDP')
highincome = data[(data['incomelabel'] == 'high') | (data['incomelabel'] == 'very high') ]
print(highincome.loc[:, ['country', 'incomeperperson', 'incomelabel']].sort_values(by='incomelabel', ascending=False))


#make new categorical variable to calculate frequency in bins for breastcancerper100th
print('Categories of breast cancer cases per 100 000 females:')
data['cancercaseslabel'] =pd.cut(data.breastcancerper100th,4,labels=['low','medium','high','very high'])
breastcan_freq = pd.concat(dict(counts = data["cancercaseslabel"].value_counts(sort=False, dropna=False),
                                   percentages = data["cancercaseslabel"].value_counts(sort=False, dropna=False,
                                                                                       normalize=True)),
                            axis=1)
print("Frequency distribution - breast cancer bins:\n", breastcan_freq)

print('Number of new breast cancer cases in correlation with urban rate per country')
print(data.loc[:, ['country', 'urbanratepercent', 'cancercaseslabel']].sort_values(by='urbanratepercent', ascending=False))


#Find out if there is a correlation between a high urban rate and a high score of new cancer cases
print('High scores of new breast cancer cases in correlation with urban rate per country')
bchiur = data[(data['cancercaseslabel'] == 'high') | (data['cancercaseslabel'] == 'very high')]
bchiur=bchiur.sort_values(by='urbanratepercent', ascending=False)
print(bchiur.loc[:, ['country', 'urbanratepercent', 'cancercaseslabel']])
#There is! According to our table, in countries where the number of new breast cancer cases is high or very high, the urban rate is 
#in almost all cases above 51%.


#make new categorical variable to categorize the deaths caused by breast cancer
#calculate frequency in bins
print('Deaths due to breast cancer in categories')
data['deathsbreastcancerlabel'] =pd.cut(data.breastcancernbdeaths,4,labels=['low','medium','high','very high'])
deathsBC_freq = pd.concat(dict(counts = data["deathsbreastcancerlabel"].value_counts(sort=False, dropna=False),
                                   percentages = data["deathsbreastcancerlabel"].value_counts(sort=False, dropna=False,
                                                                                       normalize=True)),
                            axis=1)
print("Frequency distribution - breast cancer number of deaths:\n", deathsBC_freq)

print('Number of deaths due to breast cancer in correlation with urban rate per country')
print(data.loc[:, ['country', 'urbanratepercent', 'deathsbreastcancerlabel']].sort_values(by='urbanratepercent', ascending=False))

#Find out if there is a correlation between a low number of deaths caused by breast cancer and a high urban rate
print('Deaths due to breast cancer in countries with high urban rate ')
dehiur = data[(data['urbanratepercent'] == '75-100%')]
dehiur=dehiur.sort_values(by ='breastcancernbdeaths', ascending=True)
print(dehiur.loc[:, ['country', 'urbanratepercent', 'deathsbreastcancerlabel']])
#Apprently there is! Out of 38 countries with a 75% or more urban rate, only 4 have a medium (Brazil, France, Uk) and a very high number(US) 
#of number of breast cancer deaths. 

#But once we analyse the low number of number of deaths, irrespective of the urban rate in each country, we realise
#there is no direct correlation between the number of deaths and the urban rate of each country. 
print('Low number of deaths caused by breast cancer per country')
lowbc = data[(data['deathsbreastcancerlabel'] == 'low')]
print(lowbc.loc[:, ['country', 'urbanratepercent','deathsbreastcancerlabel']].sort_values(by='urbanratepercent', ascending=False)) 


print('Number of breast cancer deaths correlated with GDP per country')
print(data.loc[:, ['country', 'deathsbreastcancerlabel', 'incomelabel']].sort_values(by='deathsbreastcancerlabel', ascending=False))


#Find out if there is a correlation between a high GDP and a low number of deaths due to breast cancer
print('Number of breast cancer deaths in correlation with high GDP per country')
brur = data[(data['incomelabel'] == 'high') | (data['incomelabel'] == 'very high')]
brur=brur.sort_values(by='deathsbreastcancerlabel', ascending=True)
print(brur.loc[:, ['country', 'incomelabel', 'deathsbreastcancerlabel']].sort_values(by='incomelabel', ascending=False))
#Apprently there is! Out of 15 countries with high and very high income per person, only 2 register with medium (Uk) and very high(USA) number of deaths.

#But once we analyse the low number of number of deaths, irrespective of the level of income, we realise there is no direct
#correlation and that we should look for causes and factors of influence somewhere else. 
print('Low number of deaths caused by breast cancer, regardless of GDP')
print(lowbc.loc[:, ['country', 'incomelabel','deathsbreastcancerlabel']].sort_values(by='incomelabel', ascending=False)) 





#add new Continent column and calculate mean variables

print('Countries by Continent')
country_counts = data.groupby('continent').size()
print(country_counts)
print('\n')

print('GDP Statistics by Continent')
gdp_mean = data.groupby('continent')['incomeperperson'].agg([np.mean, np.median, len])
print(gdp_mean)

print('Urban rate by continent')
urban_mean = data.groupby('continent')['urbanrate'].agg([np.mean, np.median, len])
print(urban_mean)

print('Average of breast cancer cases by continent')
bc_mean = data.groupby('continent')[['breastcancerper100th', 'urbanrate', 'incomeperperson']].agg([np.mean, len])
print(bc_mean)

print('Average of deaths due to breast cancer by continent')
bcd_mean = data.groupby('continent')[['breastcancernbdeaths', 'urbanrate', 'incomeperperson']].agg([np.mean, len])
print(bcd_mean)




#Histogram Breast Cancer Cases
#sns.set_context('poster')
plt.figure(figsize=(14, 7))
sns.distplot(data["breastcancerper100th"], kde=False);
plt.xlabel('breast cancer cases per 100,000 females');
plt.title('Breast Cancer Cases per 100,000 Females in 2002');
plt.xlim(0,100)
plt.show()


#Histogram income per person
plt.figure(figsize=(14, 7))
sns.distplot(data['incomeperperson'], bins=10, kde=False)
plt.xlabel('Income per person')
plt.title('Capita GDP Per Person')
plt.show()


#Histogram urban rate
plt.figure(figsize=(14, 7))
sns.distplot(data['urbanrate'])
plt.xlabel('Urban rate per country')
plt.title('Percentage of urbanisation')
plt.show()


#Histogram number of deaths caused by breast cancer
plt.figure(figsize=(10, 7))
sns.distplot(data['breastcancernbdeaths'], bins=20, kde=False)
plt.xlabel('Breast cancer number of deaths')
plt.title('Number of deaths caused by breast cancer')
plt.show()

#Frequency distribution in bins - income per person
plt.figure(figsize=(14, 7))
sns.countplot(x='incomelabel', data=data)
plt.ylabel('Count')
plt.xlabel('Income per person')

#Frequency distribution in bins - urban rate
sns.set_context('poster')
plt.figure(figsize=(14, 7))
sns.countplot(x='urbanratepercent', data=data, palette="Set3")
plt.ylabel('Count')
plt.xlabel('Percentage of urbanisation')

#Frequency distribution in bins - breast cancer cases
sns.set_context('poster')
plt.figure(figsize=(14, 7))
sns.countplot(x='cancercaseslabel', data=data, palette="Greens_d")
plt.ylabel('Count')
plt.xlabel('Breast cancer cases')


#Frequency distribution in bins - deaths due to breast cancer
sns.set_context('poster')
plt.figure(figsize=(14, 7))
sns.countplot(x='deathsbreastcancerlabel', data=data, palette="Set1")
plt.ylabel('Count')
plt.xlabel('Breast cancer deaths')


#Show breast cancer incidences against urbanisation level
sns.factorplot(x='cancercaseslabel', y='urbanrate', data=data, kind='point', ci=None, size=3, aspect=5, color="green")
plt.ylabel('urban rate per country')
plt.xlabel('breast cancer cases categories')

#Is there an association between breast cancer and income level?
fig = plt.figure(figsize=(16,4))
sns.regplot(x="breastcancerper100th", y="incomeperperson", fit_reg=True, data=data);
plt.xlabel('breast cancer incidences');
plt.ylabel('capita GDP');
plt.title('Scatterplot for the association between breast cancer and income level');


#Is there an association between deaths caused by breast cancer and urbanisation level?
fig = plt.figure(figsize=(16,4))
sns.regplot(x="breastcancernbdeaths", y="urbanrate", fit_reg=True, data=data);
plt.xlabel('breast cancer deaths incidences');
plt.ylabel('percentage of urban rate');
plt.title('Scatterplot for the association between deaths due to breast cancer and urbanisation level');


#Show level of urbanisation per continent
sns.factorplot(x='continent', y='urbanrate', data=data, kind='bar', size=7, aspect=2)
plt.ylabel('urbanrate')
plt.xlabel('continent')


#Show breast cancer incidences per continent
sns.factorplot(x='continent', y='breastcancerper100th', data=data, kind='bar', size=7, aspect=2)
plt.ylabel('breast cancer cases')
plt.xlabel('continent')




