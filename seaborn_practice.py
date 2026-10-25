import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

sns.set_theme()

df = pd.read_csv("products.csv")
df["Total"] = df["price"] * df["quantity"]

sns.barplot(data=df, x="category", y="Total", estimator=sum, errorbar=None)
plt.title("Total sales by category")
plt.savefig("seaborn_category.png")
plt.show()  

sns.barplot(data=df, x="item", y="price")
plt.title("Price of each item")
plt.savefig("seaborn_items.png")
plt.show()