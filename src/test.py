# Importamos las librerias necesarias
import pandas as pd
from graficos import GraficosSencillos

# Creamos un DataFrame y un objeto de la clase Graficos
df = pd.DataFrame({
    "Mes": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "Ingresos": [22000, 25000, 45000, 30000, 35000, 40000, 42000, 46000, 48000, 50000, 53000, 55000]
})
ingresos_mes = GraficosSencillos(df, "Mes", "Ingresos", "Ingresos de cada mes (€)", "o")

# Creamos un gráfico de barra
ingresos_mes.crearGraficoBarra()
    
# Creamos un gráficos de linea
ingresos_mes.crearGraficoLinea()
