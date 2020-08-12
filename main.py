'''
Author: Onur Sevket Aslan
Start Date: 2020/08/01
Revision Date: 2020/08/09
Revision: 2

Title: Sales increase analysis for Nuveen 
'''
#%%Libraries
import pandas as pd
pd.set_option('display.max_columns',50)
pd.set_option('display.width',200)

#%%Data ingestion
filename_x='../../Transaction Data.xlsx'
data_x=pd.read_excel(filename_x, sheet_name='Transactions18') #reading X's
data_y=pd.read_excel(filename_x, sheet_name='Transactions19') #reading Y's

#%%Join tables
data=pd.merge(data_x,data_y,how='outer',left_on='CONTACT_ID',right_on='CONTACT_ID')
# print(data.columns.values)
#%%Data Cleaning
# data.info()
data.fillna(value=0,inplace=True) #filling NA with 0
# data.describe()

#sales must be greater than or equal to 0
# data.min()

sales_list=['sales_curr','sales_12M_x','sales_12M_y']
for sales_col in sales_list:
    data.loc[data[data[sales_col]<0].index.values,sales_col]=0

#AUM must be greater than or equal to 0. Negatives must be changed to 0.
aum_list=['AUM','aum_AC_EQUITY','aum_AC_FIXED_INCOME_MUNI','aum_AC_FIXED_INCOME_TAXABLE','aum_AC_MONEY','aum_AC_MULTIPLE','aum_AC_PHYSICAL_COMMODITY','aum_AC_REAL_ESTATE','aum_AC_TARGET','aum_P_529','aum_P_ALT','aum_P_CEF','aum_P_ETF','aum_P_MF','aum_P_SMA','aum_P_UCITS','aum_P_UIT'
]
for col in aum_list:
    data.loc[data[data[col]<0].index.values,col]=0

#redemption must be less than 0
# data.max()

redemption_list=['redemption_curr','redemption_12M']
for redemption_col in redemption_list:
    data.loc[data[data[redemption_col]>0].index.values,redemption_col]=0
    
#1K sales must be greater than 10K sales
if(data['no_of_sales_12M_1'].max()>=data['no_of_sales_12M_10K'].max()):
    print('Sales comparison is OK')
else:
    print('Sales comparison is not OK')
if(data['no_of_funds_sold_12M_1'].max()>=data['no_of_fund_sales_12M_10K'].max()):
    print('Funds comparison is OK')
else:
    print('Funds comparison is not OK')
if(data['no_of_assetclass_sold_12M_1'].max()>=data['no_of_assetclass_sales_12M_10K'].max()):
    print('Asset comparison is OK')
else:
    print('Asset comparison is not OK')
if(data['no_of_Redemption_12M_1'].max()>=data['no_of_Redemption_12M_10K'].max()):
    print('Redemption comparison is OK')
else:
    print('Redemption comparison is not OK')
if(data['no_of_funds_redeemed_12M_1'].max()>=data['no_of_funds_Redemption_12M_10K'].max()):
    print('Fund redemption comparison is OK')
else:
    print('Fund redemption comparison is not OK')
if(data['no_of_assetclass_redeemed_12M_1'].max()>=data['no_of_assetclass_Redemption_12M_10K'].max()):
    print('Assetclass redemption comparison is OK')
else:
    print('Assetclass redemption comparison is not OK')
    
# sales_12M_y must be 0 or 1
data.loc[data[data['sales_12M_y']>0].index.values,'sales_12M_y']=1
#%%Exploratory Data Analysis (EDA)
# data.head(10)
