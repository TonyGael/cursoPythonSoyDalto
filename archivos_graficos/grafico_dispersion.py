import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_graficos/dispersion.csv")

# creando el gráfico
sns.scatterplot(x="tiempo", y="dinero", data=df)

# mostrando el gráfico
plt.show()
