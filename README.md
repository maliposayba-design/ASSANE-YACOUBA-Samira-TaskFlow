# ASSANE-YACOUBA-Samira-TaskFlow
Application en console Python connectee a une base de donnees MySQL.
## Auteur
Samira Assane Yacouba - Licence Informatique 1 - Groupe ISI
## Technologies utilisees
- Python 3.13
- MySQL
- mysql-connector-python
## Prerequis
- Python 3.8 ou superieur
- MySQL installe et demarre
- pip install mysql-connector-python
## Installation et lancement
1. Cloner le depot
2. Creer la base de donnees en executant les scripts SQL
3. Adapter les parametres de connexion dans connexion.py
4. Lancer l'application : python main.py
## Fonctionnalites implementees
- [x] Connexion MySQL
- [x] Inscription utilisateur avec hashage SHA-256 
- [x] connexion et deconnexion utilisateur
- [x] Ajout et affichage des taches
- [x] modification et Changement de statut avec historique
- [ ] suppression des taches
- [ ] Filtres et recherche
- [ ] Gestion des categories
- [ ] Statistiques
## Structure du projet
taskflow/
+-- main.py
+-- connexion.py
+-- utilisateur.py
+-- tache.py
+-- categorie.py
+-- etiquette.py
+-- historique.py
+-- affichage.py
+-- README.md