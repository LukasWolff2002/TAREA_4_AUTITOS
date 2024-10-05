from lectura_csv import df_filtrado as df
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from math import exp

# Filtrar los datos para Modo Privado = 1 (privado)
df_filtrado_privado = df[df['Modo privado'] == 1]
X_privado = df_filtrado_privado[['Distancia', 'Ingreso per cápita']].values

# Filtrar los datos para Modo Privado = 0 (público)
df_filtrado_publico = df[df['Modo privado'] == 0]
X_publico = df_filtrado_publico[['Distancia', 'Ingreso per cápita']].values

# Concatenar las características (X) para ambos modos
X = df[['Distancia', 'Ingreso per cápita']].values

# Crear la variable objetivo (y) - 1 para privado y 0 para público
y = df['Modo privado'].values  # Esto debe ser 1 o 0 según la columna 'Modo privado'

# Dividir los datos en entrenamiento y prueba (usamos un 80% para entrenar, 20% para probar)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de regresión logística
modelo = LogisticRegression()

# Entrenar el modelo
modelo.fit(X_train, y_train)

# Hacer predicciones con el conjunto de prueba
y_pred = modelo.predict(X_test)

# Calcular la precisión
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión: {accuracy * 100:.2f}%')

# Obtener el intercepto (αa)
intercept = modelo.intercept_

# Obtener los coeficientes (θk)
coeficientes = modelo.coef_

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


'''
# Mostrar la matriz de confusión
conf_matrix = confusion_matrix(y_test, y_pred)
print('Matriz de confusión:')
print(conf_matrix)
print('')

#En este caso la matriz de confusion representa lo siguiente:
print('\t Prediccion: 0 \t Prediccion: 1')
print('Real 0: \t TN \t FP')
print(f'Real 1: \t FN \t TP')
print('')
print('Donde:')
print('TN: True Negative')
print('FP: False Positive')
print('FN: False Negative')
print('TP: True Positive')
'''