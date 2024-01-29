import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_graficos/gases.csv")

# creamos el gráfico
sns.lineplot(x="fecha", y="gases", data=df)

# indicamos un punto en particular donde hubo mas gases
plt.plot("01-09", 17, 'o')

# ploteamos el gráfico
plt.show()
