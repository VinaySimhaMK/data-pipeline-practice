import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("products.csv")
df["Total"] = df["price"] * df["quantity"]

totals = df.groupby("category")["Total"].sum()

totals.plot(kind="bar")
plt.title("Total Sales by Category")
plt.ylabel("Total")
plt.savefig("Sales_chart.png")
plt.show()