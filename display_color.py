import reconnaissance_vocal
import matplotlib.pyplot as plt

def affichage_couleur() :
    couleur = reconnaissance_vocal.reconnaissance_vocal()
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
    if couleur in couleurs:
        # Création d'une figure avec la couleur sélectionnée
        plt.figure(figsize=(4, 4))
        plt.title(f"Couleur détectée : {couleur.capitalize()}")
        plt.gca().add_patch(plt.Rectangle((0, 0), 1, 1, color=couleurs[couleur]))
        plt.axis("off")
        plt.show()
    else:
        print("Couleur non reconnue.")

affichage_couleur()

