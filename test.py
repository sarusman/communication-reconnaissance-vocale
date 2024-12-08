import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
from faster_whisper import WhisperModel

def record_audio(duration, samplerate=16000):
    """Enregistre de l'audio à partir du micro."""
    print("Enregistrement en cours... Parlez maintenant.")
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype=np.float32)
    sd.wait()
    print("Enregistrement terminé.")
    return np.squeeze(audio_data)

def save_audio(audio_data, samplerate, filename="output.wav"):
    """Sauvegarde l'audio enregistré dans un fichier WAV."""
    wav.write(filename, samplerate, (audio_data * 32767).astype(np.int16))
    print(f"Audio sauvegardé dans le fichier : {filename}")

def transcribe_audio(filename, model_path="base"):
    """Transcrit l'audio à l'aide de Faster Whisper."""
    print("Transcription en cours...")
    model = WhisperModel(model_path, device="cpu")  # Utilisez "cuda" pour GPU si disponible
    segments, info = model.transcribe(filename, language="fr", beam_size=5)
    
    print("Transcription terminée.")
    transcription = ""
    for segment in segments:
        transcription += segment.text + " "
    return transcription

if __name__ == "__main__":
    DURATION = 10  # Durée de l'enregistrement en secondes
    SAMPLERATE = 16000  # Fréquence d'échantillonnage
    
    # Étape 1 : Enregistrer l'audio
    audio_data = record_audio(DURATION, SAMPLERATE)
    
    # Étape 2 : Sauvegarder l'audio dans un fichier WAV
    audio_file = "output.wav"
    save_audio(audio_data, SAMPLERATE, audio_file)
    
    # Étape 3 : Transcrire l'audio
    transcription = transcribe_audio(audio_file)
    print("\nTranscription :")
    print(transcription)