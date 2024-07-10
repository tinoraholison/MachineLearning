import numpy as np
import pandas as pd

# Exemple d'utilisation de numpy
matrice = np.random.randn(3, 4)
print(f"Ma matrice:\n {matrice}")

# Exemple d'utilisation de pandas
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}
print(pd.DataFrame(data))
