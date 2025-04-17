import pandas as pd
import matplotlib.pyplot as plt

# Load CSV and skip the first two rows which might contain irrelevant data
df = pd.read_csv('stock_data.csv', skiprows=2)

# Manually set the column names
df.columns = ['Date', 'Price', 'Close', 'High', 'Low', 'Volume']

# Preview the cleaned columns
print("=== Columns ===")
print(df.columns)

# Clean the 'Close' column and convert to numeric
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
df.dropna(subset=['Close'], inplace=True)

# Moving average
df['MA'] = df['Close'].rolling(window=3).mean()

# Plot the data
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Close'], label='Close Price')
plt.plot(df['Date'], df['MA'], label='3-day Moving Average')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock Price & Moving Average')
plt.legend()
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
