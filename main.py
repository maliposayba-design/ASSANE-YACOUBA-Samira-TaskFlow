from historique import (
    consulter_historique,
    statistiques_personnelles
)

historique = consulter_historique(1)

for ligne in historique:

    print("\n----------------")

    print(
        f"Ancien statut : "
        f"{ligne['ancien_statut']}"
    )

    print(
        f"Nouveau statut : "
        f"{ligne['nouveau_statut']}"
    )

    print(
        f"Date du changement : "
        f"{ligne['date_changement']}"
    )

stats = statistiques_personnelles(1)

print("\nTotal taches :")
print(stats["total"])

print("\nPar statut :")

for statut in stats["statut"]:

    print(
        statut["statut"],
        ":",
        statut["nombre"]
    )

print("\nPar priorite :")

for priorite in stats["priorite"]:

    print(
        priorite["priorite"],
        ":",
        priorite["nombre"]
    )

print(
    f"\nTaux completion : "
    f"{stats['taux_completion']:.2f}%"
)
from tache import taches_du_jour
from affichage import afficher_tache

taches = taches_du_jour(1)

for tache in taches:

    afficher_tache(tache)