import pandas as pd
import os

years = range(2015, 2022)

def procesar_dataset(year):
    # Construir la ruta del archivo CSV
    file_path = f'C:\\Users\\sdvc0\\OneDrive\\Escritorio\\REPOSITORIO_ENAPEA\\Base de datos\\Divorcios\\conjunto_de_datos_divorcios_{year}.csv'
    
    # Leer el CSV y seleccionar columnas relevantes
    df = pd.read_csv(file_path)[['anio_mat', 'tipo_div', 'ent_regis', 'mun_regis', 'causa', 'hijos', 'custodia', 'pension', 
                                 'edad_mdiv1', 'escol_div1', 'con_acdiv1', 'sexo_div1', 'edad_mdiv2', 'escol_div2', 'con_acdiv2', 'sexo_div2']]
    
    # Aplicar filtro de edad y año de ocurrencia en línea de la ENAPEA
    df = df[(df['anio_mat'] >= 2015) & (df['anio_mat'] <= 2030)]
    
    # Eliminar filas donde ambas columnas 'sexo_div1' y 'sexo_div2' son 'Mujer'
    df = df[~((df['sexo_div1'] == '2') & (df['sexo_div2'] == '2'))]
    
    # Crear columnas para identificar entidad y municipio y aplicar los primary keys
    df['entidad_id'] = df['ent_regis']
    df['municipio_id'] = df['mun_regis']
    
    return df

# Procesar y concatenar todos los datasets en uno
dfs = [procesar_dataset(year) for year in years]
DIVOR = pd.concat(dfs, ignore_index=True)

# Mapeos para las columnas específicas
mapeos = {
    'tipo_div': {1: 'Judicial', 2: 'Administrativo'},
    'custodia': {0: 'no se otorga', 1: 'Divorciante 1', 2: 'Divorciante 2', 3: 'Ambos', 4: 'Otro', 98: 'No aplica', 99: 'No especificado'},
    'pension': {1: 'Hijos', 2: 'Divorciante 1', 3: 'Divorciante 2', 4: 'Ninguno', 12: 'Hijos y Divorciante 1', 13: 'Hijos y Divorciante 2', 98: 'No aplica', 99: 'No especificado'},
    'escol_div1': {0: 'Sin escolaridad', 1: 'Primaria incompleta', 2: 'Primaria completa', 3: 'Primaria completa', 4: 'Secundaria o equivalente', 5: 'Preparatoria o equivalente', 6: 'Superior', 7: 'Carrera técnica', 8: 'Otra', 9: 'No especificada'},
    'escol_div2': {0: 'Sin escolaridad', 1: 'Primaria incompleta', 2: 'Primaria completa', 3: 'Primaria completa', 4: 'Secundaria o equivalente', 5: 'Preparatoria o equivalente', 6: 'Superior', 7: 'Carrera técnica', 8: 'Otra', 9: 'No especificada'},
    'con_acdiv1': {1: 'Trabaja', 2: 'No trabaja', 9: 'No especificada'},
    'con_acdiv2': {1: 'Trabaja', 2: 'No trabaja', 9: 'No especificada'},
    'sexo_div1': {1: 'Hombre', 2: 'Mujer'},
    'sexo_div2': {1: 'Hombre', 2: 'Mujer'},
    'causa' : { 1: "Mutuo consentimiento",
2: "Adulterio o infidelidad sexual",
    3: "Alumbramiento ilegítimo",
    4: "Propuesta de prostitución",
    5: "Incitación a la violencia",
    6: "Corrupción y/o maltrato a los hijos",
    7: "Enfermedad crónica o incurable, la impotencia o esterilidad incurable",
    8: "Enajenación mental incurable o el estado de interdicción declarado por sentencia",
    9: "Separación del hogar conyugal por más de 1 año, con o sin causa justificada",
    10: "Abandono de hogar por más de 3 o 6 meses, sin causa justificada",
    11: "Declaración de ausencia o presunción de muerte",
    12: "Sevicia, amenazas o injurias o la violencia intrafamiliar",
    13: "Negativa a contribuir voluntariamente o por sentencia del juez familiar al sostenimiento del hogar",
    14: "Acusación calumniosa",
    15: "Haber cometido delito doloso o infamante",
    16: "Hábitos de juego, embriaguez o drogas",
    17: "Cometer acto delictivo contra el cónyuge",
    18: "Incompatibilidad de caracteres",
    19: "La separación por 2 años o más independientemente del motivo",
    20: "La bigamia",
    21: "No acompañar la mujer a su marido, cuando cambie de residencia dentro o fuera del país",
    22: "Si un cónyuge solicitó el divorcio por causa injustificada, el demandado puede divorciarse 3 meses después de la última sentencia",
    23: "Fecundación asistida sin consentimiento del cónyuge",
    24: "Impedir uno de los cónyuges a otro desempeñar una actividad lícita",
    25: "Reconocer la mujer a un hijo nacido antes del matrimonio sin consentimiento del marido",
    26: "Uso de métodos de esterilización permanente sin consentimiento del cónyuge",
    27: "Bisexualidad manifestada, o intención o cambio de sexo por tratamiento médico o quirúrgico",
    28: "Voluntario unilateral",
    99: "No especificada"}
}

# Aplicar los mapeos a las columnas correspondientes
for col, mapping in mapeos.items():
    if col in DIVOR.columns:
        DIVOR[col] = DIVOR[col].map(mapping)

# Cargar archivos de municipios y entidades ycausas
municipios_df = pd.read_csv('C://Users//sdvc0//OneDrive//Escritorio//REPOSITORIO_ENAPEA//Base de datos//MUNICIPIO.csv')
entidad_df = pd.read_csv('C://Users//sdvc0//OneDrive//Escritorio//REPOSITORIO_ENAPEA//Base de datos//ENTIDAD.csv')

# Realizar las uniones
DIVOR = DIVOR.merge(municipios_df[['MUNICIPIO_ID', 'MUNICIPIO']], left_on='municipio_id', right_on='MUNICIPIO_ID')
DIVOR = DIVOR.merge(entidad_df[['ENT_ID', 'ENTIDAD']], left_on='entidad_id', right_on='ENT_ID')

# Limpiar columnas adicionales y renombrar
DIVOR.drop(columns=['MUNICIPIO_ID', 'ENT_ID','mun_regis', 'ent_regis'], inplace=True)
DIVOR.rename(columns={'MUNICIPIO': 'mun_regis', 'ENTIDAD': 'ent_regis'}, inplace=True)

# Rellenar valores nulos con 'No especificado' si los hay
DIVOR.fillna(value='No especificado', inplace=True)

DIVOR = DIVOR[['anio_mat', 'entidad_id','ent_regis', 'municipio_id', 'mun_regis', 'tipo_div',  'causa', 'hijos', 'custodia', 'pension', 
                                 'edad_mdiv1', 'escol_div1', 'con_acdiv1', 'sexo_div1', 'edad_mdiv2', 'escol_div2', 'con_acdiv2', 'sexo_div2']]

# Guardar el DataFrame final en CSV
DIVOR.to_csv('C://Users//sdvc0//OneDrive//Escritorio//REPOSITORIO_ENAPEA//BACK//Matrimonios y Divorcios//Divorcios//DIVOR.csv', index=False, encoding='utf-8-sig')

#Realizar ajustes manueales en excel en caso de haber incidencias de registros de bodas del mismo sexo