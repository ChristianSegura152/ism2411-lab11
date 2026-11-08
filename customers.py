# Reflection
#
# 1. I use brackets when a key must exist, so a missing one raises an error.
#    I use .get() when a key is optional, so the program keeps running with a
#    default.
#
# 2. It reminds me of a pivot table that totals sales by region. The Python
#    version handles huge datasets with the same loop and reruns instantly.
 
# -- Exercise 1 --
print("--- Exercise 1 ---")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}
 
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)
 
# -- Exercise 2 --
print("\n--- Exercise 2 ---")
customer["phone"] = "813-555-0142"
print(customer)
 
customer["tier"] = "platinum"
print(customer)
 
del customer["email"]
print(customer)
 
# -- Exercise 3 --
print("\n--- Exercise 3 ---")
print(customer.get("email", "no email on file"))
 
try:
    print(customer["email"])
except KeyError as error:
    print(f"KeyError caught: {error}")
 
# -- Exercise 4 --
print("\n--- Exercise 4 ---")
for key, value in customer.items():
    print(f"{key}: {value}")
 
for item in customer:
    print(item)
# Difference: looping over the dict without .items() only gives the keys,
# so I would have to look up each value myself. .items() gives each
# key and its value together as a pair.
 
# -- Exercise 5 --
print("\n--- Exercise 5 ---")
tier_discounts = {"bronze": 0, "silver": 0.05, "gold": 0.10, "platinum": 0.15}
purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)
 
print(f"Tier: {customer['tier']}")
print(f"Discount: {discount_rate * 100:.0f}%")
print(f"Final price: ${final_price:.2f}")
 
# -- Exercise 6 --
print("\n--- Exercise 6 ---")
customers = [
    {"name": "Bob", "tier": "gold", "ytd_spend": 3200},
    {"name": "Carol", "tier": "silver", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 450},
]
 
for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} discount on a $300 purchase")
 
# -- Exercise 7 --
print("\n--- Exercise 7 ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
 
for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} ({details['stock']} left)")
 
# -- Exercise 8 --
print("\n--- Exercise 8 ---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]
 
sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    sales_by_region[region] = sales_by_region.get(region, 0) + sale["amount"]
 
for region in sorted(sales_by_region):
    print(f"{region}: {sales_by_region[region]}")
 
