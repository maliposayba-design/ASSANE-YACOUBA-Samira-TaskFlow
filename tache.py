from connexion import obtenir_connexion
from mysql.connector import Error
def ajouter_tache(id_user):

    titre = input("Titre : ")

    if titre.strip() == "":
        print("Le titre est obligatoire")
        return

    description = input("Description : ")

    date_echeance = input("Date d'echeance (AAAA-MM-JJ) : ")
    
    if date_echeance.strip() == "":
       date_echeance = None

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
            (titre, description, date_echeance, priorite, id_user)
            VALUES (%s, %s, %s, %s, %s)
            """

            valeurs = (
                titre,
                description,
                date_echeance,
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

def modifier_tache(id_user):

    id_tache = input("ID de la tache a modifier : ")

    tache = recuperer_tache(id_tache, id_user)

    if tache is None:
        print("Tache introuvable")
        return

    print("\nValeurs actuelles :")
    print(f"Titre : {tache['titre']}")
    print(f"Description : {tache['description']}")
    print(f"Priorite : {tache['priorite']}")
    print(f"Date echeance : {tache['date_echeance']}")

    nouveau_titre = input("Nouveau titre : ")
    nouvelle_description = input("Nouvelle description : ")
    nouvelle_date = input(
        "Nouvelle date echeance (AAAA-MM-JJ) : "
    )

    print("Priorites disponibles :")
    print("1. basse")
    print("2. normale")
    print("3. haute")
    print("4. urgente")

    choix = input("Nouvelle priorite : ")

    priorites = {
        "1": "basse",
        "2": "normale",
        "3": "haute",
        "4": "urgente"
    }

    nouvelle_priorite = priorites.get(
        choix,
        tache["priorite"]
    )

    if nouveau_titre.strip() == "":
        nouveau_titre = tache["titre"]

    if nouvelle_description.strip() == "":
        nouvelle_description = tache["description"]

    if nouvelle_date.strip() == "":
        nouvelle_date = tache["date_echeance"]

    conn = None
    cursor = None

    try:
        conn = obtenir_connexion()

        if conn:
            cursor = conn.cursor()

            sql = """
            UPDATE TACHE
            SET titre = %s,
                description = %s,
                date_echeance = %s,
                priorite = %s
            WHERE id_tache = %s
            AND id_user = %s
            """

            valeurs = (
                nouveau_titre,
                nouvelle_description,
                nouvelle_date,
                nouvelle_priorite,
                id_tache,
                id_user
            )

            cursor.execute(sql, valeurs)

            conn.commit()

            print("Tache modifiee avec succes")

    except Error as e:
        print(f"Erreur base de donnees : {e}")

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()
def changer_statut_tache(id_user):

    id_tache = input("ID de la tache : ")

    tache = recuperer_tache(id_tache, id_user)

    if tache is None:
        print("Tache introuvable")
        return

    ancien_statut = tache["statut"]

    print(f"Statut actuel : {ancien_statut}")

    print("\nStatuts disponibles :")
    print("1. a_faire")
    print("2. en_cours")
    print("3. terminee")
    print("4. annulee")

    choix = input("Choisir le nouveau statut : ")

    statuts = {
        "1": "a_faire",
        "2": "en_cours",
        "3": "terminee",
        "4": "annulee"
    }

    nouveau_statut = statuts.get(choix)

    if nouveau_statut is None:
        print("Statut invalide")
        return

    conn = None
    cursor = None

    try:
        conn = obtenir_connexion()

        if conn:
            cursor = conn.cursor()

            sql_update = """
            UPDATE TACHE
            SET statut = %s
            WHERE id_tache = %s
            AND id_user = %s
            """

            valeurs_update = (
                nouveau_statut,
                id_tache,
                id_user
            )

            cursor.execute(
                sql_update,
                valeurs_update
            )

            sql_historique = """
            INSERT INTO HISTORIQUE
            (id_tache, ancien_statut, nouveau_statut)
            VALUES (%s, %s, %s)
            """

            valeurs_historique = (
                id_tache,
                ancien_statut,
                nouveau_statut
            )

            cursor.execute(
                sql_historique,
                valeurs_historique
            )

            conn.commit()

            print("Statut modifie avec succes")

    except Error as e:
        print(f"Erreur base de donnees : {e}")

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()

def supprimer_tache(id_user):

    id_tache = input("ID de la tache a supprimer : ")

    tache = recuperer_tache(id_tache, id_user)

    if tache is None:
        print("Tache introuvable")
        return

    print(f"Titre : {tache['titre']}")

    confirmation = input(
        "Confirmer la suppression ? (o/n) : "
    )

    if confirmation.lower() != "o":
        print("Suppression annulee")
        return

    conn = None
    cursor = None

    try:
        conn = obtenir_connexion()

        if conn:
            cursor = conn.cursor()

            sql = """
            DELETE FROM TACHE
            WHERE id_tache = %s
            AND id_user = %s
            """

            valeurs = (
                id_tache,
                id_user
            )

            cursor.execute(sql, valeurs)

            conn.commit()

            print("Tache supprimee avec succes")

    except Error as e:
        print(f"Erreur base de donnees : {e}")

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()

def filtrer_taches_statut(id_user):

    print("\nStatuts disponibles :")
    print("1. a_faire")
    print("2. en_cours")
    print("3. terminee")
    print("4. annulee")

    choix = input("Choisir un statut : ")

    statuts = {
        "1": "a_faire",
        "2": "en_cours",
        "3": "terminee",
        "4": "annulee"
    }

    statut = statuts.get(choix)

    if statut is None:
        print("Statut invalide")
        return []

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
            AND statut = %s
            """

            valeurs = (
                id_user,
                statut
            )

            cursor.execute(sql, valeurs)

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

def filtrer_taches_priorite(id_user):

    print("\nPriorites disponibles :")
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
        return []

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
            AND priorite = %s
            """

            valeurs = (
                id_user,
                priorite
            )

            cursor.execute(sql, valeurs)

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
def rechercher_taches(id_user):

    mot_cle = input("Mot-cle de recherche : ")

    recherche = f"%{mot_cle}%"

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
            AND (
                titre LIKE %s
                OR description LIKE %s
            )
            """

            valeurs = (
                id_user,
                recherche,
                recherche
            )

            cursor.execute(sql, valeurs)

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
def taches_en_retard(id_user):

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
            AND date_echeance < CURDATE()
            AND statut NOT IN (
                'terminee',
                'annulee'
            )
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