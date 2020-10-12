import boto3
import pandas as pd
#import os as os

# Road CSV file to dataframe
data = pd.read_csv('banking.csv')
df = pd.DataFrame(data)

# List the first 10 records
sampl = df.head(10)
print(sampl)

#listing down the column name
cols = df.columns
print (cols)

#Filering the data - removing unwanted column
data_filter1 = df.drop(['default', 'cons_price_idx', 'cons_conf_idx'], axis = 1)
print (data_filter1.head(10))

#renaming the column
data_filter2 = data_filter1.rename(columns = {'euribor3m': 'euro'})

#listing down the column name
cols = data_filter2.columns
print (cols)

# select one column (jobs) from the dataframe
jobs = df.loc[:, ['job']]
print(jobs)

# Removing Duplicates from the column
jobs_nodup = jobs.drop_duplicates()
print(jobs_nodup)

# Filer records based on criteria
data_filter3 = data_filter2[data_filter2['emp_var_rate'] > 0]
print(data_filter3.head(10))


# Extract specific columns
poutcome_data = data_filter3[['poutcome', 'emp_var_rate']]
print (poutcome_data.head())


#sum based on poutcome
sum_by_poutcome = poutcome_data.groupby(by=['poutcome']).mean()
print(sum_by_poutcome)
#print(sum_by_poutcome['poutcome', 'emp_var_rate'])
