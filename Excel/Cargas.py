import pandas as pd

hospitales = pd.read_csv('/workspaces/Estructura_datos/Excel/Tablahospital.csv')
print(hospitales.head()) 
print(hospitales.dtypes) 
hospitales['AÑO'] = hospitales ['AÑO'].str.replace(',','')
print(hospitales.head()) 
print(hospitales.dtypes)
hospitales['AÑO'] = hospitales ['AÑO'].astype(int)
print(hospitales.head()) 
print(hospitales.dtypes)