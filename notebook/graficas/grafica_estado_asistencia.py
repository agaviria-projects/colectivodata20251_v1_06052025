import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("../../data/asistencia_estudiantes_completo.csv")
conteo = df["estado"].value_counts()

plt.figure(figsize=(6, 4))
conteo.plot(kind='bar', color=["#66c2a5", "#fc8d62", "#8da0cb"], edgecolor="black")
plt.title("Estado de asistencia de los estudiantes")
plt.xlabel("Estado")
plt.ylabel("Cantidad")
plt.xticks(rotation=0)
for i, value in enumerate(conteo):
    plt.text(i, value + 5, str(value), ha='center')
os.makedirs("../../output", exist_ok=True)
plt.tight_layout()
plt.savefig("../../output/grafica_estado_asistencia.png")
plt.show()
