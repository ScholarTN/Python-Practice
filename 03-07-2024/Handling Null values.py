#1.import pandas and numpy, create a sample dataframe with null values.

##2. Identify null values:
   #- Use `df.isnull()` or `df.isna()` to check for null values
   #- Use `df.isnull().sum()` to count null values per column

##3. Remove rows with null values:
   #- `df.dropna()` removes rows with any null values
   #- `df.dropna(subset=['A', 'B'])` removes rows with nulls in specific columns

##4.Fill null values:
   #- `df.fillna(0)` replaces all nulls with 0
   #- `df['A'].fillna(df['A'].mean())` fills nulls with column mean
   #- `df.fillna(method='ffill')` or `df.fillna(method='bfill')` for forward/backward fill

##5. Interpolate values:
   #- `df.interpolate()` fills nulls using interpolation

##6. Replace null values:
  # - `df.replace({np.nan: None})` replaces NaN with None



import pandas as pd
import numpy as np

# Create a sample DataFrame with null values
df = pd.DataFrame({
    'Date': pd.date_range('2023-01-01', periods=10),
    'Temperature': [25, np.nan, 24, 23, np.nan, 22, 21, np.nan, 20, 19],
    'Humidity': [60, 62, np.nan, 58, 57, np.nan, 55, 54, np.nan, 52],
    'WindSpeed': [5, 6, 7, np.nan, 9, 10, np.nan, 12, 13, 14],
    'Precipitation': [0, 0, 5, 10, 0, np.nan, 0, 0, 15, np.nan]
})

print("Original DataFrame:")
print(df)
print("\nNull value counts:")
print(df.isnull().sum())

# Remove rows where all weather measurements are null
df_cleaned = df.dropna(subset=['Temperature', 'Humidity', 'WindSpeed', 'Precipitation'], how='all')

# Fill Temperature nulls with mean
df_cleaned['Temperature'] = df_cleaned['Temperature'].fillna(df_cleaned['Temperature'].mean())

# Forward fill Humidity
df_cleaned['Humidity'] = df_cleaned['Humidity'].fillna(method='ffill')

# Interpolate WindSpeed
df_cleaned['WindSpeed'] = df_cleaned['WindSpeed'].interpolate()

# Replace Precipitation nulls with 0 (assuming no precipitation)
df_cleaned['Precipitation'] = df_cleaned['Precipitation'].fillna(0)

print("\nCleaned DataFrame:")
print(df_cleaned)
print("\nRemaining null values:")
print(df_cleaned.isnull().sum())

# Demonstrate replacing NaN with None (useful for certain operations or exports)
df_none = df_cleaned.replace({np.nan: None})
print("\nDataFrame with None instead of NaN:")
print(df_none)
