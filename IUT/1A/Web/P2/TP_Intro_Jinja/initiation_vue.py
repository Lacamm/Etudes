#!/usr/bin/python3
# =====================
# NOM : Allain Lucas
# ====================
from jinja2 import Environment, FileSystemLoader # ne pas modifier

# Ajouter ici les éléments du modèles dont on a besoin
from initiation_modele import *

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

creer_html("initiation_template.html", "pages_generees/initiation_morticia.html",
            nom=morticia,
            courses=courses_morticia,
            prix=facture_morticia,
            total=somme(facture_morticia),
            )

creer_html("initiation_template.html", "pages_generees/initiation2_Gomez.html",
            nom=gomez,
            courses=courses_gomez,
            prix=facture_gomez,
            total=somme(facture_gomez),
            )