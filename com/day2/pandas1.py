import pandas as pd

d = {'col1': [1, 2], 'col2': [3, 4]}


df = pd.DataFrame(d)

print df.head()
import numpy as np


df1 = pd.read_csv('D:\Support\snowflakedata\Customer\Customer3.txt')
grouped =  df1.groupby('StoreID')
print(grouped.agg(np.size))