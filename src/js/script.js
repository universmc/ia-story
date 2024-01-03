// Sélectionnez les éléments DOM
const searchInput = document.getElementById("searchInput");
const searchButton = document.getElementById("searchButton");

// Ajoutez un gestionnaire d'événements pour la recherche
searchButton.addEventListener("click", () => {
    const searchTerm = searchInput.value;
    // Effectuez une action en fonction de la recherche (par exemple, affichez les résultats).
    console.log(`Vous avez recherché : ${searchTerm}`);
});

// Ajoutez un menu déroulant en JavaScript
const dropdownMenu = document.createElement("select");
const configMenu = document.querySelector("nav ul");

const option1 = document.createElement("option");
option1.text = "Option 1";
const option2 = document.createElement("option");
option2.text = "Option 2";
const option3 = document.createElement("option");
option3.text = "Option 3";

dropdownMenu.add(option1);
dropdownMenu.add(option2);
dropdownMenu.add(option3);

configMenu.appendChild(dropdownMenu);

// Ajoutez des actions en fonction des sélections dans le menu déroulant
dropdownMenu.addEventListener("change", (event) => {
    const selectedOption = event.target.value;
    // Effectuez une action en fonction de l'option sélectionnée.
    console.log(`Option sélectionnée : ${selectedOption}`);
});







// carrousel 
// Sélectionnez les éléments DOM
const carousel = document.querySelector('.carousel');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
let scrollValue = 0;
const imageWidth = 100; // Largeur d'une image en pourcentage
const scrollSpeed = 0.5; // Vitesse de défilement (plus petit = plus lent)

// Récupérez la div des images générées par PHP
const carouselImages = document.querySelector('.carousel-images');

// Récupération dynamique de la liste des fichiers .jpeg du répertoire avec PHP
fetch('https://oc.univers-mc.cloud/tmp/ia-story/database/rush/img')
    .then(response => response.text())
    .then(data => {
        // Analyse du contenu de la page pour extraire les noms des fichiers .jpeg
        const fileNames = data.match(/href="([^"]+\.jpeg)"/g)
            .map(match => match.match(/href="([^"]+\.jpeg)"/)[1]);
        
        // Création des éléments img pour chaque image et ajout au carrousel
        fileNames.forEach(fileName => {
            const imgElement = document.createElement('img');
            imgElement.src = `https://oc.univers-mc.cloud/tmp/ia-story/database/rush/img/${fileName}`;
            carouselImages.appendChild(imgElement);
        });

        // Ajout des écouteurs d'événements pour les boutons précédents et suivants
        prevBtn.addEventListener('click', scrollLeft);
        nextBtn.addEventListener('click', scrollRight);
    })
    .catch(error => console.error(error));

// Fonction pour faire défiler le carrousel à gauche
function scrollLeft() {
    scrollValue -= scrollSpeed;
    if (scrollValue < 0) {
        scrollValue = 0;
    }
    carousel.style.transform = `translateX(-${scrollValue}%)`;
}

// Fonction pour faire défiler le carrousel à droite
function scrollRight() {
    scrollValue += scrollSpeed;
    if (scrollValue > (100 - imageWidth)) {
        scrollValue = 0;
    }
    carousel.style.transform = `translateX(-${scrollValue}%)`;
}
