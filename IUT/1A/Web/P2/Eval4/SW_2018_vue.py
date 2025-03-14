#!/usr/bin/python3
from jinja2 import Environment, FileSystemLoader
from SW_2018_donnees import dico_personnages, logos_des_films, repertoire_logos

#from SW_2018_modele import *
from SW_2018_modele_de_secours import *


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
    env = Environment(loader=FileSystemLoader('.'),trim_blocks=True)
    template = env.get_template(fichier_template)
    html=template.render(infos)
    f = open(fichier_sortie, 'w')
    f.write(html)
    f.close()


##### TO DO ########
creer_html("SW_2018_template.html","PagesGenerees/Eval4",
    profil = image_profil,
    logo = logoFilm,
    film = nom_film,
    liste = listeFilm,
    liste_perso = listeP,
    dicoPerso = dico_personnages)


