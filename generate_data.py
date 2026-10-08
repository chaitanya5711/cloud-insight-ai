import pandas as pd
import random
from datetime import datetime

# Make results reproducible
random.seed(42)

# Number of records
num_rows = 5000

# Data options
products = [
    "Laptop",
    "Desktop",
    "Monitor",
    "Keyboard",
    "Mouse",
    "Headphones",
    "Printer",
    "Tablet",
    "Webcam",
    "Smartphone"
]

categories = {
    "Laptop": "Electronics",
    "Desktop": "Electronics",
    "Monitor": "Electronics",
    "Keyboard": "Accessories",
    "Mouse": "Accessories",
    "Headphones": "Accessories",
    "Printer": "Office Equipment",
    "Tablet": "Electronics",
    "Webcam": "Accessories",
    "Smartphone": "Electronics"
}

regions = ["North", "South", "East", "West"]

channels = [
    "Online",
    "Retail",
    "Distributor"
]

# Price ranges for products
price_ranges = {
    "Laptop": (50000, 120000),
    "Desktop": (40000, 90000),
    "Monitor": (10000, 40000),
    "Keyboard": (800, 5000),
    "Mouse": (400, 3000),
    "Headphones": (1000, 10000),
    "Printer": (8000, 35000),
    "Tablet": (15000, 60000),
    "Webcam": (1500, 12000),
    "Smartphone": (15000, 100000)
}

# Date range
dates = pd.date_range(
    start="2025-01-01",
    end="2026-09-30",
    periods=num_rows
)

data = []

for i in range(num_rows):

    product = random.choice(products)
    category = categories[product]

    quantity = random.randint(1, 9)

    unit_price = random.randint(
        price_ranges[product][0],
        price_ranges[product][1]
    )

    discount = round(random.uniform(0, 0.15), 2)

    sales = quantity * unit_price * (1 - discount)

    profit_margin = random.uniform(0.08, 0.25)

    profit = sales * profit_margin

    row = {
        "Date": dates[i].strftime("%Y-%m-%d"),
        "Order_ID": f"ORD-{10000 + i}",
        "Customer_ID": f"CUST-{random.randint(1000, 1499)}",
        "Product": product,
        "Category": category,
        "Region": random.choice(regions),
        "Channel": random.choice(channels),
        "Quantity": quantity,
        "Unit_Price": unit_price,
        "Discount": discount,
        "Sales": round(sales, 2),
        "Profit": round(profit, 2)
    }

    data.append(row)

# Create DataFrame
df = pd.DataFrame(data)

# Save CSV
df.to_csv("data/sales_data.csv", index=False)

print("Sales dataset generated successfully!")
print(f"Total records: {len(df)}")
print("File saved to: data/sales_data.csv")
print("\nFirst 5 records:")
print(df.head())