import pandas as pd

#------------------------------------------------------DATASET 2022
#Conectar al CSV
df22 = pd.read_csv('C:\\Users\\sdvc0\\OneDrive\\Escritorio\\REPOSITORIO_ENAPEA\\Base de datos\\Mortalidad\\Materna\\conjunto_de_datos_defunciones_registradas_2022.CSV')

#Selecccionar las columnas del ERM
df22 = df22[['ent_resid', 'mun_resid', 'edad', 'anio_ocur', 'capitulo', 
             'grupo', 'causa_def',  'tipo_defun', 'lugar_ocur', 'sitio_ocur', 
             'derechohab', 'embarazo', 'rel_emba', 'complicaro', 'par_agre']]

# Convertir la columna 'edad' a tipo cadena (str) para manipulación Extraer los últimos dos dígitos de cada valor en la columna 'edad' y regresar a int
df22['edad'] = df22['edad'].astype(str)
df22['edad'] = df22['edad'].str[-2:]
df22['edad'] = df22['edad'].astype(int)

#Aplicar filtro de edad y año de ocurrencia en linea de la ENAPEA y solo cuando hay evento de embarazo
df22 = df22[(df22['edad'] < 20) & (df22['anio_ocur'] > 2014) & (df22['embarazo'].isin([1, 2, 3, 4]))]



#------------------------------------------------------DATASET 2021
#Conectar al CSV
df21 = pd.read_csv('C:\\Users\\sdvc0\\OneDrive\\Escritorio\\REPOSITORIO_ENAPEA\\Base de datos\\Mortalidad\\Materna\\conjunto_de_datos_defunciones_registradas_2021.CSV')

#Selecccionar las columnas del ERM
df21 = df21[['ent_resid', 'mun_resid', 'edad', 'anio_ocur', 'capitulo', 
             'grupo', 'causa_def',  'presunto', 'lugar_ocur', 'sitio_ocur', 
             'derechohab', 'embarazo', 'rel_emba', 'complicaro', 'par_agre']]

# Convertir la columna 'edad' a tipo cadena (str) para manipulación Extraer los últimos dos dígitos de cada valor en la columna 'edad' y regresar a int
df21['edad'] = df21['edad'].astype(str)
df21['edad'] = df21['edad'].str[-2:]
df21['edad'] = df21['edad'].astype(int)

#Aplicar filtro de edad y año de ocurrencia en linea de la ENAPEA y solo cuando hay evento de embarazo
df21 = df21[(df21['edad'] < 20) & (df21['anio_ocur'] > 2014) & (df21['embarazo'].isin([1, 2, 3, 4]))]


#Cambiar el nombre de presunto a tipo_defun ya que en 2022 se actualizo el nombre de la columna
df21.rename(columns={'presunto': 'tipo_defun'}, inplace=True)

#------------------------------------------------------DATASET 2020
#Conectar al CSV
df20 = pd.read_csv('C:\\Users\\sdvc0\\OneDrive\\Escritorio\\REPOSITORIO_ENAPEA\\Base de datos\\Mortalidad\\Materna\\conjunto_de_datos_defunciones_registradas_2020.CSV')

#Selecccionar las columnas del ERM
df20 = df20[['ent_resid', 'mun_resid', 'edad', 'anio_ocur', 'capitulo', 
             'grupo', 'causa_def',  'presunto', 'lugar_ocur', 'sitio_ocur', 
             'derechohab', 'embarazo', 'rel_emba', 'complicaro', 'par_agre']]

# Convertir la columna 'edad' a tipo cadena (str) para manipulación Extraer los últimos dos dígitos de cada valor en la columna 'edad' y regresar a int
df20['edad'] = df20['edad'].astype(str)
df20['edad'] = df20['edad'].str[-2:]
df20['edad'] = df20['edad'].astype(int)

