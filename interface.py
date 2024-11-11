import tkinter as tk
from vocal import enregistrer_audio, afficher_signal_enregistre, obtenir_couleur_vocale


class ApplicationDetecteurCouleur:
    def __init__(self, racine):
        self.racine = racine
        self.racine.title("Reconnaissance vocale des couleurs")
        self.racine.geometry("600x500")

        # Initialisation des éléments de l'interface
        self.label_titre = tk.Label(racine, text="Reconnaissance vocale des couleurs", font=("Arial", 24, "italic"))
        self.label_titre.pack(pady=20)

        self.affichage_couleur = tk.Frame(racine, width=300, height=200, bg="white", relief="ridge", borderwidth=2)
        self.affichage_couleur.pack(pady=20)

        self.bouton_enregistrement = tk.Button(racine, text="Démarrer l'enregistrement", font=("Arial", 16), bg="orange", fg="white", command=self.toggle_enregistrement)
        self.bouton_enregistrement.pack(pady=10)

        self.affichage_spectre = tk.Canvas(racine, width=400, height=50, bg="lightgrey")
        self.affichage_spectre.pack(pady=20)

        # Initialisation de l'état d'enregistrement
        self.enregistrement_en_cours = False
        self.frames_audio = []

    def toggle_enregistrement(self):
        if not self.enregistrement_en_cours:
            # Démarrer l'enregistrement
            self.enregistrement_en_cours = True
            self.frames_audio = []  # Réinitialiser les frames audio
            self.bouton_enregistrement.config(text="Arrêter l'enregistrement", bg="grey")
            self.demarrer_flux_audio()
        else:
            # Arrêter l'enregistrement
            self.enregistrement_en_cours = False
            self.bouton_enregistrement.config(text="Démarrer l'enregistrement", bg="orange")
            self.arreter_flux_audio()
            self.enregistrer_fichier_audio()
            self.analyser_et_afficher_couleur()
            self.afficher_signal_enregistre()

    def demarrer_flux_audio(self):
        """Initialiser le flux audio pour enregistrer le son."""
        import pyaudio
        self.p = pyaudio.PyAudio()
        self.flux_audio = self.p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        self.mettre_a_jour_spectre()

    def arreter_flux_audio(self):
        """Arrêter l'enregistrement audio."""
        if self.flux_audio:
            self.flux_audio.stop_stream()
            self.flux_audio.close()
            self.p.terminate()

    def mettre_a_jour_spectre(self):
        """Mettre à jour l'affichage du spectre audio en temps réel."""
        if self.enregistrement_en_cours:
            # Lire les données audio
            import numpy as np
            donnees = np.frombuffer(self.flux_audio.read(1024, exception_on_overflow=False), dtype=np.int16)
            self.frames_audio.append(donnees)  # Ajouter les données dans le buffer

            self.affichage_spectre.delete("all")

            # Normaliser et afficher le spectre
            for i in range(0, 400, 4):
                y = int((donnees[i] / 32768.0) * 25 + 25)  # Normaliser pour un affichage dans la zone de 50 pixels
                self.affichage_spectre.create_line(i, 25, i, y, fill="black", width=2)

            # Répéter l'animation du spectre toutes les 50 ms
            self.racine.after(50, self.mettre_a_jour_spectre)

    def enregistrer_fichier_audio(self):
        """Enregistrer l'audio capturé dans un fichier WAV."""
        import numpy as np
        audio_complet = np.concatenate(self.frames_audio)
        enregistrer_audio(audio_complet)

    def afficher_signal_enregistre(self):
        """Afficher le signal audio du fichier WAV enregistré."""
        afficher_signal_enregistre()

    def analyser_et_afficher_couleur(self):
        """Analyser l'audio et afficher la couleur détectée."""
        couleur = obtenir_couleur_vocale()
        if couleur:
            self.affichage_couleur.config(bg=couleur)
        else:
            self.affichage_couleur.config(bg="white")


# Exécution de l'interface
if __name__ == "__main__":
    racine = tk.Tk()
    app = ApplicationDetecteurCouleur(racine)
    racine.mainloop()
