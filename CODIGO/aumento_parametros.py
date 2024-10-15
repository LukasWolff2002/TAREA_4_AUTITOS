from lectura_csv import df_filtrado

X = df_filtrado[df_filtrado['Modo privado'] == 1]
X_i = X['Ingreso per cápita']*1.1
X_i = X_i.mean()

X = df_filtrado[df_filtrado['Modo privado'] == 1]
X_ordenado = X.sort_values(by='Ingreso per cápita', ascending=False)

# Determinar el punto medio
mitad = int(len(X_ordenado) // 2)
print(X_ordenado)
# Multiplicar la primera mitad por 1.1
X_ordenado['Ingreso per cápita'].iloc[:mitad] = X_ordenado['Ingreso per cápita'].iloc[:mitad] * 1.12

# Multiplicar la segunda mitad por 0.9 (por ejemplo)
X_ordenado['Ingreso per cápita'].iloc[mitad:] = X_ordenado['Ingreso per cápita'].iloc[mitad:] * 1.08

print(X_ordenado['Ingreso per cápita'].mean())