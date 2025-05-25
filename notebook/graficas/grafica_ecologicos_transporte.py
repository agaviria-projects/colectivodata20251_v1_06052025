import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("../../data/asistencia_estudiantes_completo.csv")
ecologicos = df[df["medio_transporte"].isin(["bicicleta", "a pie"])]
conteo = ecologicos["medio_transporte"].value_counts()

plt.figure(figsize=(6, 4))
conteo.plot(kind='bar', color=["green", "darkgreen"], edgecolor="black")
plt.title("Transporte ecológico: a pie y bicicleta")
plt.xlabel("Medio de transporte")
plt.ylabel("Cantidad")
plt.xticks(rotation=0)
plt.tight_layout()
os.makedirs("../../output", exist_ok=True)
plt.savefig("../../output/grafica_eco_transporte.png")
plt.show()
