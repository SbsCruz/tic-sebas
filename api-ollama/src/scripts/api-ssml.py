import requests
import json
import sys
import os

from rules import reglas_ssml, reglas_detail  # Importar reglas para SSML y para TXT

# Función para leer ecuaciones desde un archivo .txt
def leer_ecuaciones_desde_archivo(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        # Leer cada línea del archivo y eliminar espacios en blanco o saltos de línea
        ecuaciones = [linea.strip() for linea in archivo if linea.strip()]
    return ecuaciones

# Leer las ecuaciones desde el archivo
input_file = 'forms'
ruta_archivo = f'api-ollama/src/public/extracted/{input_file}.txt' # Cambia esto a la ruta de tu archivo .txt
ecuaciones = leer_ecuaciones_desde_archivo(ruta_archivo)

# Construir la lista de mensajes para cada ecuación en el for_ssml
for idx, ecuacion in enumerate(ecuaciones):
    for_ssml = reglas_ssml + [
        {
            "role": "user",
            "content": ecuacion # Enviar la ecuación leída
        }
    ]
    
    payload_ssml = {
        "model": "llama3.1:8b",
        "messages": for_ssml,
        "stream": False,
    }

    # Enviar la solicitud a la API para SSML
    response_ssml = requests.post(
        "http://localhost:11434/api/chat",
        json=payload_ssml
    )

    # Mostrar la respuesta de la API para SSML
    respuesta_ssml = response_ssml.json()['message']['content']
    print(respuesta_ssml)

    # Crear la carpeta para guardar el archivo .ssml si no existe
    ruta_carpeta_ssml = f'api-ollama/src/public/responses/{input_file}/ssml/'
    os.makedirs(ruta_carpeta_ssml, exist_ok=True)

    # Guardar la respuesta en un archivo .ssml con un nombre único basado en el índice
    ruta_archivo_ssml = f'{ruta_carpeta_ssml}{input_file}_{idx + 1}.ssml' # Nombre de archivo único
    with open(ruta_archivo_ssml, 'w') as archivo_ssml:
        archivo_ssml.write(respuesta_ssml)

# Construir la lista de mensajes para cada ecuación en el for_txt
for idx, ecuacion in enumerate(ecuaciones):
    for_txt = reglas_detail + [
        {
            "role": "user",
            "content": ecuacion # Enviar la ecuación leída
        }
    ]

    payload_txt = {
        "model": "llama3.1:8b",
        "messages": for_txt,
        "stream": False,
    }

    # Enviar la solicitud a la API para TXT
    response_txt = requests.post(
        "http://localhost:11434/api/chat",
        json=payload_txt
    )

    # Mostrar la respuesta de la API para TXT
    respuesta_txt = response_txt.json()['message']['content']
    print(respuesta_txt)

    # Crear la carpeta para guardar el archivo .txt si no existe
    ruta_carpeta_txt = f'api-ollama/src/public/responses/{input_file}/txt/'
    os.makedirs(ruta_carpeta_txt, exist_ok=True)

    # Guardar la respuesta en un archivo .txt con un nombre único basado en el índice
    ruta_archivo_txt = f'{ruta_carpeta_txt}{input_file}_{idx + 1}.txt' # Nombre de archivo único
    with open(ruta_archivo_txt, 'w') as archivo_txt:
        archivo_txt.write(respuesta_txt)
