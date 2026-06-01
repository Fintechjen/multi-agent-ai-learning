from tools import get_stock_price

ticker = input("Ticker: ")

price = get_stock_price(ticker)

print(f"{ticker.upper()} price: {price}")

