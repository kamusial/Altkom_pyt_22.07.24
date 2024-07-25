import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('iris.csv')
# print(df.class.value_counts())
print(df['class'].value_counts())

species = {
    'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2
}

df['class_values'] = df['class'].map(species)
print(df.describe())
print(df.head(3).to_string())

# moja probka
sample = np.array([5.6, 3.2, 5.2, 1.45])

sns.scatterplot(data=df, x='sepallength', y='sepalwidth', hue='class')
plt.scatter(5.6, 3.2, color='red')
plt.show()

sns.scatterplot(data=df, x='petallength', y='petalwidth', hue='class')
plt.scatter(5.2, 1.45, c='r')
plt.show()

df['distance'] = (df.sepallength-sample[0])**2 + (df.sepalwidth-sample[1])**2 +\
                 (df.petallength-sample[2])**2 + (df.petalwidth-sample[3])**2

print(df.sort_values('distance').to_string())

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

print('Teraz gotowy klasyfikator')
print('\nKNN')
X = df.iloc[:, :4]   # 4 pierwsze kolumny
y = df.class_values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = KNeighborsClassifier(n_neighbors=5, weights='distance')
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))

# jak liczba sąsiadow wpływa na jakosc rozwiązania
results = []
for k in range(1, 101):
    model = KNeighborsClassifier(n_neighbors=k) #, weights='distance')
    model.fit(X_train, y_train)
    results.append(model.score(X_test, y_test))

plt.plot(results)
plt.show()