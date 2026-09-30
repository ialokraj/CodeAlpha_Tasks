stocks = {
    "AXIS": 1200,
    "WIPRO": 500,
    "HUL": 2500,
    "SBI": 800,
    "ITC": 450
}

portfolio = {}
total_investment = 0

print("Available stocks:")
for stock in stocks:
    print(stock, "₹", stocks[stock])

n = int(input("\nHow many different stocks do you want to buy? (Maximum 5): "))

if n < 1:
    print("Please select at least 1 stock.")
elif n > 5:
    print("Maximum 5 different stocks can be selected.")
else:
    for i in range(n):
        stock = input("\nEnter stock name: ").upper()

        if stock not in stocks:
            print("Stock not available. Please enter a valid stock.")
            continue

        if stock in portfolio:
            print("You have already selected this stock.")
            continue

        quantity = int(input("Enter quantity: "))

        value = stocks[stock] * quantity
        portfolio[stock] = quantity
        total_investment += value

    print("\n===== PORTFOLIO =====")

    for stock in portfolio:
        quantity = portfolio[stock]
        value = stocks[stock] * quantity
        print(stock, "Quantity:", quantity, "Value: ₹", value)

    print("\nTotal Investment: ₹", total_investment)

    save = input("\nDo you want to save the result? (yes/no): ").lower()

    if save == "yes":
        with open("portfolio.txt", "w") as file:
            file.write("STOCK PORTFOLIO\n")
            file.write("================\n")

            for stock in portfolio:
                quantity = portfolio[stock]
                value = stocks[stock] * quantity
                file.write(f"{stock} - Quantity: {quantity} - Value: ₹{value}\n")

            file.write(f"\nTotal Investment: ₹{total_investment}")

        print("Portfolio saved successfully.")