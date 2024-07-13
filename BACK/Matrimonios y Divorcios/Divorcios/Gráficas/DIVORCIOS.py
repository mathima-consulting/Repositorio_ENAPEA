import pandas as pd
import os

years = range(2015, 2022)


import pandas as pd

def procesar_dataset(year):
    # Construir la ruta del archivo CSV
    file_path = f'C:\\Users\\sdvc0\\OneDrive\\Escritorio\\REPOSITORIO_ENAPEA\\Base de datos\\Divorcios\\conjunto_de_datos_divorcios_{year}.csv'
    
    # Leer el CSV y seleccionar columnas relevantes
    df = pd.read_csv(file_path)[['anio_mat','tipo_div','ent_regis','mun_regis','causa','hijos','custodia','pension','edad_mdiv1','escol_div1','con_acdiv1','sexo_div1','edad_mdiv2','escol_div2','con_acdiv2','sexo_div2']]
    
    # Filtrar por sexo_div1 y edad_mdiv1
    filtered_df1 = df[(df['sexo_div1'] == 2) & (df['edad_mdiv1'] < 20)]
    
    # Si el primer filtro no tiene resultados, filtrar por sexo_div2 y edad_mdiv2
    if filtered_df1.empty:
        filtered_df2 = df[(df['sexo_div2'] == 2) & (df['edad_mdiv2'] < 20)]
        df_filtered = filtered_df2
    else:
        df_filtered = filtered_df1
    
    # Aplicar el filtro de año de ocurrencia en línea de la ENAPEA
    df_filtered = df_filtered[df_filtered['anio_mat'] > 2014]
    
    # Crear columnas para identificar entidad y municipio y aplicar los primary keys
    df_filtered['entidad_id'] = df_filtered['ent_regis']
    df_filtered['municipio_id'] = df_filtered['mun_regis']
    
    return df_filtered


# Procesar y concatenar todos los datasets en uno
dfs = [procesar_dataset(year) for year in years]
DIVOR = pd.concat(dfs, ignore_index=True)
DIVOR.to_csv('C://Users//sdvc0//OneDrive//Escritorio//REPOSITORIO_ENAPEA//BACK//Matrimonios y Divorcios//Divorcios//DIVOR.csv', index=False, encoding='utf-8-sig')
