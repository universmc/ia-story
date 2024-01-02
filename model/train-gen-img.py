import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import os

# Définir les paramètres d'entraînement
model_name = "gen-img"  # Remplacez par le nom du modèle pré-entraîné souhaité
output_dir = "output/"  # Répertoire où enregistrer les modèles générés
num_epochs = 10  # Nombre d'époques d'entraînement
batch_size = 32  # Taille du lot (batch size)
learning_rate = 1e-4  # Taux d'apprentissage

# Charger le modèle et le tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Définir les données d'entraînement (vous devrez adapter cette partie à votre ensemble de données)
train_dataset = ...  # Chargez vos données d'entraînement ici

# Créer le dataloader
train_dataloader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

# Définir l'optimiseur et la fonction de perte
optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)
criterion = torch.nn.CrossEntropyLoss()

# Boucle d'entraînement
for epoch in range(num_epochs):
    model.train()
    total_loss = 0
    for batch in train_dataloader:
        inputs = batch['input_ids'].to(device)
        labels = batch['labels'].to(device)
        
        optimizer.zero_grad()
        outputs = model(inputs, labels=labels)
        
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item()
    
    # Afficher la perte moyenne de l'époque
    average_loss = total_loss / len(train_dataloader)
    print(f"Époque {epoch+1}/{num_epochs} - Perte moyenne : {average_loss:.4f}")

    # Sauvegarder le modèle généré à la fin de chaque époque
    model.save_pretrained(os.path.join(output_dir, f'model_epoch_{epoch+1}'))

print("Entraînement terminé."
)
