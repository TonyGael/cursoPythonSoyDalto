import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_graficos/bigotes.csv")

# creando el gráfico
sns.boxplot(x="categoria", y="valor", data=df)

# mostrando el gráfico
plt.show()
