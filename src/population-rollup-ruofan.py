pip install pandas
import pandas as pd

# import the dataset 
df = pd.read_csv("./input/censustract-00-10.csv")

# select the columns we need
df_select = df[['CBSA09', 'CBSA_T', 'POP00', 'POP10', 'PPCHG']]

# drop na
# drop the rows where at least one element is missing
df_select = df_select.dropna()

# summary of columns
df_select.info(verbose=True)

# get the index of the rows that cannot calculate PPCHG and drop them
i = df_select[df_select.PPCHG=='(X)'].index
df_select = df_select.drop(i)

# if the PPCHG's value is out of the range of 3 digits' number, it contains the comma symbol, which needs to be deleted when doing the calculation
df_select['PPCHG'] = df_select['PPCHG'].str.replace(",", "")

# change PPCHG to numeric
df_select['PPCHG'] = pd.to_numeric(df_select['PPCHG'])

# groupby
df_groupby = df_select.groupby('CBSA_T').agg({
    'CBSA09':['mean','count'],
    'POP00':'sum',
    'POP10':'sum',
    'PPCHG':'mean'})

# change column names
df_groupby.columns = ['CBSA09', 'TRACTS', 'POP00', 'POP10', 'PPCHG']

# make index as a column and reset index
df_groupby = df_groupby.reset_index()

# change the order of columns
col_names = ['CBSA09', 'CBSA_T', 'TRACTS', 'POP00', 'POP10', 'PPCHG']
df_report = df_groupby[col_names]

# round PPCHG to two decimal places
df_report['PPCHG'] = round(df_report['PPCHG'], 2)

# sort df_report by Core Based Statstical Area Code (ascending)
df_report = df_report.sort_values(by='CBSA09', ascending=True)

# write df_report to report.csv without index
df_report.to_csv("./output/report.csv", index=False, header=False)
