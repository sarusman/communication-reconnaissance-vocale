import wave
import numpy as np
import matplotlib.pyplot as plt
import speech_recognition as sr

# Initialisation du recognizer pour la reconnaissance vocale
recognizer = sr.Recognizer()

def enregistrer_audio(donnees_audio):
    """Enregistrer les données audio dans un fichier WAV."""
    with wave.open("audio_sortie.wav", "wb") as wf:
        wf.setnchannels(1)  # Mono
        wf.setsampwidth(2)  # 2 octets (16 bits)
        wf.setframerate(44100)
        wf.writeframes(donnees_audio.tobytes())

    print("Fichier audio sauvegardé sous 'audio_sortie.wav'")

def afficher_signal_enregistre():
    """Afficher le signal audio à partir du fichier .wav."""
    chemin_fichier = 'audio_sortie.wav'  # Chemin du fichier .wav
    signal_audio, frequence_echantillonnage = lire_fichier_wav(chemin_fichier)

    # Calculer l'axe des temps
    temps = np.linspace(0, len(signal_audio) / frequence_echantillonnage, num=len(signal_audio))

    # Afficher le signal
    plt.figure(figsize=(10, 4))
    plt.plot(temps, signal_audio)
    plt.title("Signal Audio Enregistré")
    plt.xlabel("Temps (s)")
    plt.ylabel("Amplitude")
    plt.show()

def lire_fichier_wav(chemin_fichier):
    """Lire le fichier WAV et retourner le signal audio sous forme de tableau."""
    with wave.open(chemin_fichier, 'rb') as wf:
        n_channels = wf.getnchannels()
        sample_width = wf.getsampwidth()
        frequence_echantillonnage = wf.getframerate()
        n_frames = wf.getnframes()

        # Lire les données du fichier
        donnees_audio = wf.readframes(n_frames)

        # Convertir les données en tableau numpy
        signal_audio = np.frombuffer(donnees_audio, dtype=np.int16)

        # Si le fichier est stéréo, on prend juste un canal (par exemple, le canal gauche)
        if n_channels == 2:
            signal_audio = signal_audio[::2]

    return signal_audio, frequence_echantillonnage

def obtenir_couleur_vocale():
    """Analyser le texte vocal et retourner la couleur détectée."""
    with sr.Microphone() as source:
        print("Parlez maintenant...")
        audio_data = recognizer.listen(source)  # Enregistrer l'audio
        print("Enregistrement terminé, traitement en cours...")

        try:
            # Utiliser Google Speech API pour convertir l'audio en texte
            texte = recognizer.recognize_google(audio_data, language="fr-FR")
            print("Vous avez dit : " + texte)

            # Détecter la couleur en fonction du texte
            couleur = None
            if texte.lower() == "rouge":
                couleur = "red"
            elif texte.lower() == "bleu":
                couleur = "blue"
            elif texte.lower() == "vert":
                couleur = "green"
            else:
                print("Couleur non reconnue.")

            return couleur
        except sr.UnknownValueError:
            print("Impossible de comprendre l'audio.")
            return None
        except sr.RequestError:
            print("Service de reconnaissance indisponible.")
            return None
