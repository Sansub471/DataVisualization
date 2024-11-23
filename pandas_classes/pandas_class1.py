import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a sample DataFrame with random data
np.random.seed(42)
data = {
    'Date': pd.date_range(start='2024-01-01', periods=10),
    'Sales': np.random.randint(100, 500, size=10),
    'Expenses': np.random.randint(50, 300, size=10)
}
df = pd.DataFrame(data)

# Add a Profit column
df['Profit'] = df['Sales'] - df['Expenses']

# Print the first 5 rows of the DataFrame
print(df.head())

# Calculate summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Plot Sales, Expenses, and Profit
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Sales'], label='Sales', marker='o')
plt.plot(df['Date'], df['Expenses'], label='Expenses', marker='s')
plt.plot(df['Date'], df['Profit'], label='Profit', marker='d')

# Customize the plot
plt.title("Sales, Expenses, and Profit Over Time")
plt.xlabel("Date")
plt.ylabel("Amount ($)")
plt.legend()
plt.grid()

# Show the plot
# plt.show()
