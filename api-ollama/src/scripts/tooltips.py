import re
import os

def insertar_tooltips(input_tex, output_tex, tooltip_dir):
    with open(input_tex, 'r') as archivo_tex:
        contenido = archivo_tex.read()

    # Verificar si el paquete pdfcomment está importado
    if r'\usepackage{pdfcomment}' not in contenido:
        # Insertar la línea después del \documentclass
        contenido = re.sub(
            r'(\\documentclass\[.*?\]\{.*?\})',
            r'\1\n\\usepackage{pdfcomment}',
            contenido,
            count=1
        )
        print("El paquete pdfcomment fue añadido al archivo.")

    # Patrón para encontrar ecuaciones
    pattern = r'\\\[(.*?)\\\]|\\begin\{equation\}(.*?)\\end\{equation\}|\\begin\{equation\*\}(.*?)\\end\{equation\*\}|\$\$(.*?)\$\$'
    ecuaciones = re.findall(pattern, contenido, re.DOTALL)

    # función para envolver con \pdftooltip
    def envolver_con_tooltip(match, idx):
        ecuacion = next((ec for ec in match if ec.strip()), '')  # Encuentra la ecuación no vacía
        tooltip_path = os.path.join(tooltip_dir, f"{input_file}_{idx + 1}.txt")
        if os.path.exists(tooltip_path):
            with open(tooltip_path, 'r') as tooltip_file:
                descripcion = tooltip_file.read().strip()
            return f"\\pdftooltip{{{ecuacion}}}{{{descripcion}}}"
        else:
            print(f"Advertencia: No se encontró la descripción para la ecuación {idx + 1}.")
            return ecuacion

    # Reemplazar las ecuaciones con sus versiones con tooltip
    nuevo_contenido = contenido
    for idx, grupo in enumerate(ecuaciones):
        nuevo_contenido = nuevo_contenido.replace(
            ''.join(grupo),
            envolver_con_tooltip(grupo, idx)
        )

    # Guardar el nuevo archivo .tex
    with open(output_tex, 'w') as archivo_modificado:
        archivo_modificado.write(nuevo_contenido)
    print(f"Archivo modificado guardado en: {output_tex}")

# Rutas de ejemplo
input_file = "forms"
input_tex = f"src/public/documents/{input_file}.tex"
output_tex = f"src/public/documents/{input_file}_tooltip.tex"
tooltip_dir = f"src/public/responses/{input_file}/txt"

insertar_tooltips(input_tex, output_tex, tooltip_dir)
