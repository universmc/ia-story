import os
import markdown_it

# Répertoire contenant les fichiers .md
repertoire_md = 'database/rush/md'

# Créer un analyseur Markdown
md = markdown_it.MarkdownIt()

# Parcourir tous les fichiers .md dans le répertoire
for fichier_md in os.listdir(repertoire_md):
    if fichier_md.endswith('.md'):
        chemin_md = os.path.join(repertoire_md, fichier_md)

        # Lire le contenu du fichier .md
        with open(chemin_md, 'r', encoding='utf-8') as fichier:
            contenu_md = fichier.read()

        # Analyser le contenu Markdown
        html_contenu = md.render(contenu_md)

        # Vous pouvez maintenant travailler sur la structure HTML résultante
        # ou effectuer des modifications au contenu Markdown ici

        # Afficher ou enregistrer les modifications (par exemple, en HTML)
        print(f'Fichier {fichier_md} converti en HTML :')
        print(html_contenu)
        print()

# Vous pouvez ajouter des manipulations supplémentaires au contenu Markdown
# ou à la structure HTML selon vos besoins.
