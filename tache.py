from connexion import obtenir_connexion
from mysql.connector import Error
def ajouter_tache(id_user):

    titre = input("Titre : ")

    if titre.strip() == "":
        print("Le titre est obligatoire")
        return

    description = input("Description : ")

    print("Priorites disponibles :")
    print("1. basse")
    print("2. normale")
    print("3. haute")
    print("4. urgente")

    choix = input("Choisir une priorite : ")

    priorites = {
        "1": "basse",
        "2": "normale",
        "3": "haute",
        "4": "urgente"
    }

    priorite = priorites.get(choix)

    if priorite is None:
        print("Priorite invalide")
        return

    conn = None
    cursor = None

    try:
        conn = obtenir_connexion()

        if conn:
            cursor = conn.cursor()

            sql = """
            INSERT INTO TACHE
            (titre, description, priorite, id_user)
            VALUES (%s, %s, %s, %s)
            """

            valeurs = (
                titre,
                description,
                priorite,
                id_user
            )

            cursor.execute(sql, valeurs)

            conn.commit()

            print("Tache ajoutee avec succes")

    except Error as e:
        print(f"Erreur base de donnees : {e}")

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()

def lister_taches(id_user):

    conn = None
    cursor = None

    try:
        conn = obtenir_connexion()

        if conn:
            cursor = conn.cursor(dictionary=True)

            sql = """
            SELECT *
            FROM TACHE
            WHERE id_user = %s
            """

            cursor.execute(sql, (id_user,))

            taches = cursor.fetchall()

            return taches

    except Error as e:
        print(f"Erreur base de donnees : {e}")
        return []

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()

def recuperer_tache(id_tache, id_user):

    conn = None
    cursor = None

    try:
        conn = obtenir_connexion()

        if conn:
            cursor = conn.cursor(dictionary=True)

            sql = """
            SELECT *
            FROM TACHE
            WHERE id_tache = %s
            AND id_user = %s
            """

            valeurs = (id_tache, id_user)

            cursor.execute(sql, valeurs)

            tache = cursor.fetchone()

            return tache

    except Error as e:
        print(f"Erreur base de donnees : {e}")
        return None

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()