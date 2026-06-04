import pandas as pd

# Leer el archivo Excel
df = pd.read_excel(archivo)

df.columns = df.columns.str.strip()
print("COLUMNAS:")
print(df.columns.tolist())
