import pandas as pd
import sqlite3

# Database connection
conn = sqlite3.connect("database/mutual_fund.db")

# Read all datasets
fund_master = pd.read_csv("data/raw/mutual_fund_data/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/mutual_fund_data/02_nav_history.csv")
aum = pd.read_csv("data/raw/mutual_fund_data/03_aum_by_fund_house.csv")
sip = pd.read_csv("data/raw/mutual_fund_data/04_monthly_sip_inflows.csv")
category = pd.read_csv("data/raw/mutual_fund_data/05_category_inflows.csv")
folio = pd.read_csv("data/raw/mutual_fund_data/06_industry_folio_count.csv")
performance = pd.read_csv("data/raw/mutual_fund_data/07_scheme_performance.csv")
transactions = pd.read_csv("data/raw/mutual_fund_data/08_investor_transactions.csv")
holdings = pd.read_csv("data/raw/mutual_fund_data/09_portfolio_holdings.csv")
benchmark = pd.read_csv("data/raw/mutual_fund_data/10_benchmark_indices.csv")

# Store tables in SQLite
fund_master.to_sql("fund_master", conn, if_exists="replace", index=False)
nav_history.to_sql("nav_history", conn, if_exists="replace", index=False)
aum.to_sql("aum_by_fund_house", conn, if_exists="replace", index=False)
sip.to_sql("monthly_sip_inflows", conn, if_exists="replace", index=False)
category.to_sql("category_inflows", conn, if_exists="replace", index=False)
folio.to_sql("industry_folio_count", conn, if_exists="replace", index=False)
performance.to_sql("scheme_performance", conn, if_exists="replace", index=False)
transactions.to_sql("investor_transactions", conn, if_exists="replace", index=False)
holdings.to_sql("portfolio_holdings", conn, if_exists="replace", index=False)
benchmark.to_sql("benchmark_indices", conn, if_exists="replace", index=False)

print("All tables loaded successfully!")

conn.close()