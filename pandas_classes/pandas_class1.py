import pandas as pd

# 1. Read CSV File
def read_csv_example():
    df = pd.read_csv('Data/stack-overflow-developer-survey-2024/survey_results_public.csv')
    print("First 5 rows:")
    print(df.head())

# 2. Display First N Rows
def head_example(df):
    print("First 10 rows:")
    print(df.head(10))

# 3. Get DataFrame Info
def info_example(df):
    print("DataFrame Info:")
    df.info()

# 4. Summary Statistics
def describe_example(df):
    print("Summary Statistics:")
    print(df.describe())

# 5. Check for Missing Values
def check_missing_values(df):
    print("Missing Values Count:")
    print(df.isnull().sum())

# 6. Fill Missing Values
def fill_missing_values(df):
    df['column_name'] = df['column_name'].fillna(0)  # Replace NaN with 0
    print("Filled Missing Values:")
    print(df.head())

# 7. Group Data by Column
def group_by_example(df):
    grouped = df.groupby('category').sum()
    print("Grouped Data:")
    print(grouped)

# 8. Sort Data by Column
def sort_values_example(df):
    sorted_df = df.sort_values(by='column_name', ascending=True)
    print("Sorted Data:")
    print(sorted_df.head())

# 9. Apply Function to Column
def apply_example(df):
    df['new_col'] = df['col'].apply(lambda x: x * 2)
    print("After Applying Function:")
    print(df.head())

# 10. Merge Two DataFrames
def merge_example(df1, df2):
    merged = pd.merge(df1, df2, on='common_column', how='inner')
    print("Merged DataFrame:")
    print(merged.head())


# Learning next important pands functions for the day

# 11. Concatenate DataFrames
def concat_example(df1, df2):
    combined = pd.concat([df1, df2], axis=0)
    print("Concatenated DataFrame:")
    print(combined.head())

# 12. Create Pivot Table
def pivot_table_example(df):
    pivot = pd.pivot_table(df, values='value_col', index='index_col', columns='category_col', aggfunc='sum')
    print("Pivot Table:")
    print(pivot)

# 13. Check for Duplicates
def check_duplicates(df):
    print("Duplicate Rows:")
    print(df[df.duplicated()])

# 14. Drop Duplicates
def drop_duplicates_example(df):
    df = df.drop_duplicates()
    print("Data After Dropping Duplicates:")
    print(df.head())

# 15. Rename Columns
def rename_columns_example(df):
    df = df.rename(columns={'old_name': 'new_name'})
    print("Renamed Columns:")
    print(df.head())

# 16. Random Sampling
def sample_example(df):
    sample = df.sample(n=5)
    print("Random Sample of Rows:")
    print(sample)

# 17. Value Counts
def value_counts_example(df):
    print("Value Counts:")
    print(df['column_name'].value_counts())

# 18. Melt DataFrame
def melt_example(df):
    melted = pd.melt(df, id_vars=['id'], value_vars=['col1', 'col2'])
    print("Melted DataFrame:")
    print(melted.head())

# 19. Correlation Matrix
def correlation_example(df):
    correlation = df.corr()
    print("Correlation Matrix:")
    print(correlation)

# 20. Export to CSV
def to_csv_example(df):
    df.to_csv('output.csv', index=False)
    print("DataFrame exported to 'output.csv'")

# Example Usage:
if __name__ == "__main__":
    # Example to demonstrate functions (requires valid CSV and columns)
    try:
        df = pd.read_csv('/mnt/data/survey_results_public.csv')
        read_csv_example()
        head_example(df)
        info_example(df)
        describe_example(df)
        check_missing_values(df)
        # Uncomment below lines after ensuring the column names exist in your data
        # fill_missing_values(df)
        # group_by_example(df)
        # sort_values_example(df)
        # apply_example(df)
        # Example merge (requires second DataFrame df2)
        # merge_example(df, df2)
        # Additional examples
        # concat_example(df, df2)
        # pivot_table_example(df)
        # check_duplicates(df)
        # drop_duplicates_example(df)
        # rename_columns_example(df)
        # sample_example(df)
        # value_counts_example(df)
        # melt_example(df)
        # correlation_example(df)
        # to_csv_example(df)
    except FileNotFoundError:
        print("Please provide a valid 'data.csv' file in the working directory.")

# Start of the day with python for me.