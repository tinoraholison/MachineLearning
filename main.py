import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# Exemple d'utilisation de numpy
matrice = np.random.randn(10, 10)
print(f"Ma matrice:\n {matrice}")

# Exemple d'utilisation de pandas
dataPandas = {'Name': ['Alice', 'Bob', 'Charlie', 'Tom'],
              'Age': [25, 30, 35, 18]}
print(pd.DataFrame(dataPandas))

# Création d'un heatmap
sns.heatmap(matrice)
plt.title('Exemple de Heatmap en utilisant la Matrice')
plt.show()
