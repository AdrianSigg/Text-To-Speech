from gtts import gTTS
import os

# Texto que deseas convertir a habla
texto = "Hola, esto es una demostración de Google Text-to-Speech en Python."

# Crea un objeto gTTS
tts = gTTS(text=texto, lang='es')

# Guarda el archivo de audio en un formato temporal (por ejemplo, mp3)
temp_audio_file = "temp_audio.mp3"
tts.save(temp_audio_file)

# Reproduce el audio (esto funciona en sistemas Windows)
os.system(f"start {temp_audio_file}")
