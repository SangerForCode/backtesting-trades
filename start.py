import yfinance as yf

import plotly.graph_objects as go

# Download historical data for a stock (e.g., Apple)
df = yf.download("AAPL", auto_adjust=True)

# Select relevant columns
df = df[["Open", "High", "Low", "Close", "Volume"]]

# Reset the index so 'Date' becomes a column
df = df.reset_index()

# Generate a candlestick chart
fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close']
)])

# Show the chart
fig.show()