#Aplicar filtro de edad y año de ocurrencia en linea de la ENAPEA y solo cuando hay evento de embarazo
df20 = df20[(df20['edad'] < 20) & (df20['anio_ocur'] > 2014) & (df20['embarazo'].isin([1, 2, 3, 4]))]

#Cambiar el nombre de presunto a tipo_defun ya que en 2022 se actualizo el nombre de la columna
df20.rename(columns={'presunto': 'tipo_defun'}, inplace=True)

#------------------------------------------------------DATASET 2019
#Conectar al CSV
df19 = pd.read_csv('C:\\Users\\sdvc0\\OneDrive\\Escritorio\\REPOSITORIO_ENAPEA\\Base de datos\\Mortalidad\\Materna\\conjunto_de_datos_defunciones_registradas_2019.CSV')

#Selecccionar las columnas del ERM
df19 = df19[['ent_resid', 'mun_resid', 'edad', 'anio_ocur', 'capitulo', 
             'grupo', 'causa_def',  'presunto', 'lugar_ocur', 'sitio_ocur', 
             'derechohab', 'embarazo', 'rel_emba', 'complicaro', 'par_agre']]

# Convertir la columna 'edad' a tipo cadena (str) para manipulación Extraer los últimos dos dígitos de cada valor en la columna 'edad' y regresar a int
df19['edad'] = df19['edad'].astype(str)
df19['edad'] = df19['edad'].str[-2:]
df19['edad'] = df19['edad'].astype(int)

#Aplicar filtro de edad y año de ocurrencia en linea de la ENAPEA y solo cuando hay evento de embarazo
df19 = df19[(df19['edad'] < 20) & (df19['anio_ocur'] > 2014) & (df19['embarazo'].isin([1, 2, 3, 4]))]

#Cambiar el nombre de presunto a tipo_defun ya que en 1922 se actualizo el nombre de la columna
df19.rename(columns={'presunto': 'tipo_defun'}, inplace=True)


#------------------------------------------------------DATASET 2018
#Conectar al CSV
df18 = pd.read_csv('C:\\Users\\sdvc0\\OneDrive\\Escritorio\\REPOSITORIO_ENAPEA\\Base de datos\\Mortalidad\\Materna\\conjunto_de_datos_defunciones_registradas_2018.CSV')

#Selecccionar las columnas del ERM
df18 = df18[['ent_resid', 'mun_resid', 'edad', 'anio_ocur', 'capitulo', 
             'grupo', 'causa_def',  'presunto', 'lugar_ocur', 'sitio_ocur', 
             'derechohab', 'embarazo', 'rel_emba', 'complicaro', 'par_agre']]

# Convertir la columna 'edad' a tipo cadena (str) para manipulación Extraer los últimos dos dígitos de cada valor en la columna 'edad' y regresar a int
df18['edad'] = df18['edad'].astype(str)
df18['edad'] = df18['edad'].str[-2:]
df18['edad'] = df18['edad'].astype(int)

#Aplicar filtro de edad y año de ocurrencia en linea de la ENAPEA y solo cuando hay evento de embarazo
df18 = df18[(df18['edad'] < 20) & (df18['anio_ocur'] > 2014) & (df18['embarazo'].isin([1, 2, 3, 4]))]

#Cambiar el nombre de presunto a tipo_defun ya que en 2022 se actualizo el nombre de la columna
df18.rename(columns={'presunto': 'tipo_defun'}, inplace=True)

#------------------------------------------------------DATASET 2017
#Conectar al CSV
df17 = pd.read_csv('C:\\Users\\sdvc0\\OneDrive\\Escritorio\\REPOSITORIO_ENAPEA\\Base de datos\\Mortalidad\\Materna\\conjunto_de_datos_defunciones_registradas_2017.CSV')

#Selecccionar las columnas del ERM
df17 = df17[['ent_resid', 'mun_resid', 'edad', 'anio_ocur', 'capitulo', 
             'grupo', 'causa_def',  'presunto', 'lugar_ocur', 'sitio_ocur', 
             'derechohab', 'embarazo', 'rel_emba', 'complicaro', 'par_agre']]

