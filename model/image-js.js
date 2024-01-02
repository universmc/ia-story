const { Image } = require('image-js');
const fs = require('fs');
const path = require('path');

const repertoireRush = 'database/rush/';

// Lire le contenu du répertoire
fs.readdir(repertoireRush, async (err, fichiers) => {
  if (err) {
    console.error("Erreur lors de la lecture du répertoire :", err);
    return;
  }

  // Filtrer les fichiers pour ne conserver que les fichiers WebP
  const fichiersWebP = fichiers.filter(fichier => fichier.endsWith('.webp'));

  // Liste pour stocker les tensors SVG
  const tensorsSVG = [];

  // Charger et convertir toutes les images WebP en tensors SVG
  for (const fichierWebP of fichiersWebP) {
    const cheminImage = path.join(repertoireRush, fichierWebP);
    const image = new Image();
    await image.load(cheminImage);

    // Convertir limage en tensor SVG
    const tensorSVG = image.toSVG();
    tensorsSVG.push(tensorSVG);

    // Générer le fichier .md correspondant
    const cheminMD = path.join(repertoireRush, fichierWebP.replace('.webp', '.md'));
    const contenuMD = `Description pour ${fichierWebP}`; // À remplacer par la description générée
    fs.writeFileSync(cheminMD, contenuMD);
  }

  // À ce stade, la liste "tensorsSVG" contient les tensors SVG de toutes les images
  console.log('Tensors SVG des images chargés avec succès:', tensorsSVG);
});

