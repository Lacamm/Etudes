#!/usr/bin/python3

# Source : https://marvel.com/characters/list/986/core_team_members

# Données sous la forme d'un dictionnaire
# cle = organisation
# valeur = (nom, nomdufichierimage)

###############
# Données
###############

rep = "/pub/1A/DocNum/personnagesMarvel/"

titre_page = "Les Personnages de Marvel"

dico = {'avengers': [('Black Panther', 'Black_Panther.jpg'), ('Black Widow', 'Black_Widow.jpg'), ('Captain America', 'Captain_America.jpg'), ('Captain Marvel', 'Captain_Marvel.jpg'), ('Falcon', 'Falcon.jpg'), ('Hank Pym', 'Hank_Pym.jpg'), ('Hawkeye', 'Hawkeye.jpg'), ('Hulk', 'Hulk.jpg'), ('Iron Man', 'Iron_Man.jpg'), ('Luke Cage', 'Luke_Cage.jpg'), ('Quicksilver', 'Quicksilver.jpg'), ('Scarlet Witch', 'Scarlet_Witch.jpg'), ('Spider-Woman', 'Spider-Woman.jpg'), ('Thor', 'Thor.jpg'), ('Vision', 'Vision.jpg'), ('Wasp', 'Wasp.jpg'), ('Wonder Man', 'Wonder_Man.jpg')], 'gardians': [('Drax', 'Drax.jpg'), ('Gamora', 'Gamora.jpg'), ('Groot', 'Groot.jpg'), ('Rocket Raccoon', 'Rocket_Raccoon.jpg'), ('Star-Lord', 'Star-Lord.jpg')], 'bad_guy': [('Ultron', 'Ultron.jpg'), ('Loki', 'Loki.jpg'), ('Red Skull', 'Red_Skull.jpg'), ('Mystique', 'Mystique.jpg'), ('Thanos', 'Thanos.jpg'), ('Ronan', 'Ronan.jpg'), ('Magneto', 'Magneto.jpg'), ('Dr. Doom', 'Dr._Doom.jpg'), ('Green Goblin', 'Green_Goblin.jpg'), ('Black Cat', 'Black_Cat.jpg')], 'xmens': [('Angel', 'Angel.jpg'), ('Beast', 'Beast.jpg'), ('Colossus', 'Colossus.jpg'), ('Cyclops', 'Cyclops.jpg'), ('Emma Frost', 'Emma_Frost.jpg'), ('Gambit', 'Gambit.jpg'), ('Iceman', 'Iceman.jpg'), ('Jean Grey', 'Jean_Grey.jpg'), ('Jubilee', 'Jubilee.jpg'), ('Kitty Pryde', 'Kitty_Pryde.jpg'), ('Magik', 'Magik.jpg'), ('Nightcrawler', 'Nightcrawler.jpg'), ('Northstar', 'Northstar.jpg'), ('Psylocke', 'Psylocke.jpg'), ('Rogue', 'Rogue.jpg'), ('Storm', 'Storm.jpg'), ('Wolverine', 'Wolverine.jpg'), ('Wolverine X-23', 'Wolverine_X-23.jpg')]}


###############
# Fonctions
###############

def les_organisations(dico):
    orga = set()
    for nom in dico.keys():
        orga.add(nom)
    return orga

def les_personnages(dico):
    infos_perso = []
    for _,infos in dico.items():
        for perso in infos:
            infos_perso.append((perso))
    return infos_perso


organisations = les_organisations(dico)

perso = les_personnages(dico)
