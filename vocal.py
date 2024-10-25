import speech_recognition as sr
recognizer = sr.Recognizer()

# install pyaudio
# brew install portaudio

#https://pypi.org/project/SpeechRecognition/ LA LIBRAIRIE

with sr.Microphone() as source:
    print("Parlez maintenant...")
    audio_data = recognizer.listen(source)
    print("Reconnaissance en cours...")

    try:
        text = recognizer.recognize_google(audio_data, language="fr-FR")
        print("Résultat: " + text)
        if (text=="Rouge" ):
        	print("Vous avez dit rouge")
        elif(text=="Bleu"):
        	print("Vous avez dit vert")
        elif (text=="Vert" ):
        	print("Vous avez dit bleu")
    except sr.UnknownValueError:
        print("Impossible de comprendre l'audio")
    except sr.RequestError:
        print("Service de reconnaissance indisponible")