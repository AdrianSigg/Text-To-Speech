import boto3

# Configura el cliente de Polly
polly = boto3.client('polly', region_name='us-east-1')

# Texto a convertir
texto_a_convertir = "Bienvenido al servicio de consulta de saldo. "
texto_a_convertir += "Por favor, elija una de las siguientes opciones: "
texto_a_convertir += "1. Consultar saldo. "
texto_a_convertir += "2. Realizar una transferencia. "
texto_a_convertir += "3. Hablar con un agente de servicio al cliente."

# Define marcadores de pronunciación (SSML) para mejorar la pronunciación
ssml = f"<speak>{texto_a_convertir}</speak>"

# Solicita la síntesis de voz
response = polly.synthesize_speech(
    Engine='neural',  # Utiliza el motor "neural"
    LanguageCode = 'es-MX', # Idioma
    #LexiconNames = '', # Para modificar la pronunciación
    #SampleRate = '8000', # Tasa de muestreo del audio
    TextType='ssml',  # Indica que estás usando SSML
    Text=ssml, # Se proporciona el texto a convertir con las etiquetas SSML
    OutputFormat='mp3',  # Formato de salida
    VoiceId='Mia'  # Tipo de voz
)

# Guarda la respuesta de Polly en un archivo de audio
with open("salida.mp3", "wb") as archivo_audio:
    archivo_audio.write(response['AudioStream'].read())

print("Texto convertido en audio y guardado como 'salida.mp3'")
