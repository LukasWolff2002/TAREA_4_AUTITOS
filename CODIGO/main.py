#Este es el archivo a ejecutar que muestra las respuestas
from modelo import modelo_regresion
from lectura_csv import df_filtrado as df
from math import exp

intercept, coeficientes = modelo_regresion(df)

# Mostrar el resultado
print('Los valores para y = 1 son:')
print(f"Intercepto (αa): {intercept}")
print(f"Coeficientes (θk): {coeficientes}")

#Con esto es posible calcular el valor Va
#Va = αa + θ1x1 + θ2x2
#Donde x1 y x2 son los promedos
x1 = df['Distancia'].mean()
x2 = df['Ingreso per cápita'].mean()
Va = (intercept + coeficientes[0][0] * x1 + coeficientes[0][1] * x2)[0]
print(f'El valor Va es: {Va}')

#COn esto es posible calcular el valor de la probabilidad
P1 = exp(Va) / (1 + exp(Va))
P0 = 1 / (1 + exp(Va))
print(f'La probabilidad de que un viaje sea privado es: {P1=}')
print(f'La probabilidad de que un viaje sea público es: {P0=}')