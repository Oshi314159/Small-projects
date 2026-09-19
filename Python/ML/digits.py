import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml

mnist = fetch_openml('mnist_784', version=1, as_frame=True)

X, y = mnist['data'], mnist['target']

plt.imshow(X.iloc[0].values.reshape(28, 28), cmap='gray')
plt.title(f'Label: {y.iloc[0]}')
plt.show()
