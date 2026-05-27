from utilisateur import recuperer_utilisateur

print(recuperer_utilisateur("sam"))

from utilisateur import connecter_utilisateur

utilisateur = connecter_utilisateur()

print(utilisateur)

from utilisateur import connecter_utilisateur, deconnecter_utilisateur

utilisateur = connecter_utilisateur()

print(utilisateur)

utilisateur = deconnecter_utilisateur()

print(utilisateur)