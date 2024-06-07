# 164_fleetranger_tbu

## Sommaire

Voici toutes les étapes nécessaires à l'exécution de mon application.

- [Cahiers des charges](#cahiers-des-charges)
- [Import du projet GitHub](#import-du-projet-github)
- [Docker](#docker)
- [Installation de tous les paquets](#installation-de-tous-les-paquets)
- [Import dump base de données](#import-dump-base-de-données)
- [Lancer mon application](#lancer-mon-application)
- [Documentation](#documentation)

## Cahiers des charges
Mon projet portera sur une base de données réencensant l’intégralité des véhicules (camion, camionnette, voiture) d’une entreprise dans le but géré facilement leurs flottes.<br>
<br>
Dans cette base on y retrouvera :
 
- Type de véhicule 
- Marque et modèle
- Numéro de châssis
- Dernière expertise/control technique  
- Dernier service
- Numéro de véhicule
- Chauffeur attitré 
- Km totaux 
- Factures du véhicule
- etc…

Tout cela aura pour but de faciliter le travail rébarbatif et long de devoir constamment se rappeler ou vérifier ces informations manuellement.
 
Ce projet se fera sur une page web HTML dans laquelle un script Python (Flask) s’occupera de faire les requêtes à la base de données en MySql.
 
*- Après la fin de mon projet, qui va utiliser mon "site" avec ma base de données ?*<br>
<br>
•	Mon but serait de le mettre en ligne pour la suite, pour que toute entreprise possédant une flotte de véhicules, puisse y avoir accès et l’utiliser.<br>

*- Qui va entrer les données dans ma base de données par l'intermédiaire de mon interface utilisateur ?*<br>
<br>
•	Toute entreprise ayant besoin de mon application.

## Import du projet GitHub 

Pour importer mon projet sur votre machine, il vous suffit de rentrer cette commande dans un terminal :

```
cd [chemin ou vous voulez cloner le projet]
git clone https://github.com/PepitoSir/164_fleetranger_tbu.git
```

## Docker

Pour lancer la base de données de mon projet, veuillez utiliser docker desktop. Voici comment l'installer depuis un terminal.<br>

Avec winget :
```
winget install -e --id Docker.DockerDesktop
```
Avec homebrew :
```
brew install docker
```
Ou directement sur leur site -> [Docker.com](https://www.docker.com/products/docker-desktop/)

Ouvrez le projet, puis dans le terminal de PyCharm, exécuter la commande :

```bash
docker-compose up -d
```

Celle là va exécuter le fichier `docker-compose.yml` qui va créer un container avec une base de données MySQL et un container avec un serveur MariaDB.


## Installation de tous les paquets

Dans le but de posséder tous les paquets et dépendances python requisent pour exécuter le projet, ouvrez votre terminal et entrer-y la commande suivante :

PowerShell :
```
python -m venv .venv
.\.venv\Scripts\Activate
pip install -r requirements.txt
```

Bash :
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Un message vous disant que tout est installé devrait s'afficher.

## Import dump base de données

Pour importer la base données veuillez vous rendre `164_fleetranger_tbu/APP_FILMS_164/database/1_ImportationDumpSql.py`. Arrivé dans ce fichier, il faudra l'exécuter, soit en faisant la combinaison de touche `CTRL + SHIFT + F10` soit en cliquant directement sur logo **run** (▶️) dans PyCharm.

Vous pouvez tester la connecxion à la base de données en exécutant le script `2_test_connection_bd.py`se trouvant dans le même répertoire.

## Lancer mon application

Pour que l'application flask se lance rendez-vous dans le fichier `164_fleetranger_tbu/run_mon_app.py` et exécutez le avec  la combinaison de touche `CTRL + SHIFT + F10` soit en cliquant directement sur logo **run** (▶️) dans PyCharm.

Dans le terminal de PyCharm, celui ci devrait vous afficher que l'application est bien lancée et vous donner un adresse IP qui devrait être `http://127.0.0.1:5000`, cliquer sur le lien dans le terminal et une page web devrait s'ouvrir dans votre navigateur avec l'application exécutée.

Pour stoper l'application faites la combinaison de touche `CTRL+C` ou cliquer sur l'icon stop en haut à droite.

  [---->Documentation<----]()

Celle là se trouve aussi dans le projet GitHub.
