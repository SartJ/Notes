# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 14:05:03 2021

@author: sartaj
"""
import pandas as pd
import numpy as np
# import sklearn

volunteer = pd.read_csv('volunteer_opportunities.csv')

#.head(n) used to return first n rows of a dataFrame to check
print(volunteer.head(3))


#To check the shape (no_rows or samples, no_colums or features) of the dataFrame:-
print(volunteer.shape)

#return boolean value where dataFrame has null or not:-
print(volunteer.isnull())

#to find out how many null values each feature has:-
print(volunteer.isnull().sum())

#Dropping some columns:-
volunteer = volunteer.drop(['BIN','BBL','NTA'], axis = 1)
print(volunteer.shape)


# Check how many values are missing in
# the category_des column:-
print("Number of rows with null values in category_desc column:-")
print(volunteer['category_desc'].isnull().sum())


#Subset the volunteer dataset:-
volunteer_subset = volunteer[volunteer['category_desc'].notnull()]

print('Shape after removing null values:-')
print(volunteer_subset.shape)


print("Shape of dataframe before dropping:")
print(volunteer.shape)

volunteer = volunteer.dropna(axis = 0, subset = ['category_desc'])
print('Shape after dropping:')
print(volunteer.shape)



"""
Sales Dataset:
"""

sales = pd.read_csv('sales.csv', index_col=['month'])
print(sales)


#Fills the null place with the passed value:-
sales = sales.fillna(50)
print(sales)





















































































































