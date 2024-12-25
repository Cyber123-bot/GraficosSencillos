import unittest
import pandas as pd
from graficos import GraficosSencillos

class TestGraficosSencillos(unittest.TestCase):

    def setUp(self):
        # Crear un DataFrame de ejemplo para las pruebas
        data = {
            'Categoria': ['A', 'B', 'C', 'D'],
            'Valores': [10, 20, 15, 25]
        }
        self.df = pd.DataFrame(data)
        self.titulo_01 = 'Categoria'
        self.titulo_02 = 'Valores'
        self.titulo = 'Grafico de Prueba'
        self.graficos = GraficosSencillos(self.df, self.titulo_01, self.titulo_02, self.titulo)

    def test_crearGraficoBarra(self):
        # Probar la creación de un gráfico de barras
        try:
            self.graficos.crearGrafico(tipo='barra', color='green')
        except Exception as e:
            self.fail(f"crearGraficoBarra raised an exception {e}")

    def test_crearGraficoLinea(self):
        # Probar la creación de un gráfico de líneas
        try:
            self.graficos.crearGrafico(tipo='linea', color='red', estilo='--', grosor=3)
        except Exception as e:
            self.fail(f"crearGraficoLinea raised an exception {e}")

    def test_invalid_column(self):
        # Probar la inicialización con columnas inválidas
        with self.assertRaises(ValueError):
            GraficosSencillos(self.df, 'Invalido', self.titulo_02, self.titulo)

    def test_invalid_tipo_grafico(self):
        # Probar la creación de un gráfico con tipo inválido
        with self.assertRaises(ValueError):
            self.graficos.crearGrafico(tipo='invalido')

if __name__ == '__main__':
    unittest.main()