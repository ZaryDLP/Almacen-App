import pandas as pd

# Leer el archivo Excel
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
df = pd.read_excel(os.path.join(BASE_DIR, "Insumos.xlsx"))

# Mostrar todo el contenido
print(df)
