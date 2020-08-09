'''
Author: Onur Sevket Aslan
Start Date: 2020/08/01
Revision Date: 2020/08/01
Revision: 1

Title: Sales increase analysis for Nuveen 
'''
#%%Libraries
import pandas as pd


#%%Data ingestion
filename_x='../../Transaction Data.xlsx'
data_x=pd.read_excel(filename_x, sheet_name='Transactions18') #reading X's
data_y=pd.read_excel(filename_x, sheet_name='Transactions19') #reading Y's

#%%Exploratory Data Analysis (EDA)