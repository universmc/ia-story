from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch
from PIL import Image
import os

# Chemin vers le modèle et le processeur
model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

max_length = 16
num_beams = 4
gen_kwargs = {"max_length": max_length, "num_beams": num_beams}

# Chemin vers le répertoire des images
repertoire_img = 'database/rush/img/'
repertoire_md = 'database/rush/md/'

# Assurez-vous que le répertoire de sortie existe
os.makedirs(repertoire_md, exist_ok=True)

# Liste des fichiers d'images JPEG dans le répertoire
images = [f for f in os.listdir(repertoire_img) if f.endswith(".jpg")]

for nom_fichier_img in images:
    # Chemin complet de l'image
    chemin_image = os.path.join(repertoire_img, nom_fichier_img)

    # Lecture de l'image
    i_image = Image.open(chemin_image)
    if i_image.mode != "RGB":
        i_image = i_image.convert(mode="RGB")

    pixel_values = feature_extractor(images=[i_image], return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device)

    # Génération du texte à partir de l'image
    output_ids = model.generate(pixel_values, **gen_kwargs)
    preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    preds = [pred.strip() for pred in preds]

    # Création du texte à insérer dans le fichier .md
    titre = preds[0]
    description_metaphysique = preds[1]
    version_narrative = preds[2]

    # Écriture du contenu dans le fichier .md correspondant
    nom_fichier_md = os.path.splitext(nom_fichier_img)[0] + '.md'
    chemin_md = os.path.join(repertoire_md, nom_fichier_md)

    with open(chemin_md, 'w') as f:
        f.write(f"# {titre}\n\n")
        f.write(f"## {description_metaphysique}\n\n")
        f.write(f"## {version_narrative}\n\n")

# Le script traitera maintenant toutes les images du répertoire `rush/img/` et générera du texte spécifique à chaque image pour les fichiers `.md` correspondants.
