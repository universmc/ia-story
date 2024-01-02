import os
from PIL import Image
from sentence_transformers import SentenceTransformer, util

# Modèle Sentence-Transformers pré-entraîné
model_name = 'sentence-transformers/all-MiniLM-L6-v2'
model = SentenceTransformer(model_name)

# Répertoire d'images d'entrée
repertoire_img = 'database/rush/img/'

# Répertoire de sortie pour les fichiers .md
repertoire_md = 'database/rush/md/'

# Parcours de toutes les images dans le répertoire
for nom_fichier_img in os.listdir(repertoire_img):
    if nom_fichier_img.endswith('.jpeg'):
        chemin_img = os.path.join(repertoire_img, nom_fichier_img)

        # Chargement de l'image
        img = Image.open(chemin_img)

        # Utilisation de Sentence-Transformers pour générer le texte
        titre = "Titre généré pour " + nom_fichier_img
        description_metaphysique = "Description métaphysique générée pour " + nom_fichier_img
        version_narrative = "Version narrative générée pour " + nom_fichier_img

        # Création du contenu .md
        contenu_md = f"# {titre}\n\n"
        contenu_md += f"## Description métaphysique\n{description_metaphysique}\n\n"
        contenu_md += f"## Version narrative\n{version_narrative}\n"

        # Enregistrement dans un fichier .md correspondant
        nom_fichier_md = nom_fichier_img.replace('.jpeg', '.md')
        chemin_md = os.path.join(repertoire_md, nom_fichier_md)

        with open(chemin_md, 'w') as fichier_md:
            fichier_md.write(contenu_md)

print("Génération des fichiers .md terminée.")
