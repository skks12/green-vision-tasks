def determine_profit_or_loss(cost_price, selling_price):
    if selling_price > cost_price:
        return "Profit", selling_price - cost_price
    elif cost_price > selling_price:
        return "Loss", cost_price - selling_price
    else:
        return "No Profit No Loss", 0

cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))
result, amount = determine_profit_or_loss(cost_price, selling_price)
print(f"It's a {result} of {amount:.2f}")
