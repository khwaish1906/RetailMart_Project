# RetailMart Data Engineering Project

# Overview
This project is an end-to-end ETL (Extract, Transform, Load) pipeline developed for RetailMart Pvt. Ltd. The pipeline collects raw sales data from multiple CSV files, cleans and transforms the data, and loads it into a SQLite database for analysis and reporting.

# Features
- Load data from multiple CSV files.
- Detect and handle missing values.
- Remove duplicate records.
- Merge datasets using Pandas.
- Calculate total revenue.
- Generate city-wise revenue reports.
- Store processed data in SQLite database.
- Perform SQL-based analysis and reporting.

# Technologies Used
- Python
- Pandas
- NumPy
- SQLite
- SQL

# Project Structure

RetailMart_Project/
│
├── data/
│ ├── sales_data.csv
│ ├── products.csv
│ └── stores.csv
│
├── output/
│ └── retailmart.db
│
├── pipeline.py
├── requirements.txt
└── README.md

# How to Run
1. Install required libraries:
   pip install -r requirements.txt

2. Run the pipeline:
   python pipeline.py

# Key Insights Generated
- Total revenue generated per city
- Top 3 best-selling products
- Total revenue per store per day
- Total transactions processed

