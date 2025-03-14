#!/usr/bin/python3
# =====================
# NOM : Allain Lucas
# ====================
from jinja2 import Environment, FileSystemLoader # ne pas modifier

# Ajouter ici les éléments du modèles dont on a besoin
from modele_4_final import *

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

for (NomPages,(lienImages, Pagesuivante, Pageprecedente)) in dico_infos_pages.items():
    if Pagesuivante == None:
        Pagesuivante = NomPages
    elif Pageprecedente == None:
        Pageprecedente = NomPages

    creer_html("template_oiseaux.html","Pages_generees/"+NomPages,
                galerie = lienImages,
                lien_prec = Pageprecedente,
                lien_suiv = Pagesuivante,
                nom_page = NomPages,
                rep = repertoire,
                )
