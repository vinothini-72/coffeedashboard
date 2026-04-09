import pandas as pd
import numpy as np

df = pd.read_excel(r"C:\Users\user\Documents\day1project.xlsx")

# create total sales column
df["Total Sales"] = df["Quantity"] * df["Price"]

print(df.head())

# numpy calculations
print("Total:", np.sum(df["Total Sales"]))
print("Average:", np.mean(df["Total Sales"]))
print("Max:", np.max(df["Total Sales"]))

coffee_sales = df.groupby("Coffee_type")["Total Sales"].sum()
print("\nSales by Coffee Type")
print(coffee_sales)

city_sales = df.groupby("City")["Total Sales"].sum()
print("\nSales by City")
print(city_sales)


# save for power bi
df.to_excel("coffee_sales_cleaned.xlsx", index=False)