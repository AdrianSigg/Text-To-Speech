from google.cloud import texttospeech
import os

credentials_path = "C:/Users/mrfun/OneDrive/Documentos/Cloud/GPC/Credentials/texttospeech-402620-562568bdead6.json"

# Define las credenciales de GCP
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path

# Crea una instancia del cliente Text-to-Speech
client = texttospeech.TextToSpeechClient()

# Texto a convertir
texto = "Bienvenido al servicio de consulta de saldo. "
texto += "Por favor, elija una de las siguientes opciones: "
texto += "1. Consultar saldo. "
texto += "2. Realizar una transferencia. "
texto += "3. Hablar con un agente de servicio al cliente."

# Configura la solicitud de síntesis de voz
solicitud = texttospeech.SynthesisInput(text=texto)

# Configura el tipo de voz y parámetros de audio
voz = texttospeech.VoiceSelectionParams(
    language_code="es-US",  # Idioma (código de idioma)
    name="es-US-Neural2-A",  # Nombre de la voz
)
parametros_audio = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.LINEAR16  # Formato de audio
)

# Realiza la solicitud de síntesis de voz
respuesta = client.synthesize_speech(
    input=solicitud, voice=voz, audio_config=parametros_audio
)

# Guarda el audio en un archivo o realiza acciones adicionales
with open("audio.wav", "wb") as archivo_audio:
    archivo_audio.write(respuesta.audio_content)
    
print("Success")