# Convertir la columna 'edad' a tipo cadena (str) para manipulación Extraer los últimos dos dígitos de cada valor en la columna 'edad' y regresar a int
df17['edad'] = df17['edad'].astype(str)
df17['edad'] = df17['edad'].str[-2:]
df17['edad'] = df17['edad'].astype(int)

#Aplicar filtro de edad y año de ocurrencia en linea de la ENAPEA y solo cuando hay evento de embarazo
df17 = df17[(df17['edad'] < 20) & (df17['anio_ocur'] > 2014) & (df17['embarazo'].isin([1, 2, 3, 4]))]

#Cambiar el nombre de presunto a tipo_defun ya que en 2022 se actualizo el nombre de la columna
df17.rename(columns={'presunto': 'tipo_defun'}, inplace=True)

#------------------------------------------------------DATASET 2016
#Conectar al CSV
df16 = pd.read_csv('C:\\Users\\sdvc0\\OneDrive\\Escritorio\\REPOSITORIO_ENAPEA\\Base de datos\\Mortalidad\\Materna\\conjunto_de_datos_defunciones_registradas_2016.CSV')

#Selecccionar las columnas del ERM
df16 = df16[['ent_resid', 'mun_resid', 'edad', 'anio_ocur', 'capitulo', 
             'grupo', 'causa_def',  'presunto', 'lugar_ocur', 'sitio_ocur', 
             'derechohab', 'embarazo', 'rel_emba', 'complicaro', 'par_agre']]

# Convertir la columna 'edad' a tipo cadena (str) para manipulación Extraer los últimos dos dígitos de cada valor en la columna 'edad' y regresar a int
df16['edad'] = df16['edad'].astype(str)
df16['edad'] = df16['edad'].str[-2:]
df16['edad'] = df16['edad'].astype(int)

#Aplicar filtro de edad y año de ocurrencia en linea de la ENAPEA y solo cuando hay evento de embarazo
df16 = df16[(df16['edad'] < 20) & (df16['anio_ocur'] > 2014) & (df16['embarazo'].isin([1, 2, 3, 4]))]

#Cambiar el nombre de presunto a tipo_defun ya que en 2022 se actualizo el nombre de la columna
df16.rename(columns={'presunto': 'tipo_defun'}, inplace=True)

#------------------------------------------------------DATASET 2015
#Conectar al CSV
df15 = pd.read_csv('C:\\Users\\sdvc0\\OneDrive\\Escritorio\\REPOSITORIO_ENAPEA\\Base de datos\\Mortalidad\\Materna\\conjunto_de_datos_defunciones_registradas_2015.CSV')

#Selecccionar las columnas del ERM
df15 = df15[['ent_resid', 'mun_resid', 'edad', 'anio_ocur', 'capitulo', 
             'grupo', 'causa_def',  'presunto', 'lugar_ocur', 'sitio_ocur', 
             'derechohab', 'embarazo', 'rel_emba', 'complicaro', 'par_agre']]

# Convertir la columna 'edad' a tipo cadena (str) para manipulación Extraer los últimos dos dígitos de cada valor en la columna 'edad' y regresar a int
df15['edad'] = df15['edad'].astype(str)
df15['edad'] = df15['edad'].str[-2:]
df15['edad'] = df15['edad'].astype(int)

#Aplicar filtro de edad y año de ocurrencia en linea de la ENAPEA y solo cuando hay evento de embarazo
df15 = df15[(df15['edad'] < 20) & (df15['anio_ocur'] > 2014) & (df15['embarazo'].isin([1, 2, 3, 4]))]

#Cambiar el nombre de presunto a tipo_defun ya que en 2022 se actualizo el nombre de la columna
df15.rename(columns={'presunto': 'tipo_defun'}, inplace=True)

