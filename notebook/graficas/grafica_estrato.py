import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("../../data/asistencia_estudiantes_completo.csv")
conteo = df["estrato"].value_counts().sort_index()

plt.figure(figsize=(6, 4))
conteo.plot(kind='bar', color="slateblue", edgecolor="black")
plt.title("Distribución por estrato socioeconómico")
plt.xlabel("Estrato")
plt.ylabel("Cantidad de estudiantes")
plt.xticks(rotation=0)
plt.tight_layout()
os.makedirs("../../output", exist_ok=True)
plt.savefig("../../output/grafica_estrato.png")
plt.show()
