import csv
import os

# Hardcoded stock price dictionary (USD)
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 140.00,
    "MSFT": 400.00,
    "AMZN": 175.00,
    "NVDA": 120.00,
    "META": 490.00
}

def display_available_stocks():
    print("\n--- Available Stocks & Prices ---")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<6}: ${price:>7.2f}")
    print("-" * 33)

def run_portfolio_tracker():
    print("=" * 45)
    print("       STOCK PORTFOLIO TRACKER")
    print("=" * 45)

    display_available_stocks()

    portfolio = []

    while True:
        symbol = input("\nEnter stock symbol to add (or type 'done' to finish): ").strip().upper()
        if symbol == 'DONE':
            break

        if symbol not in STOCK_PRICES:
            print(f"'{symbol}' is not in the price list. Available: {', '.join(STOCK_PRICES.keys())}")
            continue

        qty_input = input(f"Enter quantity of {symbol} shares: ").strip()
        try:
            quantity = int(qty_input)
            if quantity <= 0:
                print("Quantity must be a positive integer.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid whole number for quantity.")
            continue

        unit_price = STOCK_PRICES[symbol]
        total_val = unit_price * quantity

        portfolio.append({
            "symbol": symbol,
            "quantity": quantity,
            "price": unit_price,
            "total": total_val
        })
        print(f"Added {quantity} shares of {symbol} (${total_val:.2f}) to your portfolio.")

    if not portfolio:
        print("\nNo stocks were added. Portfolio is empty.")
        return

    # Portfolio Summary Calculation
    print("\n" + "=" * 55)
    print("               PORTFOLIO SUMMARY")
    print("=" * 55)
    print(f"{'Stock':<8}{'Quantity':<12}{'Price/Share':<15}{'Total Value':<12}")
    print("-" * 55)

    total_portfolio_value = 0.0
    for item in portfolio:
        print(f"{item['symbol']:<8}{item['quantity']:<12}${item['price']:<14.2f}${item['total']:<11.2f}")
        total_portfolio_value += item['total']

    print("-" * 55)
    print(f"TOTAL INVESTMENT VALUE: ${total_portfolio_value:,.2f}")
    print("=" * 55)

    # Optional file export: save to CSV and TXT
    save_choice = input("\nDo you want to save this summary to a file? (txt/csv/none): ").strip().lower()

    if save_choice == "txt":
        filename = "portfolio_summary.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("PORTFOLIO SUMMARY\n")
            f.write("=" * 45 + "\n")
            for item in portfolio:
                f.write(f"{item['symbol']}: {item['quantity']} shares @ ${item['price']:.2f} = ${item['total']:.2f}\n")
            f.write("-" * 45 + "\n")
            f.write(f"Total Investment Value: ${total_portfolio_value:,.2f}\n")
        print(f">> Saved portfolio summary to '{os.path.abspath(filename)}'")

    elif save_choice == "csv":
        filename = "portfolio_summary.csv"
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock Symbol", "Quantity", "Price per Share (USD)", "Total Value (USD)"])
            for item in portfolio:
                writer.writerow([item["symbol"], item["quantity"], item["price"], item["total"]])
            writer.writerow([])
            writer.writerow(["TOTAL", "", "", total_portfolio_value])
        print(f">> Saved portfolio summary to '{os.path.abspath(filename)}'")
    else:
        print("Summary not saved to file.")

if __name__ == "__main__":
    run_portfolio_tracker()
