#!/usr/bin/python3
# =====================
# NOM : Allain Lucas
# ====================
from jinja2 import Environment, FileSystemLoader # ne pas modifier

# Ajouter ici les éléments du modèles dont on a besoin
from personnagesStarWars_modele import *

# ne modifiez pas cette fonction !
def creer_html(fichier_template, fichier_sortie,**infos):
    """
    Cette fonction génère automatiquement un fichier à partir d'un
    template et d'informations
    paramètres :
        fichier_template : un fichier template (template HTML par exemple)
        fichier_sortie : le nom du fichier généré
        **infos : un nombre indéfini de paramètres qu'il suffit de nommer
    return : -
    """
    env=Environment(loader=FileSystemLoader('.'),trim_blocks=True)
    template=env.get_template(fichier_template)
    html=template.render(infos)
    f = open(fichier_sortie, 'w')
    f.write(html)
    f.close()

# Ajouter ici les appels à la fonction creer_html

creer_html("personnagesStarWars_template.html", "Pages_generees/personnagesStarWars.html",
            personnages = cree_liste_tout_les_noms(liste_personnages),
            femmes = noms_feminins(liste_personnages),
            grands = persosGrand(liste_personnages),
            hommes = noms_masculins(liste_personnages),
            droides = noms_droides(liste_personnages),
            toutlemonde = liste_tout_le_monde(liste_personnages)
            )
