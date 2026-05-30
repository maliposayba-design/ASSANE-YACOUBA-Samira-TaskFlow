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

from connexion import obtenir_connexion
from mysql.connector import Error


def statistiques_personnelles(id_user):

    conn = None
    cursor = None

    try:
        conn = obtenir_connexion()

        if conn:

            cursor = conn.cursor(
                dictionary=True
            )

            sql_total = """
            SELECT COUNT(*) AS total
            FROM TACHE
            WHERE id_user = %s
            """

            cursor.execute(
                sql_total,
                (id_user,)
            )

            total = cursor.fetchone()["total"]

            sql_statut = """
            SELECT
                statut,
                COUNT(*) AS nombre

            FROM TACHE

            WHERE id_user = %s

            GROUP BY statut
            """

            cursor.execute(
                sql_statut,
                (id_user,)
            )

            stats_statut = cursor.fetchall()

            sql_priorite = """
            SELECT
                priorite,
                COUNT(*) AS nombre

            FROM TACHE

            WHERE id_user = %s

            GROUP BY priorite
            """

            cursor.execute(
                sql_priorite,
                (id_user,)
            )

            stats_priorite = cursor.fetchall()

            sql_terminees = """
            SELECT COUNT(*) AS terminees
            FROM TACHE
            WHERE id_user = %s
            AND statut = 'terminee'
            """

            cursor.execute(
                sql_terminees,
                (id_user,)
            )

            terminees = (
                cursor.fetchone()["terminees"]
            )

            taux_completion = 0

            if total > 0:

                taux_completion = (
                    terminees / total
                ) * 100

            return {
                "total": total,
                "statut": stats_statut,
                "priorite": stats_priorite,
                "taux_completion":
                taux_completion
            }

    except Error as e:

        print(
            f"Erreur base de donnees : {e}"
        )

        return None

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()