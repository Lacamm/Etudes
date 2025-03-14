#!/usr/bin/python3
# =====================
# NOM : ALLAIN Lucas
# ====================
from jinja2 import Environment, FileSystemLoader

from planetes_modele_2018 import *


# ne modifiez pas cette fonction
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
    env = Environment(loader=FileSystemLoader('.'),trim_blocks=True)
    template = env.get_template(fichier_template)
    html=template.render(infos)
    f = open(fichier_sortie, 'w')
    f.write(html)
    f.close()

# ==================================================


creer_html("planetes_template_2018.html", "planetes.html",
    A = planetes(liste_des_planetes),
    humains = Humains(liste_des_planetes),
    mondes_noyau = Noyau(liste_des_planetes),
    lieux = Localisation(liste_des_planetes))
