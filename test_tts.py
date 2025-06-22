from TTS.api import TTS

# Carga un modelo multi-speaker para español
tts = TTS(model_name="tts_models/es/multi-speaker/vits")

# Lista de voces disponibles para elegir una femenina
print("Voces disponibles:", tts.speakers)

# Usa la voz femenina pasando su nombre en 'speaker'
voz_femenina = [s for s in tts.speakers if "female" in s.lower()]
if voz_femenina:
    speaker_name = voz_femenina[0]
else:
    speaker_name = None

# Genera el audio con la voz femenina seleccionada
tts.tts_to_file(
    text="Hola, esta es una prueba con voz femenina en español.",
    file_path="voz_femenina_multi_speaker.wav",
    speaker=speaker_name,
)

