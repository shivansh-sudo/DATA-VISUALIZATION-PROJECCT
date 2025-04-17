import yfinance as yf
import pandas as pd

# Choose stock (AAPL = Apple)
ticker = 'AAPL'

# Download last 7 days of daily data
data = yf.download(ticker, period='7d', interval='1d')

# Save to CSV
data.to_csv('stock_data.csv')

print(" Stock data saved to stock_data.csv")
