import re

def leer_archivo_tex(ruta):
    with open(ruta, 'r') as file:
        return file.read()

def extraer_ecuaciones(tex_content):
    pattern = r'\\\[(.*?)\\\]|\\begin\{equation\}(.*?)\\end\{equation\}|\\begin\{equation\*\}(.*?)\\end\{equation\*\}|\$\$(.*?)\$\$'
    # Extraer ecuaciones y limpiar los resultados
    ecuaciones = re.findall(pattern, tex_content, re.DOTALL)
    # Filtrar las ecuaciones no vacías y aplanar la lista de tuplas
    ecuaciones_limpias = [ecuacion.strip() for grupo in ecuaciones for ecuacion in grupo if ecuacion]
    return ecuaciones_limpias

def generar_archivo_txt_con_ecuaciones(ruta_tex, ruta_txt):
    # Leer el contenido del archivo .tex
    contenido_tex = leer_archivo_tex(ruta_tex)
    # Extraer las ecuaciones del contenido del .tex
    ecuaciones = extraer_ecuaciones(contenido_tex)
    # Escribir las ecuaciones en el archivo .txt
    with open(ruta_txt, 'w') as archivo_txt:
        for ecuacion in ecuaciones:
            archivo_txt.write(f"{ecuacion}\n")

# Ejemplo de uso:
input_file = "forms"
ruta_archivo_tex = f'api-ollama/src/public/documents/{input_file}.tex'  # Ruta relativa al archivo .tex
ruta_archivo_txt = f'api-ollama/src/public/extracted/{input_file}.txt'  # Ruta relativa para el archivo .txt a generar
generar_archivo_txt_con_ecuaciones(ruta_archivo_tex, ruta_archivo_txt)

