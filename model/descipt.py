import os

repertoire_rush = "database/rush"
fichiers_webp = [fichier for fichier in os.listdir(repertoire_rush) if fichier.endswith(".webp")]

from PIL import Image

images = []
descriptions = []

for fichier_webp in fichiers_webp:
    chemin_fichier = os.path.join(repertoire_rush, fichier_webp)
    images.append(Image.open(chemin_fichier))

    # Assurez-vous d'avoir un fichier md correspondant au nom du fichier WebP
    fichier_md = os.path.join(repertoire_rush, fichier_webp.replace(".webp", ".md"))
    with open(fichier_md, "r") as fichier:
        descriptions.append(fichier.read())

class DataLoader:
    def __init__(self, images, descriptions):
        self.images = images
        self.descriptions = descriptions
        self.num_samples = len(images)

    def __len__(self):
        return self.num_samples

    def __getitem__(self, idx):
        image = self.images[idx]
        description = self.descriptions[idx]
        return image, description

dataloader = DataLoader(images, descriptions)

for image, description in dataloader:
    # Traitez les images et les descriptions comme nécessaire
    print(description)
