import pandas as pd
data = pd.read_csv("sales.csv")
data["price_with_tax"] = data["price"] * 1.10
print(data)

data.to_csv("clean_sales.csv", index=False)
print("Saved clean_sales.csv")
