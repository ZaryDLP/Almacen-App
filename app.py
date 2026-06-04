from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

df = pd.read_excel("Insumos.xlsx")
df.columns = df.columns.str.strip()

@app.route("/")
def home():
    return render_template("index.html")

# 🔍 API para autocomplete
@app.route("/buscar")
def buscar():
    q = request.args.get("q", "")

    filtrado = df[
        df["ESPECIFICACIÓN"].str.contains(q, case=False, na=False)
    ][["ESPECIFICACIÓN", "PESO UNITARIO"]]

    return jsonify(filtrado.to_dict(orient="records"))


if __name__ == "__main__":
    app.run(debug=True)
    import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)