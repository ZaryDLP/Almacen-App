# Importa la librería Tkinter, que sirve para crear ventanas
import tkinter as tk


# Esta función se ejecuta cuando se presiona el botón "Calcular"
def calcular():

    # Obtiene el texto escrito en la caja "Peso bruto"
    # y lo convierte a número decimal
    peso_bruto = float(entry_bruto.get())

    # Obtiene el valor de la caja "Tara"
    tara = float(entry_tara.get())

    # Obtiene el valor de la caja "Peso por unidad"
    peso_unitario = float(entry_unitario.get())

    # Calcula el peso neto
    peso_neto = peso_bruto - tara

    # Calcula cuántas unidades hay
    unidades = peso_neto / peso_unitario

    # Cambia el texto de la etiqueta "resultado"
    resultado.config(
        text=f"Peso neto: {peso_neto:.2f} g\nUnidades: {round(unidades)}"
    )


# Crea la ventana principal
ventana = tk.Tk()

# Título que aparece en la barra superior
ventana.title("Calculadora de Insumos")


# --------------------------
# CAMPO PESO BRUTO
# --------------------------

# Crea un texto descriptivo
tk.Label(ventana, text="Peso bruto (g)").pack()

# Crea una caja de texto donde el usuario escribe
entry_bruto = tk.Entry(ventana)

# Coloca la caja en la ventana
entry_bruto.pack()


# --------------------------
# CAMPO TARA
# --------------------------

tk.Label(ventana, text="Tara (g)").pack()

entry_tara = tk.Entry(ventana)

entry_tara.pack()


# --------------------------
# CAMPO PESO UNITARIO
# --------------------------

tk.Label(ventana, text="Peso por unidad (g)").pack()

entry_unitario = tk.Entry(ventana)

entry_unitario.pack()


# --------------------------
# BOTÓN CALCULAR
# --------------------------

# Crea un botón
tk.Button(

    ventana,               # Ventana donde aparecerá

    text="Calcular",       # Texto que mostrará

    command=calcular       # Función que ejecutará al hacer clic

).pack(pady=10)


# --------------------------
# ETIQUETA RESULTADO
# --------------------------

# Espacio donde se mostrará el resultado
resultado = tk.Label(ventana, text="")

resultado.pack()


# --------------------------
# INICIA LA VENTANA
# --------------------------

# Mantiene la ventana abierta esperando acciones del usuario
ventana.mainloop()