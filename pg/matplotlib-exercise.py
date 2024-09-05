import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a sample dataset
np.random.seed(0)
dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
data = np.random.randn(len(dates)).cumsum()

# Create a DataFrame
df = pd.DataFrame({'Date': dates, 'Value': data})

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Value'])
plt.title('Sample Time Series Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)

# Add some annotations
max_value = df['Value'].max()
max_date = df.loc[df['Value'].idxmax(), 'Date']
plt.annotate(f'Max: {max_value:.2f}', xy=(max_date, max_value), xytext=(10, 10),
             textcoords='offset points', ha='left', va='bottom',
             bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

plt.tight_layout()
plt.show()

# Create a histogram
plt.figure(figsize=(10, 6))
plt.hist(df['Value'], bins=30, edgecolor='black')
plt.title('Distribution of Values')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()
