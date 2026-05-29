from historique import consulter_historique

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