from google.cloud import texttospeech
import os

# Instancia un cliente
client = texttospeech.TextToSpeechClient()

input_name = "forms"

# Configura las rutas
input_directory = f"src/public/ssml/{input_name}"  # Directorio donde están los archivos SSML
output_directory = f"src/public/audio/{input_name}/"  # Directorio donde se guardarán los archivos de audio

# Asegúrate de que el directorio de salida existe
os.makedirs(output_directory, exist_ok=True)

# Itera sobre los archivos en el directorio de entrada
for filename in os.listdir(input_directory):
    # Procesa solo archivos .ssml
    if filename.endswith(".ssml"):
        input_ssml = os.path.join(input_directory, filename)
        output_file = os.path.join(
            output_directory, f"{os.path.splitext(filename)[0]}.mp3"
        )
        try:
            # Lee el contenido del archivo SSML
            with open(input_ssml, "r", encoding="utf-8") as ssml_file:
                ssml_content = ssml_file.read()
            # Establece el contenido SSML de entrada para sintetizar
            synthesis_input = texttospeech.SynthesisInput(ssml=ssml_content)
            # Configura la solicitud de voz
            voice = texttospeech.VoiceSelectionParams(
                language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
            )
            # Configura el tipo de archivo de audio que deseas devolver
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.MP3
            )
            # Realiza la solicitud de texto a voz
            response = client.synthesize_speech(
                input=synthesis_input, voice=voice, audio_config=audio_config
            )
            # Guarda el archivo de salida
            with open(output_file, "wb") as out:
                out.write(response.audio_content)
            print(f"Audio content written to file: {output_file}")

        except Exception as e:
            print(f"Error processing file {input_ssml}: {e}")
