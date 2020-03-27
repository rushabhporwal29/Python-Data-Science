# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import pandas as pd
import numpy as np

os.chdir("G:/rushabh/STUDY/PYTHON")
data_csv=pd.read_csv('Iris_data_sample.csv',index_col=0,na_values=["??","###"])
data_xlsx=pd.read_excel('Iris_data_sample.xlsx',sheet_name='Iris_data',index_col=0,na_values=["??","###"])
data_txt1=pd.read_table('Iris_data_sample.txt',delimiter=" ",index_col=0,na_values=["??","###"])
cars_data=pd.read_csv('Toyota.csv',index_col=0)


samp=cars_data.copy(deep=False)         #samp-cars_data (Creates Shallow Copy)
samp1=cars_data.copy(deep=True)         #Creates Deep Copy (no refrence to original copy)

Index=(cars_data.index)
print(Index)

Column=(cars_data.columns)
print(Column)

print(cars_data.size)

print(cars_data.shape)

print(cars_data.memory_usage())

print(cars_data.ndim)

print(cars_data.head(6))     #head() returns first 6 rows (By default 5 rows)





























