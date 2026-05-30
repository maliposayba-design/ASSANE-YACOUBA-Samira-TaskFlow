from connexion import obtenir_connexion
from mysql.connector import Error


def creer_categorie(id_user):

    nom_categorie = input(
        "Nom de la categorie : "
    )
    if nom_categorie.strip() == "":
     print("Nom categorie obligatoire")
     return

    print("\nCouleurs disponibles :")
    print("1. rouge")
    print("2. bleu")
    print("3. vert")
    print("4. jaune")
    print("5. magenta")
    print("6. cyan")

    choix = input("Choisir une couleur : ")

    couleurs = {
        "1": "rouge",
        "2": "bleu",
        "3": "vert",
        "4": "jaune",
        "5": "magenta",
        "6": "cyan"
    }

    couleur = couleurs.get(choix)

    if couleur is None:
        print("Couleur invalide")
        return

    conn = None
    cursor = None

    try:
        conn = obtenir_connexion()

        if conn:
            cursor = conn.cursor()

            sql = """
            INSERT INTO CATEGORIE
            (nom_categorie, couleur, id_user)
            VALUES (%s, %s, %s)
            """

            valeurs = (
                nom_categorie,
                couleur,
                id_user
            )

            cursor.execute(sql, valeurs)

            conn.commit()

            print("Categorie creee avec succes")

    except Error as e:
        print(f"Erreur base de donnees : {e}")

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()
def lister_categories(id_user):

    conn = None
    cursor = None

    try:
        conn = obtenir_connexion()

        if conn:
            cursor = conn.cursor(dictionary=True)

            sql = """
            SELECT
                CATEGORIE.id_categorie,
                CATEGORIE.nom_categorie,
                CATEGORIE.couleur,
                COUNT(TACHE.id_tache)
                AS nombre_taches

            FROM CATEGORIE

            LEFT JOIN TACHE
            ON CATEGORIE.id_categorie =
               TACHE.id_categorie

            WHERE CATEGORIE.id_user = %s

            GROUP BY
                CATEGORIE.id_categorie,
                CATEGORIE.nom_categorie,
                CATEGORIE.couleur
            """

            cursor.execute(sql, (id_user,))

            categories = cursor.fetchall()

            return categories

    except Error as e:
        print(f"Erreur base de donnees : {e}")
        return []

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()
def supprimer_categorie(id_user):

    id_categorie = input(
        "ID de la categorie a supprimer : "
    )

    conn = None
    cursor = None

    try:
        conn = obtenir_connexion()

        if conn:
            cursor = conn.cursor(dictionary=True)

            sql_select = """
            SELECT *
            FROM CATEGORIE
            WHERE id_categorie = %s
            AND id_user = %s
            """

            valeurs_select = (
                id_categorie,
                id_user
            )

            cursor.execute(
                sql_select,
                valeurs_select
            )

            categorie = cursor.fetchone()

            if categorie is None:
                print("Categorie introuvable")
                return

            print(
                f"Categorie : "
                f"{categorie['nom_categorie']}"
            )

            confirmation = input(
                "Confirmer la suppression ? (o/n) : "
            )

            if confirmation.lower() != "o":
                print("Suppression annulee")
                return

            sql_delete = """
            DELETE FROM CATEGORIE
            WHERE id_categorie = %s
            AND id_user = %s
            """

            valeurs_delete = (
                id_categorie,
                id_user
            )

            cursor.execute(
                sql_delete,
                valeurs_delete
            )

            conn.commit()

            print(
                "Categorie supprimee avec succes"
            )

    except Error as e:
        print(f"Erreur base de donnees : {e}")

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()