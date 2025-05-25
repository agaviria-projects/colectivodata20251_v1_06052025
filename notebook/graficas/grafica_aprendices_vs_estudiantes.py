import pandas as pd
import matplotlib.pyplot as plt
import os

# Cargar los datos desde la carpeta data
df = pd.read_excel("../../data/usuarios_sistema_completo.xlsx")

# Filtrar aprendices y estudiantes
aprendices = df[df["tipo_usuario"] == "aprendiz"]
estudiantes = df[df["tipo_usuario"] == "estudiante"]

# Contar cuántos hay de cada tipo
conteo = {
    "Aprendices": len(aprendices),
    "Estudiantes": len(estudiantes)
}

# Crear la gráfica
plt.bar(conteo.keys(), conteo.values(), color=["skyblue", "orange"])
plt.title("Cantidad de Aprendices vs Estudiantes")
plt.xlabel("Tipo de usuario")
plt.ylabel("Cantidad")
plt.tight_layout()

# Crear carpeta output si no existe
os.makedirs("../../output", exist_ok=True)

# Guardar la imagen
plt.savefig("../../output/grafica_aprendices_estudiantes.png")
plt.show()
