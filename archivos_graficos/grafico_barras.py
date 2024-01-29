import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_graficos/tony_ingresos.csv")

# creamos el gráfico
sns.barplot(x="fuente", y="ingresos", data=df)

# calculando el total de ingresos
total_ingresos = df['ingresos'].sum()
print(f'El total de ingresos es {total_ingresos}')

# ploteamos el gráfico
plt.show()
