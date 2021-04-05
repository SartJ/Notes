# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 12:38:18 2021

@author: sartaj
"""

import pandas as pd
import numpy as np


#Series: First Main Datatype in Pandas

label = [1,2,3,4,5,6,7]

print(pd.Series(label))


d = { 'a':10, 'b':20, 'c':30 }
print(d)

print(pd.Series(d))


#DataFrame:-

a = np.random.randint(100,size=(5,4))
print(a)

c = pd.DataFrame(a)
print(c)

df = pd.DataFrame(a,['A','B','C','D','E'],['W','X','Y','Z'])
print(df)

print(df['X'])

print(df[['X','Z']])


#Entering new column:-

df['new_col'] = np.random.randint(10,size=5)
print(df)


# #Entering new row:-

# df['new_row'] = [1,2,3,4]


#Deleting a column or row:-
df.drop('new_col', axis=1, inplace=True)
print(df)

df.drop('E', axis=0, inplace=True)
print(df)


df = pd.read_csv('sales.csv',index_col='month')
print(df)


#Indexing DataFrames:-


##Indexing using square brackets:-

print(df['eggs']['May'])


##Using column attributes and row index/label:-

print(df.eggs['May'])


df_new = df[['eggs','spam']]
print(df_new)


print(type(df_new))
print(type(df['eggs']))


# A DataFrame is a collection of a number of series.


##Selecting part of a series:-
print(df['eggs'][1:4])

"""
Slicing DataFrames:-
Using the .loc accessor-
Access a group of rows and columns by label(s) or a boolean array.

A series is a 1D-array that can store any data type.

- LOC is not based on index. The stop limit is NOT exclusive.
- ILOC is based on index. The Stop limit is exclusive.

"""

"""
We can access row by 2 ways:
    1. Location based selection. loc('rowname')
    2. Numerical based selection. iloc(rowIndex) 
"""

print(df)

#April row print:-
print("April row print:-")
print(df.loc['Apr'])

print(df.loc['Mar','salt'])  #.loc['row','column']

print(df.loc['Feb':'Apr','eggs':'salt'])

print(df.loc['Feb',:])

print(df.loc['Jan':'Mar',['eggs','spam']])



"""
Using the iloc accessor:-
Purely integer-location based indexing for selection by position.
"""

print(df)

print(df.iloc[2])  #indexWise

#.iloc[row_index,col_index]

print(df.iloc[2][2])

print(df.iloc[2:4,2])  #Last Index Not Included



'''
Filtering DataFrames:-
Creating A Boolean Series.
'''

print(df[['salt','eggs']]>60)
print(df['eggs']>60)


a = df.salt >= 60
print(df)
print(df[a])

print(df[df.salt>=60])

print(df[(df.salt>=60) & (df.eggs<200)])


'''
Adding a new column:-
'''


print(df)

df['chicken']=[23,45,34,67,89,90]
print(df)

df2 = df.copy()

print(df2)

df2['apple'] = [3,4,5,6,7,8]

print(df)
print(df2)

other = pd.DataFrame({'eggs': ['K0','K1','K2'],
                      'salt': ['b10','b20','b40'],
                      'spam': ['s1','s2','s3'],
                      'chicken': ['h3','h5','h8'],
                      'apple': ['v12','v22','v42']}, index=["Jul","Aug","Sep"])
print(other)


df2=df2.append(other)
print(df2)

#changing column names:-

df2.columns=['V','W','X','Y','Z']
print(df2)

#drop a column:-

df2.drop("Z",axis=1,inplace=True)
df2.columns=['W','X','Y','Z']
print(df2)

df2['Bacon']=[0,0,0,0,0,0,0,0,1]
print(df2['Bacon'].any())
print(df2['Bacon'].all())


print(df2)

print(df2.loc[:,df2.any()])
print(df2.loc[:,df2.all()])



#Select any column with a null:-

print(df2.loc[:,df2.isnull().any()])

print(df2.loc[:,df2.notnull().any()])


#Drop Rows with any NaN:-

##Row dropping:-
df2.drop('Sep', axis=0, inplace=True)

print(df2)


df2.dropna(axis=0, how='any', inplace=True)
print(df2)























