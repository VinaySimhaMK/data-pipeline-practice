import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

sns.set_theme()

df = pd.read_csv("products.csv")
df["Total"] = df["price"] * df["quantity"]

sns.barplot(data=df, x="item", y="price", hue = "category")
plt.title("Price of each item")
plt.show()
