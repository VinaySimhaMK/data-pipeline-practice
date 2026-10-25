import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("products.csv")
# df["Total"] = df["price"] * df["quantity"]

totals = df.groupby("category")["quantity"].sum()

totals.plot(kind="pie")
plt.title("Total Quantity by Category")
plt.xlabel("Quantity")
plt.savefig("Quantity_chart.png")
plt.show()