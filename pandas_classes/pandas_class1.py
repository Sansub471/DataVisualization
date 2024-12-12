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

# Example Usage:
if __name__ == "__main__":
    # Example to demonstrate functions (requires valid CSV and columns)
    try:
        df = pd.read_csv('Data/stack-overflow-developer-survey-2024/survey_results_public.csv')
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
    except FileNotFoundError:
        print("Please provide a valid 'data.csv' file in the working directory.")
