import pandas as pd

# Especifica la ruta del archivo CSV
archivo_csv = 'DATA/viajes_para_logit_.csv'

# Lee el archivo CSV y lo convierte en un DataFrame
df = pd.read_csv(archivo_csv, encoding='ISO-8859-1', keep_default_na=False)

# Filtra el DataFrame
df_filtrado = df[((df['Comuna de origen'] == 'LAS CONDES') & (df['Comuna de destino'] == 'VITACURA'))]
