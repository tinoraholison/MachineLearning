import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# Exemple d'utilisation de numpy
matrice = np.random.randn(3, 4)
print(f"Ma matrice:\n {matrice}")

# Exemple d'utilisation de pandas
dataPandas = {'Name': ['Alice', 'Bob', 'Charlie'],
              'Age': [25, 30, 35]}
print(pd.DataFrame(dataPandas))

# Générateur random data
data = np.random.rand(10, 10)
# Création d'un heatmap
sns.heatmap(data)
plt.title('Exemple de Heatmap')
plt.show()
