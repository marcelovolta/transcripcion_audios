import whisper
import os

def procesar_directo(archivo: str):
    model = whisper.load_model("large")  # o "small", "medium", "large"
    result = model.transcribe(archivo, language="es")
    print(result["text"])
    os.system('osascript -e \'display notification "Tu script ha terminado." with title "Proceso completado"\'')


def procesar_con_progreso(archivo: str):
    from pydub import AudioSegment
    from tqdm import tqdm


    model = whisper.load_model("large")
    audio = AudioSegment.from_file(archivo)
    chunk_duration_ms = 60_000  # 1 minuto

    chunks = [audio[i:i + chunk_duration_ms] for i in range(0, len(audio), chunk_duration_ms)]
    results = []

    for i, chunk in enumerate(tqdm(chunks, desc="Transcribiendo")):
        temp_path = f"chunk_{i}.wav"
        chunk.export(temp_path, format="wav")
        result = model.transcribe(temp_path, language="es")
        results.append(result["text"])
    return results

archivo = '/Users/sergiovolta/Documents/Videos de Clases Maestria/AID/Análisis Inteligente de Datos   31 05 2025.m4a'
results = procesar_con_progreso(archivo)
print(results)
os.system('osascript -e \'display notification "Tu script ha terminado." with title "Proceso completado"\'')