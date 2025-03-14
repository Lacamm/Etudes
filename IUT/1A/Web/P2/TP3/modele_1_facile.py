#!/usr/bin/python3

# modele_1_facile.py
# Version 1 du modèle

#################
# Les données
#################

repertoire='/pub/1A/DocNum/PhotosDeMartine/images/'
tableau_infos_pages=[
  (['adler-2611528__340.jpg', 'adler-2872995__340.jpg', 'adler-3366239__340.jpg'], 'page-1.html', None),
  (['adler-339128__340.jpg', 'adler-3551609__340.jpg', 'alcedo-atthis-881594__340.jpg'], 'page-2.html', 'page-0.html'), 
  (['animal-1854225__340.jpg', 'bald-eagle-1728739__340.jpg', 'bald-eagle-2715461__340.jpg'], 'page-3.html', 'page-1.html'),
  (['bald-eagles-341898__340.jpg', 'barn-owl-1107397__340.jpg', 'barn-owl-2550068__340.jpg'], 'page-4.html', 'page-2.html'),
  (['barn-owl-2988291__340.jpg', 'beautiful-16736__340.jpg', 'bee-eaters-3749679__340.jpg'], None, 'page-3.html')]


##################
# Les fonctions
##################

def tableau_to_dico(tableau):
    """
        Transforme la liste de tuple en dictionnaire
    """
    dico = dict()
    for n in range(len(tableau)):
        dico['page-'+str(n)+'.html'] = tableau[n]
    return dico


dico_infos_pages=tableau_to_dico(tableau_infos_pages)
