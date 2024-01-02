import os

repertoire_img = 'database/rush/img'
repertoire_md = 'database/rush/md'

# Créer le sous-répertoire 'md' s'il n'existe pas
os.makedirs(repertoire_md, exist_ok=True)

# Liste les fichiers JPEG dans le répertoire 'database/rush/img'
fichiers_jpeg = [fichier for fichier in os.listdir(repertoire_img) if fichier.endswith('.jpeg')]

for fichier_jpeg in fichiers_jpeg:
    # Générer le contenu Markdown correspondant
    titre = fichier_jpeg.replace('.jpeg', '')
    description = f'Description de {titre}'
    prompt = f'Prompt de {titre}'
    contenu_md = f'# {titre}\n\n{description}\n\nPrompt:\n\n{prompt}'

    # Enregistrer le fichier Markdown
    fichier_md = fichier_jpeg.replace('.jpeg', '.md')
    chemin_md = os.path.join(repertoire_md, fichier_md)
    with open(chemin_md, 'w') as fichier:
        fichier.write(contenu_md)

    print(f'Créé {fichier_md}')

print('Création des fichiers Markdown terminée.')
