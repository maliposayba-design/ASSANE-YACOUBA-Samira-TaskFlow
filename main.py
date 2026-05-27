from connexion import obtenir_connexion, fermer_connexion

conn = obtenir_connexion()

if conn:
    print("Test réussi !")
    fermer_connexion(conn)