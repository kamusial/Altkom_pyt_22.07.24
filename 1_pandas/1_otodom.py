import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('otodom.csv')
print(df)

print(df.describe().T.to_string())
print(df.iloc[1:5, 2:4])
print(df.describe().T.loc['price', '25%'])
print(df.iloc[:, 1:].corr())

