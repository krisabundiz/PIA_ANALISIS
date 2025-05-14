# Demuestra la aplicación de objetos de pandas.
import pandas as pd

df_datos = pd.read_csv('datos.csv')

# Propone el esquema de filtrado más conveniente.

# Filtrar solo registros de México
mexico_df = df_datos[df_datos['PAÍS'] == 'MEXICO']
print(mexico_df[["FECHA", "CONTAGIOS", "MUERTES", "PAÍS"]].head(10))


