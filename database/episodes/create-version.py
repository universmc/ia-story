import os
import shutil
from datetime import datetime

# Obtenez la date et l'heure actuelles
current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Créez un répertoire de sauvegarde pour stocker les anciennes versions
backup_dir = 'versions'
os.makedirs(backup_dir, exist_ok=True)

# Liste des fichiers .md à sauvegarder
md_files = [f for f in os.listdir() if f.endswith('.md')]

# Copiez chaque fichier .md dans le répertoire de sauvegarde avec un nouveau nom
for md_file in md_files:
    # Construisez le nom du fichier de sauvegarde en ajoutant la date et l'heure
    backup_file = os.path.join(backup_dir, f"{md_file.replace('.md', '')}_{current_datetime}.md")

    # Copiez le fichier .md dans le répertoire de sauvegarde
    shutil.copy(md_file, backup_file)

print("Versions créées avec succès.")
