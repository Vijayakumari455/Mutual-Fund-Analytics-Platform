import pandas as pd

files = {
    "Fund Master": "data/raw/mutual_fund_data/01_fund_master.csv",
    "NAV History": "data/raw/mutual_fund_data/02_nav_history.csv",
    "AUM By Fund House": "data/raw/mutual_fund_data/03_aum_by_fund_house.csv",
    "Monthly SIP Inflows": "data/raw/mutual_fund_data/04_monthly_sip_inflows.csv",
    "Category Inflows": "data/raw/mutual_fund_data/05_category_inflows.csv",
    "Industry Folio Count": "data/raw/mutual_fund_data/06_industry_folio_count.csv",
    "Scheme Performance": "data/raw/mutual_fund_data/07_scheme_performance.csv",
    "Investor Transactions": "data/raw/mutual_fund_data/08_investor_transactions.csv",
    "Portfolio Holdings": "data/raw/mutual_fund_data/09_portfolio_holdings.csv",
    "Benchmark Indices": "data/raw/mutual_fund_data/10_benchmark_indices.csv"
}

for name, path in files.items():

    df = pd.read_csv(path)

    print("\n" + "="*60)
    print(name)

    print("\nShape:")
    print(df.shape)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("="*60)