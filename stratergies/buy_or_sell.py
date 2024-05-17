import pandas as pd
import matplotlib.pyplot as plt
import SMA
import points_of_intersection as POI

# Example data loading (this will depend on your data source)
data = pd.read_csv('dataset.csv')
close_prices = data['Close']

# Parameters
sma_window = 20

# Calculate SMA
sma = SMA.calculate_sma(close_prices, sma_window)

# Find Buy/Sell Points
signals = POI.find_intersections(close_prices, sma)

# Visualize the data with buy/sell signals
plt.figure(figsize=(14, 7))
plt.plot(close_prices, label='Close Prices')
plt.plot(sma, label=f'SMA {sma_window} days', alpha=0.7)

# Plot buy and sell signals
for signal in signals:
    if signal[1] == 'buy':
        plt.plot(signal[0], close_prices[signal[0]], 'g^', markersize=10, label='Buy Signal')
    else:
        plt.plot(signal[0], close_prices[signal[0]], 'rv', markersize=10, label='Sell Signal')

plt.legend()
plt.show()
