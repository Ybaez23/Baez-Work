# Furniture.py - This program calculates profits and sales prices for a furniture company.

itemName = "TV Stand"
retailPrice = 325.00
wholesalePrice = 200.00

# Write your assignment statements here for profit, salePrice, and saleProfit

# Calculate profit
profit = retailPrice - wholesalePrice

# Calculate the sale price
salePrice = retailPrice * 0.75

# Calculate the profit
saleProfit = salePrice - wholesalePrice

print("Item Name: " + itemName)
print("Retail Price: $" + str(retailPrice))
print("Wholesale Price: $" + str(wholesalePrice))
print("Profit: $" + str(profit))
print("Sale Price: $" + str(salePrice))
print("Sale Profit: $" + str(saleProfit))
