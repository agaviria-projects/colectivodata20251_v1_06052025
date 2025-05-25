import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("../../data/asistencia_estudiantes_completo.csv")
conteo = df["medio_transporte"].value_counts()

plt.figure(figsize=(8, 5))
conteo.plot(kind='barh', color="teal", edgecolor="black")
plt.title("Medios de transporte más utilizados")
plt.xlabel("Cantidad de estudiantes")
plt.ylabel("Medio de transporte")
plt.tight_layout()
os.makedirs("../../output", exist_ok=True)
plt.savefig("../../output/grafica_transporte.png")
plt.show()
