from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

archivo_excel = os.path.join(BASE_DIR, "Insumos.xlsx")

df = pd.read_excel(archivo_excel)
df.columns = df.columns.str.strip()

print("COLUMNAS:")
print(df.columns.tolist())

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/buscar")
def buscar():
    q = request.args.get("q", "")

    filtrado = df[
        df["ESPECIFICACIÓN"].str.contains(q, case=False, na=False)
    ][["ESPECIFICACIÓN", "PESO UNITARIO"]]

    return jsonify(filtrado.to_dict(orient="records"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)