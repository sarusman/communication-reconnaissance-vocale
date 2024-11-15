import speech_recognition as sr
couleurs = {
    "rouge": "#FF0000",
    "bleu": "#0000FF",
    "vert": "#00FF00",
    "jaune": "#FFFF00",
    "noir": "#000000",
    "blanc": "#FFFFFF",
    "gris": "#808080",
    "orange": "#FFA500",
    "rose": "#FFC0CB",
    "violet": "#800080"
}
def reconnaissance_vocal() :
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
            couleur_detectee = next((couleur for couleur in couleurs if couleur in texte.lower()), None)

            if couleur_detectee:
                print("Couleur détectée :", couleur_detectee)
                return couleur_detectee
            else:
                print("Aucune couleur détectée.")
                return ""
        except sr.UnknownValueError:
            print("Désolé, je n'ai pas compris.")
            return ""
        except sr.RequestError as e:
            print(f"Erreur du service Google Speech Recognition : {e}")
            return ""
