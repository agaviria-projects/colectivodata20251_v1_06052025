import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("../../data/asistencia_estudiantes_completo.csv")
promedio = df.groupby("estado")["estrato"].mean()

plt.figure(figsize=(6, 4))
promedio.plot(kind='bar', color="coral", edgecolor="black")
plt.title("Promedio de estrato por estado de asistencia")
plt.xlabel("Estado")
plt.ylabel("Promedio de estrato")
plt.xticks(rotation=0)
plt.tight_layout()
os.makedirs("../../output", exist_ok=True)
plt.savefig("../../output/grafica_promedio_estrato_por_estado.png")
plt.show()
