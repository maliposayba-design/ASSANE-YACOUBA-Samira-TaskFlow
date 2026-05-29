from categorie import creer_categorie

creer_categorie(1)

from categorie import lister_categories

categories = lister_categories(1)

for categorie in categories:

    print("\n----------------")

    print(
        f"ID : {categorie['id_categorie']}"
    )

    print(
        f"Nom : {categorie['nom_categorie']}"
    )

    print(
        f"Couleur : {categorie['couleur']}"
    )

    print(
        f"Nombre de taches : "
        f"{categorie['nombre_taches']}"
    )
    from categorie import supprimer_categorie

supprimer_categorie(1)

from tache import ajouter_tache
tache = ajouter_tache(1)

from tache import lister_taches
from affichage import afficher_tache

taches = lister_taches(1)

for tache in taches:
    afficher_tache(tache)
from tache import modifier_tache
modifier_tache(1)

from tache import filtrer_taches_categorie
from affichage import afficher_tache

taches = filtrer_taches_categorie(1)

for tache in taches:

    afficher_tache(tache)

from etiquette import creer_etiquette

creer_etiquette(1)

from etiquette import ajouter_etiquette_tache

ajouter_etiquette_tache(1)

from etiquette import retirer_etiquette_tache

retirer_etiquette_tache()