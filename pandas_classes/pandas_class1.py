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



# Show the plot
# plt.show()
