from connexion import obtenir_connexion
from mysql.connector import Error


def creer_etiquette(id_user):

    nom_etiquette = input(
        "Nom de l'etiquette : "
    )
    
    if nom_etiquette.strip() == "":
      print ("Nom etiquette obligatoire")
    return
    conn = None
    cursor = None

    try:
        conn = obtenir_connexion()

        if conn:

            cursor = conn.cursor()

            sql = """
            INSERT INTO ETIQUETTE
            (nom_etiquette, id_user)
            VALUES (%s, %s)
            """

            valeurs = (
                nom_etiquette,
                id_user
            )

            cursor.execute(sql, valeurs)

            conn.commit()

            print(
                "Etiquette creee avec succes"
            )

    except Error as e:

        print(
            f"Erreur base de donnees : {e}"
        )

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()

def lister_etiquettes(id_user):

    conn = None
    cursor = None

    try:
        conn = obtenir_connexion()

        if conn:

            cursor = conn.cursor(
                dictionary=True
            )

            sql = """
            SELECT *
            FROM ETIQUETTE
            WHERE id_user = %s
            """

            cursor.execute(
                sql,
                (id_user,)
            )

            etiquettes = cursor.fetchall()

            return etiquettes

    except Error as e:

        print(
            f"Erreur base de donnees : {e}"
        )

        return []

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()

def ajouter_etiquette_tache(id_user):

    id_tache = input(
        "ID de la tache : "
    )

    etiquettes = lister_etiquettes(id_user)

    if not etiquettes:

        print("Aucune etiquette disponible")
        return

    print("\nEtiquettes disponibles :")

    for etiquette in etiquettes:

        print(
            f"{etiquette['id_etiquette']} - "
            f"{etiquette['nom_etiquette']}"
        )

    id_etiquette = input(
        "Choisir ID etiquette : "
    )

    conn = None
    cursor = None

    try:
        conn = obtenir_connexion()

        if conn:

            cursor = conn.cursor()

            sql = """
            INSERT INTO TACHE_ETIQUETTE
            (id_tache, id_etiquette)
            VALUES (%s, %s)
            """

            valeurs = (
                id_tache,
                id_etiquette
            )

            cursor.execute(sql, valeurs)

            conn.commit()

            print(
                "Etiquette ajoutee a la tache"
            )

    except Error as e:

        print(
            f"Erreur base de donnees : {e}"
        )

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()

def retirer_etiquette_tache():

    id_tache = input(
        "ID de la tache : "
    )

    conn = None
    cursor = None

    try:
        conn = obtenir_connexion()

        if conn:

            cursor = conn.cursor(
                dictionary=True
            )

            sql_select = """
            SELECT
                ETIQUETTE.id_etiquette,
                ETIQUETTE.nom_etiquette

            FROM ETIQUETTE

            INNER JOIN TACHE_ETIQUETTE
            ON ETIQUETTE.id_etiquette =
               TACHE_ETIQUETTE.id_etiquette

            WHERE TACHE_ETIQUETTE.id_tache = %s
            """

            cursor.execute(
                sql_select,
                (id_tache,)
            )

            etiquettes = cursor.fetchall()

            if not etiquettes:

                print(
                    "Aucune etiquette "
                    "sur cette tache"
                )

                return

            print(
                "\nEtiquettes de la tache :"
            )

            for etiquette in etiquettes:

                print(
                    f"{etiquette['id_etiquette']} - "
                    f"{etiquette['nom_etiquette']}"
                )

            id_etiquette = input(
                "ID etiquette a retirer : "
            )

            sql_delete = """
            DELETE FROM TACHE_ETIQUETTE
            WHERE id_tache = %s
            AND id_etiquette = %s
            """

            valeurs = (
                id_tache,
                id_etiquette
            )

            cursor.execute(
                sql_delete,
                valeurs
            )

            conn.commit()

            print(
                "Etiquette retiree "
                "avec succes"
            )

    except Error as e:

        print(
            f"Erreur base de donnees : {e}"
        )

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()