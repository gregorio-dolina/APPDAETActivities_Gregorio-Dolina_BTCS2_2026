# Function 1: price change
def calculate_change(open_price, close_price):
    return close_price - open_price

# Function 2: percentage change
def calculate_percent_change(open_price, close_price):
    change = close_price - open_price
    return (change / open_price) * 100

# Function 3: market status
def get_market_status(change):
    if change > 0:
        return "GAIN"
    elif change < 0:
        return "LOSS"
    else:
        return "NO CHANGE"

# Function 4: Display stock summary
def display_summary(stock_name, open_price, close_price, change, percent_change, status):
    print()
    print("========== DAILY STOCK SUMMARY ==========")
    print("Stock:", stock_name)
    print("Price Change:", round(change, 2))
    print("Percent Change:", round(percent_change, 2), "%")
    print("Status:", status)
    print("==================================================")

# MAIN PROGRAM
print("STOCK ANALYZER")

stock_name = input("Enter stock name: ")
open_price = float(input("Enter opening price: "))
close_price = float(input("Enter closing price: "))

change = calculate_change(open_price, close_price)
percent_change = calculate_percent_change(open_price, close_price)
status = get_market_status(change)

display_summary(
    stock_name,
    open_price,
    close_price,
    change,
    percent_change,
    status
)