import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_excel("../../data/usuarios_sistema_completo.xlsx")
conteo = df["tipo_usuario"].value_counts()

plt.figure(figsize=(6, 4))
conteo.plot(kind='bar', color=["#4daf4a", "#377eb8"], edgecolor="black")
plt.title("Cantidad de usuarios por tipo")
plt.xlabel("Tipo de usuario")
plt.ylabel("Cantidad")
plt.xticks(rotation=0)
for i, value in enumerate(conteo):
    plt.text(i, value + 5, str(value), ha='center', fontsize=10)
os.makedirs("../../output", exist_ok=True)
plt.tight_layout()
plt.savefig("../../output/grafica_tipo_usuario.png")
plt.show()
