# Inventory Alert System
import pandas as pd

# Load dataset (sample: inventory_data.xlsx with Item, Quantity)
inventory = pd.read_excel('inventory_data.xlsx')

# Threshold
threshold = 10

# Find items below threshold
alerts = inventory[inventory['Quantity'] < threshold]

if not alerts.empty:
    print("⚠️ Items below threshold:")
    for _, row in alerts.iterrows():
        print(f"- {row['Item']} (Quantity: {row['Quantity']})")
else:
    print("All items are sufficiently stocked.")

# Save low-stock items for review
alerts.to_excel('low_stock_alerts.xlsx', index=False)
print("Low stock items saved to low_stock_alerts.xlsx")
