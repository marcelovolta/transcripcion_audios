# Transcripcion_audios
Este script Python toma un archivo de audio mejorado y lo convierte a texto usando la biblioteca Whisper de Open AI

# Pre-tratamiento y mejora de audios
Si tengo un video el primer paso es extraer el audio, lo que se logra con el siguiente comando: 
`ffmpeg -i "nombre_archivo_origen.mp4" -q:a 0 -map a "nombre_archivo_destino.mp3"`
Una vez tengo el archivo de audio, ejecutar el siguiente comando que lo convierte en mono, normaliza el volumen, quita silencios y lo mejora antes del reconocimiento:
`ffmpeg -i "nombre_archivo_origen.mp3|wav" -ac 1 -ar 16000 -filter:a "loudnorm,silenceremove=start_periods=1:start_duration=1:start_threshold=-40dB" "nombre_archivo_destino.m4a"`




