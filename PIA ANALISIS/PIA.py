# Demuestra la aplicación de objetos de pandas.
import pandas as pd

df_datos = pd.read_csv('datos.csv')

# print(df_datos.head())


# Filtrado de datos en un DataFrame de pandas
#mexico_df = df_datos[df_datos['PAÍS'] == 'MEXICO']
#print(mexico_df[["FECHA", "CONTAGIOS", "MUERTES", "PAÍS"]].head(10))

# Filtrado por valores nulos
#nulo_df = df_datos[df_datos["FECHA"].isnull()]
#print(nulo_df)

# Agrupar por México y mes, y obtener la suma de contagios y muertes
agrupado = df_datos.groupby('MES')[['CONTAGIOS', 'MUERTES']].sum().reset_index()
print(agrupado.head())
