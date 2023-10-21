import boto3
import io
from pydub import AudioSegment

# Configura el cliente de Polly
polly = boto3.client('polly', region_name='us-east-1')  # Cambia 'us-east-1' a tu región

# Texto que deseas convertir en voz con marcadores de pronunciación y puntuación
texto_a_convertir = "Bienvenido al servicio de consulta de saldo. "
texto_a_convertir += "Por favor, elija una de las siguientes opciones: "
texto_a_convertir += "1. Consultar saldo. "
texto_a_convertir += "2. Realizar una transferencia. "
texto_a_convertir += "3. Hablar con un agente de servicio al cliente."

# Define marcadores de pronunciación (SSML) para mejorar la pronunciación
ssml = f"<speak>{texto_a_convertir}</speak>"

# Solicita la síntesis de voz
response = polly.synthesize_speech(
    TextType='ssml',  # Indica que estás usando SSML
    Text=ssml,
    OutputFormat='mp3',  # Puedes cambiar el formato de salida a 'ogg_vorbis' u otros
    VoiceId='Mia'  # Cambia a la voz que suene más natural para tu caso
)

# Lee el stream de audio
audio_stream = response['AudioStream'].read()

# Crea un archivo temporal para guardar el audio en formato MP3
with io.BytesIO(audio_stream) as temp_audio:
    audio = AudioSegment.from_mp3(temp_audio)

    # Guarda el audio en un archivo temporal en formato WAV
    temp_wav_path = "temp.wav"
    audio.export(temp_wav_path, format="wav")

# Reproduce el archivo WAV con un reproductor de audio externo
import subprocess
subprocess.run(["start", "temp.wav"], shell=True, check=True)
