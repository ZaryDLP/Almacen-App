import pandas as pd

df = pd.read_excel("Insumos.xlsx")
df.columns = df.columns.str.strip()

busqueda = input("Buscar producto: ")

resultado = df[
    df["ESPECIFICACIÓN"].str.contains(
        busqueda,
        case=False,
        na=False
    )
]

# Reinicia los índices para que empiecen en 0
resultado = resultado.reset_index(drop=True)

for i, fila in resultado.iterrows():
    print(f"{i} - {fila['ESPECIFICACIÓN']}")

opcion = int(input("\nSelecciona un número: "))

producto = resultado.iloc[opcion]

print("\nProducto seleccionado:")
print(producto["ESPECIFICACIÓN"])

print("Peso unitario:")
print(producto["PESO UNITARIO"])
peso_unitario = float(producto["PESO UNITARIO"])

peso_bruto = float(input("\nPeso bruto: "))
tara = float(input("Tara: "))

peso_neto = peso_bruto - tara
unidades = peso_neto / peso_unitario

print("\nRESULTADO")
print(f"Peso neto: {peso_neto}")
print(f"Unidades estimadas: {round(unidades)}")
