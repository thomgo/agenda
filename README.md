# Agenda pour terminal en python orienté objet

Il s'agit d'une application développée dans le cadre de mon poste de formateur en programmation et plus particulièrement pour l'élaboration d'un programme d'apprentissage du python. L'objectif est que les apprenants produisent une application complète sans interface graphique intégrant une base de données PostgreSQL permettant de gérer un agenda simple avec des événements.

Au travers de cet exercice, ils apprennent à :
- Utiliser et redéfinir des méthodes spéciales
- Utiliser les attributs et les méthodes de classe
- Organiser leur code selon un embryon de pattern MVC
- Créer une base de données
- Créer une table
- Executer les opérations du CRUD
- Utiliser la librairie Psycopg2
- Sécuriser ses données et les inputs utilisateurs

## Consignes

Développeur freelance, vous avez été contacté par Madame Derieux, médecin généraliste qui a besoin de vos services. Madame Derieux est très occupée entre son métier et ses nombreuses activités. Elle a souvent des difficultés à gérer son agenda et son emploi du temps. Comme tous les scientifiques, elle est tournée vers les nouvelles technologies et voudrait quelque chose de plus performant qu'un agenda papier. Elle voudrait utiliser cette dernière technologie dont tout le monde parle : l'ordinateur ! Votre mission sera donc de lui développer une application pour son terminal qui fonctionnera comme un agenda et lui permettra d'organiser son emploi du temps.

Spécifications fonctionnelles :
- La page d'accueil affiche la date du jour et le calendrier du mois en cours
- L'utilisateur peut voir le calendrier du mois suivant et du mois précédent
- L'utilisateur peut voir tous les événements d'une date précise
- L'utilisateur peut annuler (supprimer) un événement enregistré dans l'agenda
- L'utilisateur peut ajouter un événement dans l'agenda
- L'utilisateur peut modifier les caractéristiques d'un événement déjà enregistré dans l'agenda
- Deux événements ne peuvent pas avoir lieu le même jour à la même heure
- Un événement est composé obligatoirement d'un titre, d'une date, d'une heure et éventuellement d'une description

Spécifications techniques :
- Langage Python 3
- Organisation du code selon le principe MVC
- Usage de la programmation orientée objet
- Respect du principe DRY
- Essayer de respecter certains des principes SOLID
- Programme exécutable par le lancement d'un fichier main.py
- Intégration d'une base de données PostgreSQL via la librairie Psycopg2
- Utilisation du module Calendar

## Pour aller plus loin

Vous pouvez, si vous le souhaitez, rajouter des fonctionnalités à votre application comme par exemple :
- Une vérification stricte des données rentrées par l'utilisateur dans les inputs (validité du format des dates, heures, absence de caractères spéciaux...)
- Une gestion plus fine de l'expérience utilisateur. Par exemple que se passe-t-il l'utilisateur cherche à modifier un événement non-existant ?
- Transformer votre application en agenda partagé pour plusieurs personnes avec la possibilité de créer des comptes personnels
