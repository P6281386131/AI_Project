import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

penguins = sns.load_dataset("penguins")

penguins_numeric = penguins.select_dtypes(include='number').dropna()

corr = penguins_numeric.corr()

print("=== Correlation Matrix ===")
print(corr)

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, fmt=".2f", cmap='plasma', square=True)
plt.title("Correlation Heatmap of Penguin Numerical Features")
plt.tight_layout()
plt.show()

corr_abs = corr.abs()
np.fill_diagonal(corr_abs.values, 0)  
max_idx = divmod(corr_abs.values.argmax(), corr_abs.shape[1])
var1 = corr_abs.index[max_idx[0]]
var2 = corr_abs.columns[max_idx[1]]
strong_corr = corr.loc[var1, var2]

print(f"\n=== Strongest Correlation Pair ===")
print(f"{var1} and {var2} → correlation = {strong_corr:.3f}")
