# TIC - Sebastian Cruz

Este repositorio contiene los recursos desarrollados para la generación de contenido matemático accesible mediante sonificación de ecuaciones con SSML y descripciones textuales integradas en documentos LaTeX. Se emplearon Python, Google Cloud TTS y Ollama para implementar esta solución.

---

## Estructura del Proyecto

### **`src/public`**
- **`audio/`**: Archivos `.mp3` generados a partir de SSML.
- **`documents/`**: Archivos `.tex` originales y modificados con tooltips.
- **`extracted/`**: Ecuaciones extraídas de archivos `.tex` en formato `.txt`.
- **`pdf/`**: PDFs generados a partir de archivos LaTeX.
- **`responses/`**: Salidas de Ollama en formato SSML y texto.

### **`src/scripts`**
Contiene los scripts en Python para las distintas etapas del proceso:
1. **`extract-eqs.py`**: Extrae ecuaciones de archivos LaTeX.
2. **`api-ssml.py`**: Genera archivos SSML y descripciones usando Ollama.
3. **`tooltips.py`**: Añade tooltips descriptivos a las ecuaciones en los archivos LaTeX.
4. **`lattex.py`**: Compila archivos `.tex` en documentos PDF.
5. **`rules.py`**: Define reglas para la generación de SSML y descripciones.

---

## Flujo de Trabajo

1. **Extracción de Ecuaciones**  
   Ejecuta `extract-eqs.py` para obtener ecuaciones en un archivo `.txt`.
   
2. **Generación de Contenidos**  
   Usa `api-ssml.py` para crear archivos SSML y descripciones textuales con ayuda de un modelo de LLAMA.

3. **Modificación de LaTeX**  
   Aplica `tooltips.py` para añadir tooltips a las ecuaciones en los archivos `.tex`.

4. **Compilación Final**  
   Genera PDFs accesibles ejecutando `lattex.py`.

---

## Requisitos

### Herramientas
- Python 3.10+
- Google Cloud TTS
- Ollama API
- LaTeX (pdflatex - mikTex)

### Paquetes Python
- `re`
- `os`
- `requests`
- `subprocess`

---

## Cómo Ejecutar

1. **Configura el entorno**: 
Instala Python, LaTeX, y configura Google Cloud TTS y Ollama.
2. **Extrae ecuaciones**:
   ```bash
   python src/scripts/extract-eqs.py
   ```
3. **Genera SSML y descripciones:**
    ```bash
    python src/scripts/api-ssml.py
    ```

4. **Añade tooltips:**
    ```bash
    python src/scripts/tooltips.py
    ```
5. **Compila el PDF final:**
    ```bash
    python src/scripts/lattex.py
    ```

## Contacto
- Sebastián Cruz
- Escuela Politécnica Nacional
- dilan.cruz@epn.edu.ec






