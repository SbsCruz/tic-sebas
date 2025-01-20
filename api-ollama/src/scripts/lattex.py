import subprocess
import os


input_file = "forms"

def compilar_latex(archivo_tex, directorio_salida):
    try:
        # Crear el directorio de salida si no existe
        os.makedirs(directorio_salida, exist_ok=True)
        
        # Ejecutar el comando pdflatex con la opción -output-directory
        subprocess.run(["pdflatex", "-output-directory", directorio_salida, archivo_tex], check=True)
        print("Compilación exitosa.")
        return True
    except subprocess.CalledProcessError:
        print("Error al compilar LaTeX.")
        return False

# Rutas
output_tex = f"src/public/documents/{input_file}_tooltip.tex"
directorio_salida = f"src/public/pdf/{input_file}/"
compilar_latex(output_tex, directorio_salida)

