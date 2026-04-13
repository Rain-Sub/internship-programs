import pandas as pd
import matplotlib.pyplot as plt


data = {
    "Date": pd.date_range(start="2024-01-01", periods=10, freq='D'),
    "Revenue": [200, 340, 300, 500, 700, 650, 800, 750, 900, 1000],
    "Age_Group": ["18-25", "26-35", "18-25", "36-45", "26-35", "18-25", "36-45", "26-35", "18-25", "36-45"],
    "Gender": ["Male", "Female", "Female", "Male", "Female", "Male", "Male", "Female", "Female", "Male"],
    "Purchase_Amount": [50, 80, 60, 120, 200, 150, 220, 180, 160, 250]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(df["Date"], df["Revenue"], marker='o')
plt.title("Revenue Trend")
plt.xticks(rotation=45)

plt.subplot(2, 2, 2)
df["Age_Group"].value_counts().plot(kind='bar')
plt.title("Customer Age Distribution")

plt.subplot(2, 2, 3)
df["Gender"].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Gender Distribution")


plt.subplot(2, 2, 4)
plt.scatter(df["Age_Group"], df["Purchase_Amount"])
plt.title("Purchase Behavior by Age Group")

plt.tight_layout()
plt.show()