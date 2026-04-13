import numpy as np

# -----------------------------
# 1. Create Sales Dataset
# -----------------------------
# Rows = Products (5)
# Columns = Months (12)

sales = np.array([
    [120, 130, 125, 140, 150, 160, 170, 180, 175, 190, 200, 210],  # Product 1
    [100, 110, 105, 115, 120, 125, 130, 135, 140, 145, 150, 155],  # Product 2
    [90, 95, 100, 105, 110, 115, 120, 118, 117, 119, 121, 123],    # Product 3
    [200, 195, 190, 185, 180, 175, 170, 168, 165, 160, 158, 155],  # Product 4
    [150, 155, 160, 158, 162, 165, 170, 175, 180, 185, 190, 195]   # Product 5
])

print("Sales Matrix (Products × Months):\n", sales)

# -----------------------------
# 2. Sales Analysis
# -----------------------------

# Total yearly sales for each product
yearly_sales_per_product = np.sum(sales, axis=1)
print("\nTotal Yearly Sales per Product:")
print(yearly_sales_per_product)

# Monthly total sales
monthly_total_sales = np.sum(sales, axis=0)
print("\nMonthly Total Sales:")
print(monthly_total_sales)

# Best-selling product
best_product_index = np.argmax(yearly_sales_per_product)
print("\nBest Selling Product: Product", best_product_index + 1)

# Best sales month
best_month_index = np.argmax(monthly_total_sales)
print("Best Sales Month:", best_month_index + 1)

# -----------------------------
# 3. Statistical Analysis
# -----------------------------

# Mean sales per product
mean_sales = np.mean(sales, axis=1)
print("\nMean Sales per Product:")
print(mean_sales)

# Standard deviation
std_sales = np.std(sales, axis=1)
print("\nStandard Deviation per Product:")
print(std_sales)

# Growth percentage between months
monthly_growth = np.diff(monthly_total_sales) / monthly_total_sales[:-1] * 100
print("\nMonthly Growth Percentage:")
print(monthly_growth)

# -----------------------------
# 4. Business Insights
# -----------------------------

# Identify products with declining sales (negative overall trend)
declining_products = []
for i in range(len(sales)):
    if sales[i, -1] < sales[i, 0]:
        declining_products.append(i + 1)

print("\nProducts with Declining Sales:", declining_products)

# Top 3 sales months
top3_months = np.argsort(monthly_total_sales)[-3:][::-1] + 1
print("Top 3 Sales Months:", top3_months)

# Predict next month sales using average growth
avg_growth = np.mean(monthly_growth) / 100
predicted_next_month_sales = monthly_total_sales[-1] * (1 + avg_growth)

print("\nPredicted Next Month Sales:", round(predicted_next_month_sales, 2))