# Unir los DataFrames
MORT_MAT = pd.concat([df15, df16, df17, df18, df19, df20, df21, df22], ignore_index=True)

# Diccionario para mapear los valores de 'Presunto' a sus etiquetas correspondientes
tipo_defun_mapping = {
    1: 'Accidente',
    2: 'Homicidio',
    3: 'Suicidio',
    4: 'Se ignora',
    5: 'Operaciones legales y de guerra',
    8: 'No aplica'
}
# Reemplazar los valores de la columna 'causa_def' utilizando el diccionario
MORT_MAT['tipo_defun'] = MORT_MAT['tipo_defun'].map(tipo_defun_mapping)

# Diccionario para mapear los valores de 'lugar_ocur' a sus etiquetas correspondientes
lugar_ocur_mapping = {
    0: 'Vivienda particular',
    1: 'Vivienda colectiva',
    2: 'Escuela u oficina pública',
    3: 'Áreas deportivas',
    4: 'Calle o carretera (vía pública)',
    5: 'Área comercial o de servicios',
    6: 'Área industrial (taller, fabrica u obra)',
    7: 'Granja (rancho o parcela)',
    8: 'Otro',
    9: 'Se ignora',
    88: 'No aplica'
}

# Reemplazar los valores de la columna 'Presunto' utilizando el diccionario
MORT_MAT['lugar_ocur'] = MORT_MAT['lugar_ocur'].map(lugar_ocur_mapping)

# Diccionario para mapear los valores de 'Sitio_ocur' a sus etiquetas correspondientes
sitio_ocur_mapping = {
    1: 'Secretaría de Salud',
    2: 'IMSS PROSPERA',
    3: 'IMSS',
    4: 'ISSSTE',
    5: 'PEMEX',
    6: 'Secretaría de la Defensa Nacional (SEDENA)',
    7: 'Secretaría de Marina (SEMAR)',
    8: 'Otra unidad pública',
    9: 'Unidad médica privada',
    10: 'Vía pública',
    11: 'Hogar',
    12: 'Otro lugar',
    99: 'No especificada'
}

MORT_MAT['sitio_ocur'] = MORT_MAT['sitio_ocur'].map(sitio_ocur_mapping)

derechohab_mapping = {
    1: 'Ninguna',
    2: 'IMSS',
    3: 'ISSSTE',
    4: 'PEMEX',
    5: 'SEDENA',
    6: 'SEMAR',
    7: 'Seguro Popular',
    8: 'Otra',
    9: 'IMSS PROSPERA',
    99: 'No especificada'
}
MORT_MAT['derechohab'] = MORT_MAT['derechohab'].map(derechohab_mapping)

embarazo_mapping = {
    1: 'El embarazo',
    2: 'El parto',
    3: 'El puerperio',
    4: '43 días a 11 meses después del parto o aborto'
}
MORT_MAT['embarazo'] = MORT_MAT['embarazo'].map(embarazo_mapping)
rel_emba_mapping = {
    1: 'Sí tuvieron relación las causas',
    2: 'No tuvieron relación las causas',
    8: 'No aplica',
    9: 'No especificada'
}
MORT_MAT['rel_emba'] = MORT_MAT['rel_emba'].map(rel_emba_mapping)

complicaro_mapping = {
    1: 'Sí complicaron el embarazo',
    2: 'No complicaron el embarazo',
    8: 'No aplica',
    9: 'No especificada'
}
MORT_MAT['complicaro'] = MORT_MAT['complicaro'].map(complicaro_mapping)

causa_df = pd.read_csv('C://Users//sdvc0//OneDrive//Escritorio//REPOSITORIO_ENAPEA//Base de datos//Mortalidad//Materna//Catalogos//causa_defuncion.csv')
merged_df = MORT_MAT.merge(causa_df, left_on='causa_def', right_on='cve')
merged_df['causa_def'] = merged_df['descrip']
MORT_MAT = merged_df
MORT_MAT.drop(columns=['cve'], inplace=True)
MORT_MAT.drop(columns=['descrip'], inplace=True)

