import pandas as pd
import os

# Update this with your folder name inside raw
folder_path = "data/raw/mutual_fund_data"

files = os.listdir(folder_path)

for file in files:
    if file.endswith(".csv"):

        file_path = os.path.join(folder_path, file)

        df = pd.read_csv(file_path)

        print("\n" + "=" * 60)
        print("Dataset:", file)

        print("\nShape:")
        print(df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("=" * 60)