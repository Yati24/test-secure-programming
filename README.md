Jeu clicker avec failles de securité

utilisation de l’ia : utilisé pour m’aider à générer rapidement le back + le css + la base du
html et à mettre en forme la liste des failles sur ce texte. les failles quant à elles ont été
pensées et ajouté par moi même

Jeu de type clicker simple avec un bouton, un score, des users, et un leaderboard
failles de sécurités :

1. Clé Secrète en Dur
● Description : La clé de chiffrement des sessions est écrite directement dans le
fichier source.
● Risque : Permet à un attaquant de créer de faux cookies pour usurper l'identité de
n'importe quel utilisateur ou administrateur.
● Correction : Stocker la clé dans une variable d'environnement serveur, hors du code
source.
2. Mode Débogage Activé
● Description : L'application tourne avec les outils de développement actifs en
production.
● Risque : Affiche des détails techniques sensibles (chemins de fichiers, versions,
code source) en cas d'erreur, aidant un pirate à comprendre l'architecture.
● Correction : Désactiver impérativement le mode debug lors du déploiement final.
3. Stockage de Mots de Passe en Clair
● Description : Les mots de passe sont enregistrés tels quels dans la base de
données.
● Risque : En cas de vol de la base de données, tous les comptes utilisateurs sont
compromis immédiatement.
● Correction : Hacher (chiffrer via un algorithme irréversible) les mots de passe avant
de les stocker.
4. Injection SQL
● Description : Les données entrées par l'utilisateur sont insérées directement dans
les commandes de la base de données.
● Risque : Permet de contourner l'authentification sans mot de passe ou de
voler/supprimer toute la base de données.
● Correction : Utiliser des "requêtes préparées" pour séparer les commandes SQL
des données utilisateurs.
5. Identifiants par Défaut Faibles
● Description : Un compte administrateur existe avec un login/mot de passe prévisible
(admin/admin).
● Risque : Offre un accès total immédiat au système pour quiconque devine ces
identifiants standards.
● Correction : Supprimer les comptes par défaut ou forcer un mot de passe fort à
l'installation.
6. Cross-Site Scripting (XSS Stockée)
● Description : Le site affiche les noms d'utilisateurs sans filtrer les caractères
spéciaux (HTML/JS).
● Risque : Un script malveillant inséré dans un pseudo s'exécute sur le navigateur des
autres joueurs, pouvant voler leurs sessions.
● Correction : Échapper automatiquement les caractères spéciaux lors de l'affichage
des données.
7. Manque de Validation Côté Serveur (Confiance aveugle au client)
● Description : Le serveur accepte le score envoyé par le navigateur sans vérifier s'il
est cohérent.
● Risque : Un utilisateur peut modifier la requête pour s'attribuer un score infini sans
jouer (triche).
● Correction : Calculer la progression côté serveur et ne valider que les actions de
l'utilisateur, pas le résultat final.
