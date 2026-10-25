import pandas as pd 
import sqlite3

customers = pd.read_csv("customers.csv")
orders = pd.read_csv("orders.csv")

conn = sqlite3.connect("shop.db")

customers.to_sql("customers",conn, if_exists="replace", index=False)
orders.to_sql("orders",conn, if_exists="replace", index=False)

query = """SELECT c.name, c.city, sum(o.amount) AS Total
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.name, c.city"""

result = pd.read_sql(query,conn)
print(result)

conn.close()
