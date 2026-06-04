peso_bruto = float(input("Peso bruto (g): "))
tara = float(input("Tara (g): "))
peso_unitario = float(input("Peso por unidad (g): "))

peso_neto = peso_bruto - tara
unidades = peso_neto / peso_unitario

print(f"\nPeso neto: {peso_neto:.2f} g")
print(f"Unidades estimadas: {round(unidades)}")