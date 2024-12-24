# Librerias necesarias
import seaborn as sns
import matplotlib.pyplot as plt

# Libreria necesaria para la prueba
import pandas as pd

class Graficos:
    """Clase que facilita la creación de gráficos con seaborn y matplotlib"""

    def __init__(self, df, titulo_01, titulo_02, titulo, punto='X'):
        """Guardar los parámetros como atributos de la instancia"""
        self.df = df
        self.titulo_01 = titulo_01
        self.titulo_02 = titulo_02
        self.titulo = titulo
        self.punto = punto
    
    def crearGraficoBarra(self):
        """ Función para crear gráficos en barra """
        # Crear el gráfico de barra con matplotlib
        plt.bar(self.df[self.titulo_01], self.df[self.titulo_02])
        plt.title(self.titulo)
        plt.xlabel(self.titulo_01)
        plt.ylabel(self.titulo_02)
        plt.show()
        
    def crearGraficoLinea(self):
        """ Función para crear gráficos en modo de linea """
        # Crear el gráfico de linea con seaborn
        sns.lineplot(data=self.df, x=self.titulo_01, y=self.titulo_02, marker=self.punto)
        plt.title(self.titulo)
        plt.show()
