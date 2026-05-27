
# couleurs de texte
ROUGE = "\033[91m"
VERT = "\033[92m"
JAUNE = "\033[93m"
BLEU = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
BLANC = "\033[97m"
RESET = "\033[0m"

 #styles
GRAS = "\033[1m"
SOULIGNE = "\033[4m"


def afficher_succes(message):
    print(f"{VERT}{GRAS}[OK]{RESET} {message}")


def afficher_erreur(message):
    print(f"{ROUGE}{GRAS}[ERREUR]{RESET} {message}")


def afficher_info(message):
    print(f"{CYAN}[INFO]{RESET} {message}")


def afficher_alerte(message):
    print(f"{JAUNE}{GRAS}[!]{RESET} {message}")


def afficher_menu_principal(nom_utilisateur):

    print("\n" + "=" * 50)

    print(f"{BLEU}{GRAS} TASKFLOW — Bienvenue, {nom_utilisateur}{RESET}")

    print("=" * 50)

    print(f" {GRAS}1.{RESET} Voir toutes mes taches")
    print(f" {GRAS}2.{RESET} Ajouter une nouvelle tache")
    print(f" {GRAS}3.{RESET} Modifier une tache")
    print(f" {GRAS}4.{RESET} Changer le statut d'une tache")
    print(f" {GRAS}5.{RESET} Supprimer une tache")
    print(f" {GRAS}6.{RESET} Gerer mes categories")
    print(f" {GRAS}7.{RESET} Gerer mes etiquettes")
    print(f" {GRAS}8.{RESET} Voir l'historique d'une tache")
    print(f" {GRAS}9.{RESET} Rechercher des taches")
    print(f" {GRAS}0.{RESET} {ROUGE}Se deconnecter{RESET}")

    print("=" * 50)


def vider_ecran():
    import os
    os.system("cls" if os.name == "nt" else "clear")    