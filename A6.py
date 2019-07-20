# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 10:09:34 2019

@author: AR
"""
import pandas as pd
import statsmodels.api as sm
mtcars = sm.datasets.get_rdataset(dataname='mtcars', package='datasets')
mtcars.data.reset_index(level=0, inplace=True)
mtcars.data=mtcars.data.rename(columns={'index':'carname'})

mtcars.data
#structure summary
str(mtcars)
print(mtcars.data.info())
print(mtcars.data.describe())


#Number of Rows
len(mtcars.data)
#number of rows and columns
mtcars.data.shape

#first / last few rows
print(mtcars.data.head())
print(mtcars.data.tail())

    
#column names   
#1.
for col in mtcars.data.columns: 
    print(col)
# OR 2.    
list(mtcars.data.columns)

#filter rows

#cyl=8
df=mtcars.data[mtcars.data.cyl==8]
print(df)

#mpg<=27
df1=mtcars.data[mtcars.data.mpg<=27]
print(df1)

#rows match auto tx
df2=mtcars.data[mtcars.data['carname']=='auto tx']
print(df2)

#first row
#1.
print(mtcars.data[0:1])

# OR 2.
print(mtcars.data.head(1))

#last row
#1.
print(mtcars.data[-1:])

# OR 2.
print(mtcars.data.tail(1))


# 1st, 4th, 7th, 25th row + 1st 6th 7th columns.
print(mtcars.data.iloc[[0,3,6,24],[0,5,6]])

# first 5 rows and 5th, 6th, 7th columns of data frame
print(mtcars.data.iloc[0:5,5:8])

#rows between 25 and 3rd last
print(mtcars.data.iloc[24:-3])

#alternative rows and alternative column
print(mtcars.data[::2])
m1=mtcars.data.columns[::2]
m1

1.#find row with Mazda RX4 Wag and columns cyl, am
mt1=mtcars.data[mtcars.data['carname']=='Mazda RX4 Wag']
mt1.loc[:,['carname','cyl','am']]

1.#find row betwee Merc 280 and Volvo 142E Mazda RX4 Wag and columns cyl, am
import numpy as np
m0=mtcars.data.loc[mtcars.data['carname']==('Merc 280''Volvo 142E')]


# mpg > 23 or wt < 2
df4=mtcars.data[(mtcars.data.mpg>23) | (mtcars.data.wt<2)]
print(df4)

3.#using lambda for above
mtcars.data.apply(lambda x: mtcars.data[(mtcars.data.mpg>23)|(mtcars.data.wt<2)])

#with or condition
df4=mtcars.data[(mtcars.data.mpg>23) | (mtcars.data.wt<2)]
print(df4)

#find unique rows of cyl, am, gear
#using unique give output as an array
mtcars.data['cyl'].unique()
mtcars.data['am'].unique()
mtcars.data['gear'].unique()
#using drop_duplicates t the unique rows
mtcars.data.drop_duplicates('cyl')
mtcars.data.drop_duplicates('am')
mtcars.data.drop_duplicates('gear')

#create new columns: first make a copy of mtcars to mtcars2
mtcars2=mtcars.data.copy()
mtcars2['New_col']=range(len(mtcars2))
# OR
mtcars2['New_col']=''
mtcars2
mtcars.data.reset_index
mtcars.data
#keeps other cols and divide displacement by 61
mtcars2['disp_div_by_61'] = (mtcars2.disp)/61
mtcars2

# multiple mpg * 1.5 and save as original column
mtcars2['mpg*1.5'] = (mtcars2.mpg)*1.5
mtcars2
