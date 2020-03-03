# Diamonds Project
## Introducción
En el siguiente proyecto vamos a predecir el precio de una serie de diamantes 
en base a sus características

## Limpieza de datos
Para la limpieza de datos, lo primero que he hecho ha sido detectar 
aquellas columnas categóricas. Lo que descubrimos es que existen
tres columnas categóricas: cut, color y clarity. En el script clean.py 
procedemos a su trasformación a tipo numérico haciendo la escala donde
el número 1 corresponde al peor y el más alto a lo mejor en su categoría.
Eliminamos las columnas: table, depth, z e y debido a que table y depth 
no tienen una alta correlación con la columna que queremos predecir (price),
y borramos z e y porque tienen una alta correlación con la columna 
x  que es la que usaremos para entranar el modelo

## Modelos
Para la predicción hemos usado el modelo RandomForestRegressor