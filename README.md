# Projet_IMC

## Objectif
Le but de ce projet est de créer une application qui permet de calculer l'indice de masse corporelle (IMC) d'une personne. L'IMC est un indicateur qui permet d'évaluer la corpulence d'une personne. Il se calcule en fonction de la taille et du poids de la personne. L'IMC est défini par la formule suivante :

$$IMC = \frac{poids}{taille^2}$$

Au delà de l'IMC, l'application doit également donner une interprétation de l'IMC en fonction des valeurs suivantes :
1. Moins de 16.5 : Dénutrition ou famine
2. Entre 16.5 et 18.5 : Maigreur
3. Entre 18.5 et 25 : Corpulence normale
4. Entre 25 et 30 : Surpoids
5. Entre 30 et 35 : Obésité modérée
6. Entre 35 et 40 : Obésité sévère
7. Plus de 40 : Obésité morbide ou massive

Cette application est une plateforme sur laquelle l'on peut :
* Créer un compte utilisateur
* Se connecter

Une fois connecter, l'utilisateur peut :
* Modifier ses données personnelles
* Consulter son IMC
* Consulter son état de santé en fonction de son IMC

## BD : Système de fichier au format json
Tous les utilisateurs et leurs informations personnelles sont stockés dans le dossier [database](/database/).

**Structure de la base de données**
* [users.json](/database/users.json) contient la liste des utilisateurs enregistrés sur la plateforme avec leur ID
* [infos.json](/database/infos.json) contient toutes les informations personnelles de tous les utilisateurs enregistrée dans sur la plateforme
* [sante.json](/database/sante.json) contient le classement en fonction de l'IMC avec des appréciations
* [id_increment.json](/database/id_increment.json) contien le dernier ID utilisateur enregistré sur la plateforme qui est en même temps le plus grand ID dans la base de données. Cela permet de générer un nouvel ID pour un nouvel utilisateur en incrémentant de 1 le dernier ID enregistré.

Le fichier [test.py](/test.py) a permis d'alimenter le fichier [sante.json](/database/sante.json)

Le contenu du fichier [sante.json](/database/sante.json) est le même au format `plain text` avec l'encodage `utf-8` dans le fichier [sante_classement.txt](/sante_classement.txt)

Il est essentiel de changer la variable `ROOT_PATH `dans les fichiers [main.py](/main.py) et [test.py](/test.py) pour correspondre au chemin absolu du projet sur votre machine.