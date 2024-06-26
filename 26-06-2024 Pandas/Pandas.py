##1. Installation:
#First, install pandas

"""pip install pandas"""


##2. Importing pandas:
#Once installed, you import pandas in your Python script:

import pandas as pd
import pandas as pd

##3. Creating a DataFrame:
#The DataFrame is the primary data structure in pandas.

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Paris', 'London']}
df = pd.DataFrame(data)

##4. Viewing the DataFrame:
  #To see your DataFrame, you can use:
print(df)


##5. Basic operations:

#- Accessing a column:

print(df['Name'])
  

#- Adding a new column:
  
df['Salary'] = [50000, 60000, 70000]
  

#- Filtering data:
young_people = df[df['Age'] < 30]


##6. Reading data from files:
df = pd.read_csv('your_file.csv')

##7. Basic statistics:
#You can get quick statistics of your numerical columns:

print(df.describe())


##8. Handling missing data:
#To check for missing values:

print(df.isnull().sum())

#To drop rows with missing values:

df_cleaned = df.dropna()


##9. Grouping and aggregating:
#Group by a column and perform operations:

grouped = df.groupby('City')
print(grouped['Age'].mean())

##10. Merging DataFrames:
 #You can combine DataFrames using various methods:

df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value': [4, 5, 6]})
merged = pd.merge(df1, df2, on='key', how='outer')


##11. Reshaping data:
  #Pivot tables can be created easily:

pivot = df.pivot_table(values='Salary', index='City', columns='Name')

##12. Time series handling:
#Pandas has excellent support for time series data:

dates = pd.date_range('20230101', periods=6)
ts = pd.Series(range(6), index=dates)
