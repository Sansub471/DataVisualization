import pandas as pd
# Load the dataset
df = pd.read_csv("data.csv")

# Display the first few rows
print(df.head())

# Drop rows with missing values
df = df.dropna()

# Convert a column to lowercase (for example, 'name' column)
df['name'] = df['name'].str.lower()

# Filter rows based on a condition
filtered_df = df[df['age'] > 30]

# Calculate the average of a column (e.g., 'salary')
average_salary = filtered_df['salary'].mean()

# Display the result
print("Average salary for age > 30:", average_salary)