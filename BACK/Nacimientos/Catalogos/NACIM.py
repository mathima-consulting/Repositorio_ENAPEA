import pandas as pd

#ACTUALIZAR EN LOS AÑOS SUBSECUENTES DURANTE EL PERIODO DE LA ENAPEA 2015-2030
years = range(2015, 2022) 

def procesar_dataset(year):
    # Construir la ruta del archivo CSV
    file_path = f'C:\\Users\\sdvc0\\OneDrive\\Escritorio\\REPOSITORIO_ENAPEA\\Base de datos\\Nacimientos registrados\\conjunto_de_datos_natalidad_{year}.csv'
    
    # Leer el CSV y seleccionar columnas relevantes
    df = pd.read_csv(file_path)[['ent_resid','mun_resid','ano_nac','edad_madn','edad_padn','sexo','tipo_nac','orden_part','lugar_part','q_atendio','edociv_mad','escol_mad','escol_pad','act_mad','act_pad','fue_prese']]   
    
    # Aplicar filtro de edad y año de ocurrencia en línea de la ENAPEA
    #df = df[(df['edad_madn'] < 20) & (df['ano_nac'] > 2014)]
    
    # Crear columnas para identificar entidad y municipio y aplicar los primary keys
    df['entidad_id'] = df['ent_resid']
    df['municipio_id'] = df['mun_resid']
    
    return df


# Procesar y concatenar todos los datasets en uno
dfs = [procesar_dataset(year) for year in years]
NACIM = pd.concat(dfs, ignore_index=True)

NACIM.to_csv('C://Users//sdvc0//OneDrive//Escritorio//REPOSITORIO_ENAPEA//BACK//Nacimientos//NACIM.csv', index=False, encoding='utf-8-sig')

