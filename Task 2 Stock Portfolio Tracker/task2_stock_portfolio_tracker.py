# ============================================================
# TASK 2: Stock Portfolio Tracker
# Intern   : Isra Asif  |  ID: CA/DF1/54477
# Internship: CodeAlpha — Python Programming (May 2026)
# ============================================================

import csv
import os
from datetime import date

# ---------- 1. Hardcoded stock prices (USD) -----------------
STOCK_PRICES = {
    "AAPL":  182.50,   # Apple
    "TSLA":  250.00,   # Tesla
    "GOOGL": 175.30,   # Google
    "AMZN":  190.40,   # Amazon
    "MSFT":  420.10,   # Microsoft
    "META":  510.60,   # Meta
    "NFLX":  635.20,   # Netflix
    "NVDA":  875.00,   # NVIDIA
}


# ---------- 2. Display available stocks ---------------------
def show_available_stocks() -> None:
    print("\n  Available Stocks:")
    print("  " + "-" * 30)
    print(f"  {'Symbol':<8} {'Company':<12} {'Price (USD)':>12}")
    print("  " + "-" * 30)
    names = {
        "AAPL": "Apple", "TSLA": "Tesla", "GOOGL": "Google",
        "AMZN": "Amazon", "MSFT": "Microsoft", "META": "Meta",
        "NFLX": "Netflix", "NVDA": "NVIDIA"
    }
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<8} {names[symbol]:<12} ${price:>11,.2f}")
    print("  " + "-" * 30 + "\n")


# ---------- 3. Get portfolio from user ----------------------
def get_portfolio() -> dict:
    portfolio = {}
    print("  Enter stock symbol and quantity (type 'done' to finish).\n")

    while True:
        symbol = input("  Stock symbol (or 'done'): ").strip().upper()

        if symbol == "DONE":
            if not portfolio:
                print("  ⚠  Please add at least one stock.\n")
                continue
            break

        if symbol not in STOCK_PRICES:
            print(f"  ⚠  '{symbol}' not found. Choose from the list above.\n")
            continue

        try:
            qty = int(input(f"  Quantity of {symbol}: ").strip())
            if qty <= 0:
                print("  ⚠  Quantity must be a positive number.\n")
                continue
        except ValueError:
            print("  ⚠  Please enter a valid whole number.\n")
            continue

        if symbol in portfolio:
            portfolio[symbol] += qty
            print(f"  ✅  Updated {symbol}: total {portfolio[symbol]} shares.\n")
        else:
            portfolio[symbol] = qty
            print(f"  ✅  Added {symbol} x{qty}.\n")

    return portfolio


# ---------- 4. Calculate & display results ------------------
def display_results(portfolio: dict) -> list:
    rows = []
    total = 0.0

    print("\n" + "=" * 50)
    print("         📊  YOUR STOCK PORTFOLIO SUMMARY")
    print("=" * 50)
    print(f"  {'Symbol':<8} {'Qty':>5}  {'Price':>10}  {'Value':>12}")
    print("  " + "-" * 42)

    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        total += value
        print(f"  {symbol:<8} {qty:>5}  ${price:>9,.2f}  ${value:>11,.2f}")
        rows.append({"Symbol": symbol, "Quantity": qty,
                     "Price (USD)": price, "Total Value (USD)": value})

    print("  " + "-" * 42)
    print(f"  {'TOTAL INVESTMENT':>36}  ${total:>11,.2f}")
    print("=" * 50 + "\n")

    return rows, total


# ---------- 5. Save to CSV ----------------------------------
def save_to_csv(rows: list, total: float) -> None:
    filename = f"portfolio_{date.today()}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["Symbol", "Quantity", "Price (USD)", "Total Value (USD)"])
        writer.writeheader()
        writer.writerows(rows)
        writer.writerow({})   # blank separator
        writer.writerow({"Symbol": "TOTAL", "Quantity": "",
                         "Price (USD)": "", "Total Value (USD)": total})
    print(f"  💾  Portfolio saved to '{filename}'\n")


# ---------- 6. Save to TXT ----------------------------------
def save_to_txt(rows: list, total: float) -> None:
    filename = f"portfolio_{date.today()}.txt"
    with open(filename, "w") as f:
        f.write("STOCK PORTFOLIO SUMMARY\n")
        f.write(f"Date: {date.today()}\n")
        f.write("=" * 45 + "\n")
        f.write(f"{'Symbol':<8} {'Qty':>5}  {'Price':>10}  {'Value':>12}\n")
        f.write("-" * 45 + "\n")
        for row in rows:
            f.write(f"{row['Symbol']:<8} {row['Quantity']:>5}  "
                    f"${row['Price (USD)']:>9,.2f}  "
                    f"${row['Total Value (USD)']:>11,.2f}\n")
        f.write("-" * 45 + "\n")
        f.write(f"{'TOTAL':>36}  ${total:>11,.2f}\n")
    print(f"  💾  Portfolio saved to '{filename}'\n")


# ---------- 7. Main -----------------------------------------
def main() -> None:
    print("\n" + "=" * 50)
    print("    📈  WELCOME TO STOCK PORTFOLIO TRACKER")
    print("=" * 50)

    show_available_stocks()
    portfolio = get_portfolio()
    rows, total = display_results(portfolio)

    # Ask to save
    save = input("  Save results? (csv / txt / both / no): ").strip().lower()
    if save in ("csv", "both"):
        save_to_csv(rows, total)
    if save in ("txt", "both"):
        save_to_txt(rows, total)

    print("  Thank you for using Stock Portfolio Tracker! 👋\n")


if __name__ == "__main__":
    main()
