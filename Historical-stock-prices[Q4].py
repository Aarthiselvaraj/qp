import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('GOOG.csv')  


df['Date'] = pd.to_datetime(df['Date'], dayfirst=True) 


start_date = '2023-01-01'
end_date = '2024-01-01'


filtered_data = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]


plt.figure(figsize=(10, 6))
plt.plot(filtered_data['Date'], filtered_data['Close'],
         marker='o', linestyle='-')
plt.title('Historical Stock Prices of Alphabet Inc. between {} and {}'
          .format(start_date, end_date))
plt.xlabel('Date')
plt.ylabel('Closing Price ($)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
