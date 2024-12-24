# Librerías necesarias
import seaborn as sns
import matplotlib.pyplot as plt

class GraficosSencillos:
    """Clase para crear gráficos con seaborn y matplotlib"""

    def __init__(self, df, titulo_01, titulo_02, titulo, punto='X'):
        """Inicializa los parámetros y valida las columnas del DataFrame"""
        self.df = df
        self.titulo_01 = titulo_01
        self.titulo_02 = titulo_02
        self.titulo = titulo
        self.punto = punto
        
        if titulo_01 not in df.columns or titulo_02 not in df.columns:
            raise ValueError(f"Las columnas '{titulo_01}' y '{titulo_02}' deben existir en el DataFrame.")
    
    def crearGraficoBarra(self, color='skyblue'):
        """Crea un gráfico de barras"""
        plt.figure(figsize=(8, 6))  # Configura el tamaño del gráfico
        plt.bar(self.df[self.titulo_01], self.df[self.titulo_02], color=color)  # Crea el gráfico de barras
        plt.title(self.titulo)  # Asigna el título del gráfico
        plt.xlabel(self.titulo_01)  # Asigna el nombre del eje X
        plt.ylabel(self.titulo_02)  # Asigna el nombre del eje Y
        plt.xticks(rotation=45)  # Rota las etiquetas del eje X para mayor legibilidad
        plt.tight_layout()  # Ajusta el diseño para evitar que las etiquetas se corten
        plt.show()  # Muestra el gráfico
        
    def crearGraficoLinea(self, color='blue', estilo='-', grosor=2):
        """Crea un gráfico de líneas"""
        plt.figure(figsize=(8, 6))  # Configura el tamaño del gráfico
        # Crea el gráfico de líneas con seaborn
        sns.lineplot(data=self.df, x=self.titulo_01, y=self.titulo_02, 
                     marker=self.punto, color=color, linestyle=estilo, linewidth=grosor)
        plt.title(self.titulo)  # Asigna el título del gráfico
        plt.tight_layout()  # Ajusta el diseño para evitar que las etiquetas se corten
        plt.show()  # Muestra el gráfico
        
    def crearGrafico(self, tipo='barra', **kwargs):
        """Crea un gráfico de barras o líneas dependiendo del tipo"""
        if tipo == 'barra':
            return self.crearGraficoBarra(**kwargs)
        elif tipo == 'linea':
            return self.crearGraficoLinea(**kwargs)
        else:
            raise ValueError("El tipo de gráfico debe ser 'barra' o 'linea'.")
