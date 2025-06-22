import requests
import uuid
import time
from playsound import playsound

def hablar(texto):
    url = "https://api.fishaudio.xyz/api/tts"
    voz = "Lucia"
    payload = {
        "text": texto,
        "voice": voz,
        "id": str(uuid.uuid4())
    }

    r = requests.post(url, json=payload)
    audio_url = r.json().get("url")
    if not audio_url:
        print("No se pudo obtener el audio.")
        return

    filename = f"voz_{int(time.time())}.mp3"
    audio = requests.get(audio_url)
    with open(filename, "wb") as f:
        f.write(audio.content)

    playsound(filename)
