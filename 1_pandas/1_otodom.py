import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('otodom.csv')
print(df)

print(df.describe().T.to_string())


