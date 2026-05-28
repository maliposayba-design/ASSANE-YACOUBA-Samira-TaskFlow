from tache import lister_taches
from affichage import afficher_tache

taches = lister_taches(1)

for tache in taches:
    afficher_tache(tache)

from tache import recuperer_tache
from affichage import afficher_tache

tache = recuperer_tache(1, 1)

print(tache)

if tache:
    afficher_tache(tache)

from tache import modifier_tache

modifier_tache(1)

from tache import changer_statut_tache

changer_statut_tache(1)