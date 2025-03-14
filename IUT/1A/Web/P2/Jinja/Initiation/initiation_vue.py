#!/bin/python

from jinja2 import Environment , FileSystemLoader
from initiation_modele import mes_nombres , proprietaire


def creer_html(fichier_template , fichier_sortie ,**infos):
    env=Environment(loader=FileSystemLoader('.'),trim_blocks=True)
    template=env.get_template(fichier_template)
    html=template.render(infos)
    f = open(fichier_sortie , 'w')
    f.write(html)
    f.close()

creer_html("initiation_template.html", "initiation.html",
            liste=mes_nombres ,
            nom=proprietaire)