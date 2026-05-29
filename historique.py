from connexion import obtenir_connexion
from mysql.connector import Error


def consulter_historique(id_user):

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

            sql = """
            SELECT
                HISTORIQUE.*

            FROM HISTORIQUE

            INNER JOIN TACHE
            ON HISTORIQUE.id_tache =
               TACHE.id_tache

            WHERE TACHE.id_tache = %s
            AND TACHE.id_user = %s

            ORDER BY
            date_changement DESC
            """

            valeurs = (
                id_tache,
                id_user
            )

            cursor.execute(
                sql,
                valeurs
            )

            historique = cursor.fetchall()

            return historique

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