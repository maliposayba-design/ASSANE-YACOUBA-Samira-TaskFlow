from utilisateur import (
    inscrire_utilisateur,
    connecter_utilisateur
)

from affichage import (
    afficher_menu_principal,
    afficher_erreur,
    afficher_info,
    vider_ecran,
    afficher_tache
)

from tache import (
    ajouter_tache,
    modifier_tache,
    changer_statut_tache,
    supprimer_tache,
    rechercher_taches,
    taches_en_retard,
    taches_du_jour,
    lister_taches,
    filtrer_taches_statut,
    filtrer_taches_priorite,
    filtrer_taches_categorie
)

from categorie import (
    creer_categorie,
    supprimer_categorie
)

from etiquette import (
    creer_etiquette,
    ajouter_etiquette_tache,
    retirer_etiquette_tache
)

from historique import (
    consulter_historique,
    statistiques_personnelles
)

utilisateur_connecte = None

while True:

    if not utilisateur_connecte:

        print("\n===== TASKFLOW =====")

        print("1. Inscription")
        print("2. Connexion")
        print("0. Quitter")

        choix = input("Votre choix : ")

        if choix == "1":

            inscrire_utilisateur()

        elif choix == "2":

            utilisateur_connecte = (
                connecter_utilisateur()
            )

        elif choix == "0":

            print("Au revoir")
            break

        else:

            afficher_erreur(
                "Choix invalide"
            )

    else:

        afficher_menu_principal(
            utilisateur_connecte[
                "nom_utilisateur"
            ]
        )

        choix = input(
            "Votre choix : "
        )

        if choix == "1":

            taches = lister_taches(
                utilisateur_connecte[
                    "id_user"
                ]
            )

            if not taches:

                afficher_info(
                    "Aucune tache disponible"
                )

            else:

                for tache in taches:

                    afficher_tache(tache)
            input("\nAppuyez sur Entree pour continuer...")
            vider_ecran()
        elif choix == "2":

            ajouter_tache(
                utilisateur_connecte[
                    "id_user"
                ]
            )
            input("\nAppuyez sur Entree pour continuer...")
            vider_ecran()

        elif choix == "3":

            modifier_tache(
                utilisateur_connecte[
                    "id_user"
                ]
            )
            input("\nAppuyez sur Entree pour continuer...")
            vider_ecran()

        elif choix == "4":

            changer_statut_tache(
                utilisateur_connecte[
                    "id_user"
                ]
            )
            input("\nAppuyez sur Entree pour continuer...")
            vider_ecran()

        elif choix == "5":

            supprimer_tache(
                utilisateur_connecte[
                    "id_user"
                ]
            )
            input("\nAppuyez sur Entree pour continuer...")
            vider_ecran()

        elif choix == "6":

         print("\n=== CATEGORIES ===")
         print("1. Creer une categorie")
         print("2. Supprimer une categorie")

         choix_cat = input("Votre choix : ")

         if choix_cat == "1":

             creer_categorie(
             utilisateur_connecte["id_user"]
             )

         elif choix_cat == "2":

              supprimer_categorie(
              utilisateur_connecte["id_user"]
              )

         else:

              afficher_erreur(
              "Choix invalide"
              ) 

         input("\nAppuyez sur Entree pour continuer...")
         vider_ecran()

        elif choix == "7":

         print("\n=== ETIQUETTES ===")
         print("1. Creer une etiquette")
         print("2. Ajouter une etiquette a une tache")
         print("3. Retirer une etiquette d'une tache")

         choix_etiq = input("Votre choix : ")

         if choix_etiq == "1":

               creer_etiquette(
              utilisateur_connecte[
                "id_user"
               ]
              )

         elif choix_etiq == "2":

               ajouter_etiquette_tache(
              utilisateur_connecte[
                "id_user"
              ]
             )

         elif choix_etiq == "3":

              retirer_etiquette_tache()
 
         else:

             afficher_erreur(
              "Choix invalide"
             )

         input("\nAppuyez sur Entree pour continuer...")
         vider_ecran()

        elif choix == "8":

            historique = (
                consulter_historique(
                    utilisateur_connecte[
                   "id_user"
                 ]
                 )
             )
            
            if not historique:

                 afficher_info(
                    "Aucun historique disponible"
                 )

            else:

                for ligne in historique:

                 print(
                 f"{ligne['date_changement']} : "
                 f"{ligne['ancien_statut']} -> "
                 f"{ligne['nouveau_statut']}"
                  )
            input("\nAppuyez sur Entree pour continuer...")
            vider_ecran()         
        elif choix == "9":

         print("\n=== RECHERCHE ET FILTRES ===")

         print("1. Rechercher par mot-cle")
         print("2. Filtrer par statut")
         print("3. Filtrer par priorite")
         print("4. Filtrer par categorie")
         print("5. Voir les taches en retard")
         print("6. Voir les taches du jour")

         choix_filtre = input(
          "Votre choix : "
          )
      
         if choix_filtre == "1":
             taches = rechercher_taches(
             utilisateur_connecte[
                "id_user"
              ]
             )

         elif choix_filtre == "2":
              taches = filtrer_taches_statut(
             utilisateur_connecte[
                "id_user"
             ]
              )

         elif choix_filtre == "3":

              taches = filtrer_taches_priorite(
             utilisateur_connecte[
                "id_user"
              ]
             )

         elif choix_filtre == "4":

             taches = filtrer_taches_categorie(
              utilisateur_connecte[
                "id_user"
              ]
             )

         elif choix_filtre == "5":

             taches = taches_en_retard(
             utilisateur_connecte[
                "id_user"
             ]
             )

         elif choix_filtre == "6":

              taches = taches_du_jour(
             utilisateur_connecte[
                "id_user"
             ]
             )

         else:

              afficher_erreur(
             "Choix invalide"
             )

              taches = []

         if not taches:

               afficher_info(
             "Aucune tache trouvee"
              )

         else:

             for tache in taches:

              afficher_tache(tache)

         input(
          "\nAppuyez sur Entree pour continuer..."
         )

         vider_ecran()

        elif choix == "10":

            stats = statistiques_personnelles(
             utilisateur_connecte[
             "id_user"
             ]
           )

            if stats is None:

              afficher_erreur(
             "Impossible de recuperer les statistiques"
              )

            else:

             print(
             f"\nNombre total de taches : "
             f"{stats['total']}"
             )

             print(
             f"Taux de completion : "
             f"{stats['taux_completion']:.2f}%"
             )

             print("\nPar statut :")

             for statut in stats["statut"]:

                 print(
                 f"{statut['statut']} : "
                 f"{statut['nombre']}"
                 )

             print("\nPar priorite :")

             for priorite in stats["priorite"]:
   
                 print(
                 f"{priorite['priorite']} : "
                 f"{priorite['nombre']}"
                 )

            input(
           "\nAppuyez sur Entree pour continuer..."
            )

            vider_ecran()

        elif choix == "0":

            utilisateur_connecte = None

            afficher_info(
                "Deconnexion reussie"
            )

        else:

            afficher_erreur(
                "Choix invalide"
            )