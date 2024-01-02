from PIL import Image
import os

repertoire_rush = 'database/rush'
repertoire_img = os.path.join(repertoire_rush, 'img')

# Créer le sous-répertoire 'img' s'il n'existe pas
os.makedirs(repertoire_img, exist_ok=True)

# Liste les fichiers WebP dans le répertoire 'database/rush'
fichiers_webp = [fichier for fichier in os.listdir(repertoire_rush) if fichier.endswith('.webp')]

for fichier_webp in fichiers_webp:
    chemin_webp = os.path.join(repertoire_rush, fichier_webp)
    image = Image.open(chemin_webp)
    
    # Convertir l'image WebP en JPEG
    fichier_jpeg = fichier_webp.replace('.webp', '.jpeg')
    chemin_jpeg = os.path.join(repertoire_img, fichier_jpeg)
    image.save(chemin_jpeg, 'JPEG')

    print(f'Converti {fichier_webp} en {fichier_jpeg}')

print('Conversion terminée.')