capitulo = pd.read_csv('C://Users//sdvc0//OneDrive//Escritorio//REPOSITORIO_ENAPEA//Base de datos//Mortalidad//Materna//Catalogos//capitulo.csv')
merged_df = MORT_MAT.merge(capitulo, left_on='capitulo', right_on='CAP', how='left')
merged_df['capitulo'] = merged_df['DESCRIP']
MORT_MAT = merged_df
MORT_MAT.drop(columns=['CAP'], inplace=True)
MORT_MAT.drop(columns=['DESCRIP'], inplace=True)

grupo = pd.read_csv('C://Users//sdvc0//OneDrive//Escritorio//REPOSITORIO_ENAPEA//Base de datos//Mortalidad//Materna//Catalogos//grupo.csv')
merged_df = MORT_MAT.merge(grupo, left_on='grupo', right_on='GRUPO')
merged_df['grupo'] = merged_df['DESCRIP']
MORT_MAT = merged_df
MORT_MAT.drop(columns=['GRUPO'], inplace=True)
MORT_MAT.drop(columns=['DESCRIP'], inplace=True)

par_agre = pd.read_csv('C://Users//sdvc0//OneDrive//Escritorio//REPOSITORIO_ENAPEA//Base de datos//Mortalidad//Materna//Catalogos//parentesco_agresor.csv')
merged_df = MORT_MAT.merge(par_agre, left_on='par_agre', right_on='CVE')
merged_df['par_agre'] = merged_df['DESCRIP']
MORT_MAT = merged_df
MORT_MAT.drop(columns=['CVE'], inplace=True)
MORT_MAT.drop(columns=['DESCRIP'], inplace=True)

#Crear columnas para identificar entidad y municipio y aplicar los primary keys
MORT_MAT['entidad_id'] = MORT_MAT['ent_resid']
MORT_MAT['municipio_id'] = (MORT_MAT['ent_resid'].astype(str) + MORT_MAT['mun_resid'].astype(str)).astype(int)

# Cargar el archivo ENTIDAD.csv
entidad = pd.read_csv('C://Users//sdvc0//OneDrive//Escritorio//REPOSITORIO_ENAPEA//Base de datos//ENTIDAD.csv')
# Realizar la unión entre los DataFrames
merged_df = MORT_MAT.merge(entidad, left_on='entidad_id', right_on='ENT_ID')

# Reemplazar la columna 'mun_resid' con la columna 'ENTIDAD'
merged_df['ent_resid'] = merged_df['ENTIDAD']


#Actualizar el dataset MORT_MAT
MORT_MAT = merged_df

# Cargar el archivo causas.csv
municipios_df = pd.read_csv('C://Users//sdvc0//OneDrive//Escritorio//REPOSITORIO_ENAPEA//Base de datos//MUNICIPIO.csv')
# Realizar la unión entre los DataFrames
merged_df = MORT_MAT.merge(municipios_df, left_on='municipio_id', right_on='MUNICIPIO_ID')

# Reemplazar la columna 'mun_resid' con la columna 'MUNICIPIO'
merged_df['mun_resid'] = merged_df['MUNICIPIO']


MORT_MAT = merged_df

MORT_MAT.drop(columns=['ENT_ID'], inplace=True)
MORT_MAT.drop(columns=['MUNICIPIO_ID'], inplace=True)
MORT_MAT.drop(columns=['ENTIDAD'], inplace=True)
MORT_MAT.drop(columns=['MUNICIPIO'], inplace=True)

MORT_MAT.to_csv('C://Users//sdvc0//OneDrive//Escritorio//REPOSITORIO_ENAPEA//BACK//Mortalidad//Materna//MORT_MAT.csv', index=False, encoding='utf-8-sig')

