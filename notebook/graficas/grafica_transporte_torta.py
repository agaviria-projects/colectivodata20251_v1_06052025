import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Leer datos
dataFrameAsistencia = pd.read_csv("../../data/asistencia_estudiantes_completo.csv")

# Conteo de medios de transporte
conteoTransporte = dataFrameAsistencia['medio_transporte'].value_counts()

# Crear figura
plt.figure(figsize=(5, 5))
plt.pie(
    conteoTransporte,
    labels=conteoTransporte.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=sns.color_palette("Blues")
)

plt.title("Distribución por medio de transporte")
plt.tight_layout()

# Guardar imagen
os.makedirs("../../output", exist_ok=True)
plt.savefig("../../output/grafica_transporte_torta.png")
plt.show()
plt.close()
