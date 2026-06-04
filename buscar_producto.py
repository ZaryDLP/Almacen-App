import pandas as pd

# Leer Excel
df = pd.read_excel("Insumos.xlsx")

# Pedir nombre al usuario
producto = input("Escribe el nombre del producto: ")

# Buscar coincidencias
resultado = df[df["ESPECIFICACIÓN"].str.contains(producto, case=False, na=False)]

print(resultado)
