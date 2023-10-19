import pymongo
import pandas as pd
# import matplotlib.pyplot as plt
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient(
    'mongodb+srv://nadun:nadun2001@cluster0.lemvb4s.mongodb.net/')
db = client['Advizor']
collection = db['HouseSale_Advertisement']

# Query data from MongoDB
data = list(collection.find({}))

# Convert data to a pandas DataFrame
df = pd.DataFrame(data)

# Set the date as the index
df['Posted_Date'] = pd.to_datetime(df['Posted_Date'])
df.set_index('Posted_Date', inplace=True)

# Calculate the moving average
window_size = 5  # Define the window size for the moving average
df['Price'] = df['Price'].rolling(window=window_size).mean()

# Perform forecast for future time points
future_time_points = 35  # Define the number of future time points to forecast
last_date = df.index[-1]

# Generating future date range
future_dates = pd.date_range(
    start=last_date, periods=future_time_points, freq='W')

# Create a new DataFrame for the future dates
future_df = pd.DataFrame(index=future_dates, columns=df.columns)

# Set initial values for future data
future_df['Price'] = df['Price'].iloc[-1]

# Combine current and future data
combined_df = pd.concat([df, future_df])

# Perform forecasting for the future time points
for i in range(len(future_df)):
    # Adjust the increment as needed
    combined_df['Price'].iloc[len(
        df) + i] = combined_df['Price'].iloc[len(df) + i - 1] + 100000

# Plot the forecasted prices
# plt.figure(figsize=(12, 6))
# combined_df['Price'].plot(label='Forecasted Prices', linestyle='dashed')
# plt.title('House Prices Forecast for the Next 5 Weeks')
# plt.xlabel('Date')
# plt.ylabel('Price')
# plt.legend()
# plt.grid(True)
# plt.show()
