import hashlib

from connexion import obtenir_connexion
from mysql.connector import Error

def hasher_mdp(mot_de_passe):
    return hashlib.sha256(mot_de_passe.encode()).hexdigest()

def verifier_mdp(mot_de_passe_saisi, hash_stocke):
    return hasher_mdp(mot_de_passe_saisi) == hash_stocke

def utilisateur_existe(nom_utilisateur):

    conn = None
    cursor = None

    try:
        conn = obtenir_connexion()

        if conn:
            cursor = conn.cursor(dictionary=True)

            sql = """
            SELECT * FROM utilisateur
            WHERE nom_utilisateur = %s
            """

            cursor.execute(sql, (nom_utilisateur,))

            utilisateur = cursor.fetchone()

            return utilisateur is not None

    except Error as e:
        print(f"Erreur base de donnees : {e}")
        return False

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()

def recuperer_utilisateur(nom_utilisateur):

    conn = None

    cursor = None

    try:
        conn = obtenir_connexion()

        if conn:
            cursor = conn.cursor(dictionary=True)

            sql = """
            SELECT * FROM UTILISATEUR
            WHERE nom_utilisateur = %s
            """

            cursor.execute(sql, (nom_utilisateur,))

            utilisateur = cursor.fetchone()

            return utilisateur

    except Error as e:
        print(f"Erreur base de donnees : {e}")
        return None

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()

def connecter_utilisateur():

    nom_utilisateur = input("Nom d'utilisateur : ")
    mot_de_passe = input("Mot de passe : ")

    utilisateur = recuperer_utilisateur(nom_utilisateur)

    if utilisateur is None:
        print("Utilisateur introuvable")
        return None

    if verifier_mdp(mot_de_passe, utilisateur["mot_de_passe"]):
        print("Connexion reussie")
        return utilisateur

    print("Mot de passe incorrect")
    return None

def inscrire_utilisateur():

    nom_utilisateur = input("Nom d'utilisateur : ")
    email = input("Email : ")

    mot_de_passe = input("Mot de passe : ")
    confirmation = input("Confirmer le mot de passe : ")

    if mot_de_passe != confirmation:
        print("Les mots de passe ne correspondent pas")
        return

    if utilisateur_existe(nom_utilisateur):
        print("Ce nom d'utilisateur existe deja")
        return

    conn = None
    cursor = None

    try:
        conn = obtenir_connexion()

        if conn:
            cursor = conn.cursor()

            hash_mdp = hasher_mdp(mot_de_passe)

            sql = """
            INSERT INTO utilisateur
            (nom_utilisateur, email, mot_de_passe)
            VALUES (%s, %s, %s)
            """

            valeurs = (nom_utilisateur, email, hash_mdp)

            cursor.execute(sql, valeurs)

            conn.commit()

            print("Utilisateur inscrit avec succes")

    except Error as e:
        print(f"Erreur base de donnees : {e}")

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()

def deconnecter_utilisateur():
    print("Deconnexion reussie")
    return None       