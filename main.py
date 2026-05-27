from connexion import obtenir_connexion, fermer_connexion

conn = obtenir_connexion()

if conn:
    print("Test réussi !")
    fermer_connexion(conn)
    from affichage import *

vider_ecran()

afficher_succes("Connexion réussie")
afficher_info("Bienvenue dans TaskFlow")
afficher_alerte("Attention aux tâches urgentes")
afficher_erreur("Exemple d'erreur")

afficher_menu_principal("Samira")