import pandas as pd 

customers = pd.read_csv("customers.csv")
orders = pd.read_csv("orders.csv")

inner = pd.merge(orders, customers, on = "customer_id", how = "inner")
print(inner)

left = pd.merge(orders, customers, on = "customer_id", how = "left")
print(left)

right = pd.merge(orders, customers, on = "customer_id", how = "right")
print(right)

print(inner.groupby("city")["amount"].sum())
