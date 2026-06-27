import pandas as pd
import numpy as np
import sqlite3


sales = pd.read_csv("data/sales_data.csv")
products = pd.read_csv("data/products.csv")
stores = pd.read_csv("data/stores.csv")
print(sales)


print("\nFirst 5 Rows of Sales Data")
print(sales.head())


print("\nFirst 5 Rows of Products Data")
print(products.head())

print("\nFirst 5 Rows of Stores Data")
print(stores.head())

print("\nSales Shape :", sales.shape)
print("Products Shape :", products.shape)
print("Stores Shape :", stores.shape)


print("\nMissing Values in Sales Data")
print(sales.isnull().sum())






#Task 2
# print("\nDuplicate Rows =", sales.duplicated().sum())

# sales = sales.drop_duplicates()

# print("Shape after removing duplicates :", sales.shape)




# sales["quantity"] = sales["quantity"].fillna(0)

# sales = sales.dropna(subset=["amount"])

# print("\nMissing Values After Cleaning")
# print(sales.isnull().sum())

# print("\nShape After Cleaning :", sales.shape)


# -----------------------------
# Task 2 : Data Cleaning
# -----------------------------

# Check duplicate rows (ignoring sale_id)

















# ---------------- TASK 2 : Data Cleaning ----------------

print("\nDuplicate Rows =", sales.duplicated().sum())

# Remove complete duplicate rows (sale_id bhi check hoga)
sales = sales.drop_duplicates()

print("Shape after removing duplicates :", sales.shape)

# Fill missing quantity with 0
sales["quantity"] = sales["quantity"].fillna(0)

# Remove rows where amount is missing
sales = sales.dropna(subset=["amount"])

print("\nMissing Values After Cleaning")
print(sales.isnull().sum())

print("\nShape After Cleaning :", sales.shape)

















###################

# -----------------------------
# Task 3 : Data Transformation
# -----------------------------

# Merge sales with products
merged_data = pd.merge(
    sales,
    products,
    on="product_id",
    how="inner"
)

print("\nSales + Products Merged")
print(merged_data.head())

# Merge with stores
merged_data = pd.merge(
    merged_data,
    stores,
    on="store_id",
    how="inner"
)

print("\nFinal Merged Data")
print(merged_data.head())

print("\nFinal Shape :", merged_data.shape)

# Create Total Revenue Column
merged_data["total_revenue"] = merged_data["quantity"] * merged_data["price"]

print("\nData with Total Revenue")
print(merged_data.head())



# -----------------------------
# Task 4 : NumPy Calculations
# -----------------------------

average_revenue = np.mean(merged_data["total_revenue"])
maximum_revenue = np.max(merged_data["total_revenue"])
minimum_revenue = np.min(merged_data["total_revenue"])

print("\nAverage Revenue :", average_revenue)
print("Maximum Revenue :", maximum_revenue)
print("Minimum Revenue :", minimum_revenue)



# -----------------------------
# STEP 5 : LOAD DATA INTO SQLITE
# -----------------------------

conn = sqlite3.connect("output/retailmart.db")

merged_data.to_sql(
    "sales_report",
    conn,
    if_exists="replace",
    index=False
)

print("\nData Loaded Successfully into SQLite Database!")

conn.close()







# -----------------------------
# STEP 6 : RUN SQL QUERIES
# -----------------------------

conn = sqlite3.connect("output/retailmart.db")

query = """
SELECT
    store_name,
    SUM(total_revenue) AS Total_Revenue
FROM sales_report
GROUP BY store_name
ORDER BY Total_Revenue DESC;
"""

result = pd.read_sql(query, conn)

print("\nRevenue by Store")
print(result)

conn.close()




# -----------------------------
# STEP 7 : EXPORT FINAL DATA
# -----------------------------

merged_data.to_csv("output/final_sales_report.csv", index=False)

print("\nFinal CSV Exported Successfully!")






