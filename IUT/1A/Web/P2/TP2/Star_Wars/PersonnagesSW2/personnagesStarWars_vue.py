# ==================================================
# == WEB P2 - TD 1 =================================
# ==================================================
#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader
from personnagesStarWars_modele import *

def creer_html(fichier_template, fichier_sortie, **infos):
	env=Environment(loader=FileSystemLoader('.'),trim_blocks=True)
	template=env.get_template(fichier_template)
	html=template.render(infos)
	f=open(fichier_sortie,'w')
	f.write(html)
	f.close()

# ==================================================

creer_html("personnagesStarWars_template.html","personnagesSW.html",
	liste_personnages=liste_personnages,
	liste_f=liste_f,
	
)
