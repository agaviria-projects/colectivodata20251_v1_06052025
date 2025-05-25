import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("../../data/asistencia_estudiantes_completo.csv")
conteoEstadoMedioTransporte = df.groupby(['estado', 'medio_transporte']).size().unstack(fill_value=0)

colores = plt.cm.Set2.colors

plt.figure(figsize=(10,6))
conteoEstadoMedioTransporte.plot(
    kind='bar',
    figsize=(10,6),
    color=colores
)

plt.title("Registros por estado y medio de transporte")
plt.xlabel("Estados de asistencias")
plt.ylabel("Medio de transporte")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
os.makedirs("../../output", exist_ok=True)
plt.savefig("../../output/grafica_estado_vs_transporte.png")
plt.show()
plt.close("all")
