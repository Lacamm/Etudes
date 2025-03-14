#!/usr/bin/python3

# modele_2_avance.py
# Version 2 du modèle

repertoire='/pub/1A/DocNum/PhotosDeMartine/images/'

tableau_liste_images=[
  ['adler-2611528__340.jpg', 'adler-2872995__340.jpg', 'adler-3366239__340.jpg'],
  ['adler-339128__340.jpg', 'adler-3551609__340.jpg', 'alcedo-atthis-881594__340.jpg'],
  ['animal-1854225__340.jpg', 'bald-eagle-1728739__340.jpg', 'bald-eagle-2715461__340.jpg'],
  ['bald-eagles-341898__340.jpg', 'barn-owl-1107397__340.jpg', 'barn-owl-2550068__340.jpg'],
  ['barn-owl-2988291__340.jpg', 'beautiful-16736__340.jpg', 'bee-eaters-3749679__340.jpg']]

def tableau_to_dico(tableau):
    """
        Transforme la liste de tuple en dictionnaire
    """
    dico = dict()
    for n in range(len(tableau)):
        dico['page-'+str(n)+'.html'] = tableau[n]
    return dico


def tableau_liste_to_tableau_infos(tableau):
    """
        Rajoute les liens des pages
    """
    tableau_infos_pages = []
    tableau_infos=()

    for n in range(len(tableau)):
        if n == 0:
            tableau_infos=(tableau[n],'page-'+str(n+1)+'.html',None)
        elif n == len(tableau)-1:
            tableau_infos=(tableau[n],None,'page-'+str(n-1)+'.html')
        else:
            tableau_infos=(tableau[n],'page-'+str(n+1)+'.html','page-'+str(n-1)+'.html')
        tableau_infos_pages.append(tableau_infos)

    return tableau_infos_pages


tableau_infos_pages=tableau_liste_to_tableau_infos(tableau_liste_images)

dico_infos_pages=tableau_to_dico(tableau_infos_pages)




