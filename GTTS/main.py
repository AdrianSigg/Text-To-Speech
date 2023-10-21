from gtts import gTTS
import os

# Texto que deseas convertir a habla
texto = "Bienvenido al servicio de consulta de saldo. "
texto += "Por favor, elija una de las siguientes opciones: "
texto += "1. Consultar saldo. "
texto += "2. Realizar una transferencia. "
texto += "3. Hablar con un agente de servicio al cliente."

# Crea un objeto gTTS
tts = gTTS(text=texto, lang='es', tld='com.mx')

# Guarda el archivo de audio en tu sistema
tts.save("audio.mp3")

print('Text to speech realizada con éxito')