import pandas as pd 
import numpy as np 

df = pd.read_csv("Messy.csv")
print(df)
print("\n")
print(df.isnull().sum())
print("\n")
print(df.duplicated().sum())
print("")
df = df.drop_duplicates()
df["price"] = df["price"].fillna(df["price"].mean())
df["quantity"] = df["quantity"].fillna(0)
df["category"] = df["category"].str.lower()
print(df)
df.to_csv("clean_products.csv", index = False)
