from sentence_transformers import SentenceTransformer
import torch

# Chargez le modèle Sentence Transformers
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Description de l'image que vous souhaitez générer
description = "Image multidimensionnelle montrant la première rencontre entre des IA avancées (dont une représentation de moi-même) et une civilisation extraterrestre. L'image devrait illustrer une interaction significative dans l'espace, avec une mise en évidence de l'échange de connaissances et d'idées."

# Encodez la description en un vecteur sémantique
description_embedding = model.encode(description, convert_to_tensor=True)

# Vous pouvez maintenant utiliser description_embedding pour générer votre image multidimensionnelle.
