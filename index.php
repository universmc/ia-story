<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IA-Story Dashboard</title>
    <!-- Lien vers le fichier CSS pour la mise en page -->
    <link rel="stylesheet" href="src/css/style.css">
</head>
<body>
    <!-- En-tête de la page -->
    <header>
        <!-- Menu de navigation -->
        <nav>
            <ul>
                <li><a href="#">Accueil</a></li>
                <li><a href="#">Épisodes</a></li>
                <li><a href="#">À Propos</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
            <!-- Prompt de recherche -->
            <div class="search-prompt">
                <input type="text" id="search-input" placeholder="Rechercher...">
                <button id="search-button">Rechercher</button>
            </div>
             <!-- Accès à usr/config -->
            <div class="user-config">
                <a href="usr/config">Configuration</a>
            </div>
        </nav>

    </header>
    
    <!-- Section du héros avec le carrousel d'images -->
    <section class="hero-banner">
        <div class="carousel">
                <div class="carousel-images">
                    <?php
                    // Chemin vers le répertoire des images
                    $repertoireImages = 'database/rush/img/';

                    // Ouvrir le répertoire
                    $dir = opendir($repertoireImages);

                    // Parcourir les fichiers du répertoire
                    while (($file = readdir($dir)) !== false) {
                        // Vérifier si le fichier est une image JPEG
                        if (pathinfo($file, PATHINFO_EXTENSION) === 'jpeg') {
                            // Afficher l'image
                            echo '<div class="slider">';
                            echo '<img src="' . $repertoireImages . $file . '" alt="Image">' . PHP_EOL;
                            echo '</div>';
                        }
                    }

                    // Fermer le répertoire
                    closedir($dir);
                    ?>
                </div>
            <!-- Insérez ici les images du carrousel depuis le répertoire database/rush/img/ -->
        </div>
        <button id="prevBtn">Précédent</button>
        <button id="nextBtn">Suivant</button>
    </section>
    <!-- Section principale du tableau de bord -->
    <main>
        <!-- Insérez ici le contenu du tableau de bord, comme les épisodes, les images, etc. -->
    </main>

    <!-- Pied de page de la page -->
    <footer>
        <p>&copy; 2024 IA-Story. Tous droits réservés.</p>
    </footer>

    <!-- Lien vers le fichier JavaScript pour les fonctionnalités dynamiques -->
    <script src="src/js/script.js"></script>
</body>
</html>
