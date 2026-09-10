import pandas as pd

df = pd.read_csv("data/monthly_finance.csv")

df["Profit"] = df["Revenue"] - df["Costs"]
df["Profit Margin %"] = ((df["Profit"] / df["Revenue"]) * 100).round(2)

print(df)

total_revenue = df["Revenue"].sum()

print("Total Revenue:", total_revenue)

total_costs = df["Costs"].sum()

print("Total Costs:", total_costs)

total_profit = df["Profit"].sum()

print("Total Profit:", total_profit)

annual_profit_margin = (total_profit / total_revenue) * 100

print("Annual Profit Margin:", round(annual_profit_margin, 2), "%")

best_month = df.loc[df["Profit"].idxmax()]

print("Best Month:", best_month["Month"])

worst_month = df.loc[df["Profit"].idxmin()]

print("Worst Month:", worst_month["Month"])
