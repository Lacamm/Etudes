#!/usr/bin/python3

# modele_0_tropfacile.py
# Version 0 du modèle directement exploitable
# dico_infos_pages est un dictionnaire dont :
#   - les clés sont le nom des pages à générer
#   - les valeurs associées sont des tuples contenant :
#      - la liste des images à afficher
#      - le nom de la page suivante (s'il y a lieu)
#      - le nom de la page précédente (s'il y a lieu)

repertoire='/pub/1A/DocNum/PhotosDeMartine/images/'

dico_infos_pages={
  'page-0.html': (
      ['adler-2611528__340.jpg', 'adler-2872995__340.jpg', 'adler-3366239__340.jpg'], 
      'page-1.html',
       None), 
  'page-1.html': (
      ['adler-339128__340.jpg', 'adler-3551609__340.jpg', 'alcedo-atthis-881594__340.jpg'], 
      'page-2.html',
      'page-0.html'),
  'page-2.html': (
      ['animal-1854225__340.jpg', 'bald-eagle-1728739__340.jpg', 'bald-eagle-2715461__340.jpg'], 
      'page-3.html',
      'page-1.html'),
  'page-3.html': (
      ['bald-eagles-341898__340.jpg', 'barn-owl-1107397__340.jpg', 'barn-owl-2550068__340.jpg'], 
      'page-4.html',
      'page-2.html'),
  'page-4.html': (
      ['barn-owl-2988291__340.jpg', 'beautiful-16736__340.jpg', 'bee-eaters-3749679__340.jpg'], 
      None,
      'page-3.html')
}
