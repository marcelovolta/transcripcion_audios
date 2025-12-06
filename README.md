# Transcripcion_audios
Este script Python toma un archivo de audio mejorado y lo convierte a texto usando la biblioteca Whisper de Open AI

# Pre-tratamiento y mejora de audios
Si tengo un video el primer paso es extraer el audio, lo que se logra con el siguiente comando: 
`ffmpeg -i "nombre_archivo_origen.mp4" -q:a 0 -map a "nombre_archivo_destino.mp3"`
Una vez tengo el archivo de audio, ejecutar el siguiente comando que lo convierte en mono, normaliza el volumen, quita silencios y lo mejora antes del reconocimiento:
`ffmpeg -i "nombre_archivo_origen.mp3|wav" -ac 1 -ar 16000 -filter:a "loudnorm,silenceremove=start_periods=1:start_duration=1:start_threshold=-40dB" "nombre_archivo_destino.m4a"`

## Pegar varios videos juntos
Cuando hay varios videos juntos que necesito pegar, como sucede en EEA, usar un archivo de texto para especificar qué archivos de video quiero pegar. 
Comando para pegar varios videos uno después del otro
`ffmpeg -f concat -safe 0 -i clase_01.txt -c copy eea_clase_01_completa.mp4` 
El archivo clase_01.txt tiene esta pinta: 
```
file 'nombre_archivo_01.mp4'
file 'nombre_archivo_02.mp4'
file 'nombre_archivo_03.mp4'
```

#### Prompt para limpiar subtitulos
Necesito una transcripción limpia del texto proporcionado. Dado que es un subtítulo de YouTube, necesito que le quites las indicaciones de tiempo y los saltos de linea innecesarios, dejando todo el resto inalterado

#### Prompt para recrear el texto: 
Utilizando toda esta información que extraje de una clase, necesito que me hagas una transcripción detallada de la clase, extrayendo toda la información compartida por el profesor y ampliando cuando sea necesario. Ten en cuenta que puede haber errores de interpretación en el texto copiado ( no los PDFs), ya que para obtenerlo se procesó un archivo de audio grabado durante la clase. No quiero un resumen sino un texto completo que pueda utilizar para estudiar y como fuente de consulta, pero que esté bien organizado y completo. EN lo posible, que reproduzca el modo en el que el profesor lo presentó, pero quitando interjecciones como "eh" y otros modismos que no contribuyen al texto.




