import pandas as pd
import numpy as np

data = {
    'ord_no': [70001.0, 5002.0, 5003.0, 70004.0, np.nan, 70005.0, 70010.0, 70003.0, 70012.0, np.nan, 70013.0],
    'purch_amt': [150.50, np.nan, 65.26, 110.50, 948.50, 2400.60, 5760.00, 1983.43, 2480.40, 75.29, 3045.60],
    'ord_date': ['2012-10-05', '2012-09-10', np.nan, '2012-08-17', '3 2min', '2012-07-27', '2012-09-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],
    'customer_id': [3002, 3001, 3001, 3003, 3002, 3001, 3004, 3003, 3002, 3001, 3001],
    'salesman_id': [5002.0, 5003.0, 3001, np.nan, 5002.0, 5001.0, np.nan, 5003.0, 5002.0, 3001, np.nan]
}

df = pd.DataFrame(data)
df['ord_no'].fillna(0, inplace=True)
df['purch_amt'].fillna(0, inplace=True)
df['ord_date'].fillna("Unknown", inplace=True)
df['customer_id'].fillna("Unknown", inplace=True)
df['salesman_id'] = df['salesman_id'].fillna(0).astype(int).astype(str)  # Convert to string
df['salesman_id'].replace('0', 'Unknown', inplace=True)  # Replace '0' with 'Unknown'
print(df)
