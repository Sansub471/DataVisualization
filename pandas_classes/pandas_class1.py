import pandas as pd

import pandas as pd
import numpy as np

# 1. Load the dataset
df = pd.read_csv("data.csv")

# 2. Display basic info
print("Dataset Info:")
print(df.info())

# 3. Display first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# 4. Display column names
print("\nColumn Names:")
print(df.columns)

# 5. Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 6. Drop rows with missing values
df_cleaned = df.dropna()

# 7. Fill missing values with column mean (if numeric)
for col in df.select_dtypes(include=np.number):
    df[col].fillna(df[col].mean(), inplace=True)

# 8. Add a new column with a transformation
df['log_column1'] = np.log1p(df['column1'])

# 9. Rename a column
df.rename(columns={'old_column_name': 'new_column_name'}, inplace=True)

# 10. Filter rows where a column value is greater than a threshold
filtered_df = df[df['column2'] > 50]

# 11. Group by a column and calculate mean
grouped_mean = df.groupby('category_column')['numeric_column'].mean()
print("\nGrouped Mean:")
print(grouped_mean)

# 12. Add a calculated column
df['difference'] = df['column1'] - df['column2']

# 13. Sort the dataframe by a column
df_sorted = df.sort_values(by='column1', ascending=False)

# 14. Get unique values in a column
unique_values = df['category_column'].unique()
print("\nUnique Values in 'category_column':")
print(unique_values)

# 15. Count occurrences of unique values
value_counts = df['category_column'].value_counts()
print("\nValue Counts:")
print(value_counts)

# 16. Drop duplicate rows
df_no_duplicates = df.drop_duplicates()

# 17. Select specific columns
selected_columns = df[['column1', 'column2', 'category_column']]

# 18. Apply a lambda function to a column
df['squared_column1'] = df['column1'].apply(lambda x: x**2)

# 19. Filter rows using multiple conditions
filtered_rows = df[(df['column1'] > 50) & (df['category_column'] == 'A')]

# 20. Pivot table example
pivot_table = pd.pivot_table(df, values='column1', index='category_column', aggfunc=np.mean)
print("\nPivot Table:")
print(pivot_table)

# 21. Merge two datasets (assume df2 is another dataframe)
df2 = pd.DataFrame({'category_column': ['A', 'B', 'C'], 'extra_info': [100, 200, 300]})
merged_df = pd.merge(df, df2, on='category_column', how='left')

# 22. Drop a column
df_dropped = df.drop(columns=['unnecessary_column'])

# 23. Save the cleaned dataframe to a new CSV
df.to_csv("cleaned_data.csv", index=False)

# 24. Display the correlation matrix
print("\nCorrelation Matrix:")
print(df.corr())

# 25. Create dummy variables
df_with_dummies = pd.get_dummies(df, columns=['category_column'], drop_first=True)

# 26. Reset the index
df.reset_index(drop=True, inplace=True)

# 27. Sample a subset of rows
sampled_df = df.sample(n=10)

# 28. Add a row
new_row = pd.DataFrame({'column1': [10], 'column2': [20], 'category_column': ['D']})
df = pd.concat([df, new_row], ignore_index=True)

# 29. Describe the dataset
print("\nStatistical Summary:")
print(df.describe())

# 30. Count missing values after transformations
print("\nMissing Values After Transformations:")
print(df.isnull().sum())

# 31. Use query to filter rows
queried_rows = df.query('column1 > 50 and column2 < 100')

# 32. Explode a list column into multiple rows
if 'list_column' in df.columns:
    df = df.explode('list_column')

# 33. Calculate a rolling mean
if 'numeric_column' in df.columns:
    df['rolling_mean'] = df['numeric_column'].rolling(window=3).mean()

# 34. Convert a column to datetime
if 'date_column' in df.columns:
    df['date_column'] = pd.to_datetime(df['date_column'])

# 35. Extract year from a datetime column
if 'date_column' in df.columns:
    df['year'] = df['date_column'].dt.year

# 36. Display the first 5 rows of the final dataframe
print("\nFinal Dataset Preview:")
print(df.head())
