import speech_recognition as sr

# Initialiser le recognizer
recognizer = sr.Recognizer()

# Utiliser le microphone pour capturer l'audio
with sr.Microphone() as source:
    print("Parlez quelque chose...")
    try:
        # Écouter et capturer l'audio
        audio = recognizer.listen(source)

        # Reconnaître le texte (langue française)
        texte = recognizer.recognize_google(audio, language="fr-FR")
        print("Vous avez dit : ", texte)

    except sr.UnknownValueError:
        print("Désolé, je n'ai pas compris.")
    except sr.RequestError as e:
        print(f"Erreur du service Google Speech Recognition : {e}")
