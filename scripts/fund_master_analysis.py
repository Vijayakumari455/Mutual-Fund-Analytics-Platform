import pandas as pd

df = pd.read_csv("data/raw/mutual_fund_data/01_fund_master.csv")

print("\nTotal Funds:")
print(df.shape[0])

print("\nUnique Fund Houses:")
print(df["fund_house"].unique())

print("\nNumber of Fund Houses:")
print(df["fund_house"].nunique())

print("\nCategories:")
print(df["category"].unique())

print("\nSub Categories:")
print(df["sub_category"].unique())

print("\nRisk Categories:")
print(df["risk_category"].unique())