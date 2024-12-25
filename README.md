## GraficosSencillos

Este proyecto facilita la creación de gráficos personalizables con seaborn y matplotlib.

## Requisitos

- `Python 3.x`
- Módulo `pandas`
- Módulo `seaborn`
- Módulo `matplotlib`
- Módulo `unittest`

## Instalación

1. Clona este repositorio en tu máquina local:
    ```bash
    git clone https://github.com/Cyber123-bot/GraficosSencillos.git
    ```
2. Asegúrate de tener Python 3.x y los módulos necesarios instalados:
    ```bash
    pip install pandas seaborn matplotlib
    ```

## Uso

Para usar la clase `GraficosSencillos`, primero debes importar las librerías necesarias y ejecutar el archivo `src/pruebas.py`.

## Parámetros de la clase

- `df`: DataFrame que contiene los datos a graficar.
- `titulo_01`: Nombre de la columna para el eje X.
- `titulo_02`: Nombre de la columna para el eje Y.
- `titulo`: Título del gráfico.
- `punto`: Estilo del marcador para el gráfico de líneas (opcional, por defecto 'X').

## Métodos de la clase

- `crearGraficoBarra(color='skyblue')`: Crea un gráfico de barras.
- `crearGraficoLinea(color='blue', estilo='-', grosor=2)`: Crea un gráfico de líneas.
- `crearGrafico(tipo='barra', **kwargs)`: Crea un gráfico de barras o líneas dependiendo del tipo especificado.

## Testeo
Para asegurarte de que todo funciona correctamente puedes ejecutar el archivo `src/test.py`

## Estilos de marcadores

Puedes usar los siguientes estilos de marcadores para el gráfico de líneas:

1. "." - Punto pequeño
2. "," - Pixel (pequeño, solo un píxel)
3. "o" - Círculo
4. "v" - Triángulo hacia abajo
5. "^" - Triángulo hacia arriba
6. "<" - Triángulo hacia la izquierda
7. ">" - Triángulo hacia la derecha
8. "1" - Triángulo con vértice hacia abajo
9. "2" - Triángulo con vértice hacia arriba
10. "3" - Triángulo con vértice hacia la izquierda
11. "4" - Triángulo con vértice hacia la derecha
12. "8" - Octágono
13. "s" - Cuadrado
14. "p" - Pentágono
15. "P" - Plus (más)
16. "*" - Estrella
17. "h" - Hexágono
18. "H" - Hexágono rotado
19. "+" - Cruz
20. "x" - Cruz en diagonal
21. "X" - Cruz doble en diagonal
22. "D" - Diamante
23. "d" - Diamante pequeño
24. "|" - Línea vertical
25. "-" - Línea horizontal

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún problema o tienes alguna mejora, por favor abre un issue o envía un pull request. Más información en `docs/CONTRIBUTING.md`

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.