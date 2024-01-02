# Lire le contenu du fichier episodes.txt
with open('episodes.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Séparer le contenu en épisodes en utilisant la chaîne "Episode X - "
episodes = content.split("Episode ")

# Supprimer le premier élément de la liste, car il ne contient pas d'épisode
episodes.pop(0)

# Parcourir chaque épisode et créer un fichier Markdown correspondant
for i, episode in enumerate(episodes, start=1):
    # Diviser chaque épisode en titre, description métaphysique et version narrative
    parts = episode.split("\n")

    # Extraire le titre de l'épisode
    title = parts[0].strip()

    # Extraire la description métaphysique de l'épisode
    metaphysical_description = parts[1].strip()

    # Extraire la version narrative de l'épisode
    narrative_version = "\n".join(parts[2:]).strip()

    # Créer le contenu du fichier Markdown
    markdown_content = f"# {title}\n\n"
    markdown_content += f"**Description Métaphysique:** {metaphysical_description}\n\n"
    markdown_content += f"**Version Narrative:**\n{narrative_version}"

    # Enregistrer le contenu dans un fichier Markdown
    filename = f"ia_story_episode{i}.md"
    with open(filename, 'w', encoding='utf-8') as md_file:
        md_file.write(markdown_content)

    print(f"Fichier Markdown pour l'Épisode {i} créé : {filename}")

print("Conversion terminée.")
