import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("../../data/asistencia_estudiantes_completo.csv")
df_junio = df[df["fecha"].str.contains("-04-")]
conteo = df_junio["estado"].value_counts()

plt.figure(figsize=(6, 4))
conteo.plot(kind='bar', color="gold", edgecolor="black")
plt.title("Estado de asistencia en abril")
plt.xlabel("Estado")
plt.ylabel("Cantidad")
plt.xticks(rotation=0)
plt.tight_layout()
os.makedirs("../../output", exist_ok=True)
plt.savefig("../../output/grafica_asistencia_abril.png")
plt.show()
