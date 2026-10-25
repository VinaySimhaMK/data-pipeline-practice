items = ["pen","book","bag"]
prices = [10,50,200]
for i in range(3):
    print(items[i], "costs", prices[i])

print("")

for i in range(3):
    if prices[i] > 20:
        print(items[i], "is expensive")
    else:
        print(items[i], "is cheap")

print("")

def tax(price):
    return price*1.10

print(tax(100))
print(tax(50))

print("")

def rounded_tax(price):
    return round(price*1.10,2)

print(rounded_tax(100))
print(rounded_tax(50))

print("")

try:
    number = int("abc")
except:
    print("It's not a number")
print("Program continues")

print("")

try:
    data = open("no_such_file.csv")
except:
    print("File not found, skipping")

print("")

product = {"item":"pen","price":10}
print(product)
print(product["item"])
print(product["price"])

product["price"] = 12
print(product)

print("")

name = "pen"
cost = 10
print(f"The cost of {name} is {cost}")

print("")

