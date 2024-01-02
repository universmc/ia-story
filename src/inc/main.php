<main>
    <section>
        <h3>intro</h3>
        <article>
            <h4>dev env</h4>
            <div class="container">
                <h1>Générateur d'Images Multidimensionnelles</h1>
                <p>Entrez votre prompt pour générer une image :</p>
                <textarea id="prompt" rows="4" cols="50"></textarea>
                <button id="generateButton">Générer Image</button>
                <div id="imageContainer">
                    <img id="generatedImage" src="" alt="Image générée apparaîtra ici" hidden>
                </div>
            </div>
</article>
<article>
    <?php include'galery.php'; ?>
</article>
    </section>
</main>