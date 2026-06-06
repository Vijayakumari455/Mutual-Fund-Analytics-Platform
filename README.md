# Mutual-Fund-Analytics-Platform
Mutual Fund Analytics Platform using Python, SQL, SQLite, ETL Pipelines, and Power BI Dashboards.

## Overview

The Mutual Fund Analytics Platform is an end-to-end data analytics solution developed as part of the Bluestock Fintech Capstone Project. The project integrates mutual fund data from multiple public sources, performs data processing through an ETL pipeline, calculates key financial and risk metrics, and delivers actionable insights through an interactive Power BI dashboard.

The platform enables efficient analysis of fund performance, investor behavior, industry trends, and risk-adjusted returns, supporting data-driven investment decision-making.

---

## Business Problem

The mutual fund ecosystem generates large volumes of data from various sources, making it challenging for investors and analysts to perform comprehensive performance evaluation and comparison.

This project addresses the following challenges:

* Fragmented mutual fund data across multiple platforms
* Limited visibility into fund performance and risk metrics
* Lack of centralized investor analytics
* Manual and time-consuming reporting processes
* Difficulty in benchmarking funds against market indices

---

## Project Objectives

* Develop an automated ETL pipeline for mutual fund datasets
* Design a structured relational database for analytics
* Perform Exploratory Data Analysis (EDA)
* Compute risk and performance metrics
* Analyze investor transaction behavior
* Build an interactive Power BI dashboard
* Generate meaningful business insights from financial data

---

## Technology Stack

| Category        | Technologies       |
| --------------- | ------------------ |
| Programming     | Python             |
| Data Processing | Pandas, NumPy      |
| Database        | SQLite, SQLAlchemy |
| Analytics       | Jupyter Notebook   |
| Visualization   | Power BI           |
| Version Control | Git, GitHub        |

---

## Data Sources

The project utilizes publicly available financial datasets from:

* AMFI India
* mfapi.in
* NSE India
* BSE India

### Datasets Used

* Fund Master Data
* NAV History
* Assets Under Management (AUM)
* SIP Inflow Data
* Category-wise Inflows
* Investor Transactions
* Portfolio Holdings
* Benchmark Indices

---

## System Architecture

```text
Data Sources
     │
     ▼
Data Extraction
     │
     ▼
Data Cleaning & Transformation
     │
     ▼
SQLite Database
     │
     ▼
Analytics & Performance Metrics
     │
     ▼
Power BI Dashboard
```

---

## Project Structure

```text
bluestock_mf_capstone
│
├── data
│   ├── raw
│   └── processed
│
├── notebooks
│   ├── Data Ingestion
│   ├── Data Cleaning
│   ├── EDA Analysis
│   ├── Performance Analytics
│   └── Advanced Analytics
│
├── sql
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard
│   └── Power BI Dashboard
│
├── reports
│   ├── Final Report
│   └── Presentation
│
├── README.md
└── requirements.txt
```

---

## Key Analytics Performed

### Exploratory Data Analysis

* NAV Trend Analysis
* AUM Growth Analysis
* SIP Inflow Trends
* Investor Demographics
* Geographic Distribution Analysis
* Correlation Analysis

### Performance Analytics

* CAGR
* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Maximum Drawdown

### Advanced Analytics

* Value at Risk (VaR)
* Conditional Value at Risk (CVaR)
* Rolling Sharpe Ratio
* Investor Cohort Analysis
* SIP Continuity Analysis
* Fund Recommendation Model
* Sector Concentration Analysis

---

## Dashboard Features

The Power BI dashboard consists of four interactive pages:

### 1. Industry Overview

* Total AUM
* SIP Inflows
* Folio Count
* Fund House Analysis

### 2. Fund Performance

* Risk vs Return Analysis
* Fund Ranking
* Benchmark Comparison
* Performance Metrics

### 3. Investor Analytics

* State-wise Investments
* Demographic Insights
* Transaction Trends

### 4. SIP & Market Trends

* SIP Growth Analysis
* Category-wise Inflows
* Market Trend Visualization

---

## Key Outcomes

* Built a complete ETL workflow for mutual fund analytics.
* Created a structured database for financial analysis.
* Generated risk-adjusted performance metrics.
* Developed an interactive business intelligence dashboard.
* Produced actionable insights for investment evaluation.

---

## Future Enhancements

* Real-time data integration
* Predictive analytics using Machine Learning
* Portfolio optimization models
* Streamlit-based web application
* Automated reporting and alerts

---

## Author

**Katuri Vijayakumari**
Data Analyst Intern
Bluestock Fintech Capstone Project
June 2026

