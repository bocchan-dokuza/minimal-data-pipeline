# %%

import pandas as pd

# path of file
input_path = 'data/Sample - Superstore.xlsx'
output_path = 'data/superstore_cleaned.csv'

# read csv file
df = pd.read_excel(input_path, engine="openpyxl")

# conver data type to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# remove postal code
df = df.drop(columns=['Postal Code'])

# Check the first five rows
print("Top 5 rows:\n", df.head())

# Save as csv without index column
df.to_csv(output_path, index=False)

print(f"Cleaned CSV saved to {output_path}")

