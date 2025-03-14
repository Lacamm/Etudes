# Source : https://marvel.com/characters/list/986/core_team_members

# Données sous la forme d'un dictionnaire
# cle = organisation
# valeur = (nom, nomdufichierimage)

dico= {'avengers': [('Black Panther', 'Black_Panther.jpg'), ('Black Widow', 'Black_Widow.jpg'), ('Captain America', 'Captain_America.jpg'), ('Captain Marvel', 'Captain_Marvel.jpg'), ('Falcon', 'Falcon.jpg'), ('Hank Pym', 'Hank_Pym.jpg'), ('Hawkeye', 'Hawkeye.jpg'), ('Hulk', 'Hulk.jpg'), ('Iron Man', 'Iron_Man.jpg'), ('Luke Cage', 'Luke_Cage.jpg'), ('Quicksilver', 'Quicksilver.jpg'), ('Scarlet Witch', 'Scarlet_Witch.jpg'), ('Spider-Woman', 'Spider-Woman.jpg'), ('Thor', 'Thor.jpg'), ('Vision', 'Vision.jpg'), ('Wasp', 'Wasp.jpg'), ('Wonder Man', 'Wonder_Man.jpg')], 'gardians': [('Drax', 'Drax.jpg'), ('Gamora', 'Gamora.jpg'), ('Groot', 'Groot.jpg'), ('Rocket Raccoon', 'Rocket_Raccoon.jpg'), ('Star-Lord', 'Star-Lord.jpg')], 'bad_guy': [('Ultron', 'Ultron.jpg'), ('Loki', 'Loki.jpg'), ('Red Skull', 'Red_Skull.jpg'), ('Mystique', 'Mystique.jpg'), ('Thanos', 'Thanos.jpg'), ('Ronan', 'Ronan.jpg'), ('Magneto', 'Magneto.jpg'), ('Dr. Doom', 'Dr._Doom.jpg'), ('Green Goblin', 'Green_Goblin.jpg'), ('Black Cat', 'Black_Cat.jpg')], 'xmens': [('Angel', 'Angel.jpg'), ('Beast', 'Beast.jpg'), ('Colossus', 'Colossus.jpg'), ('Cyclops', 'Cyclops.jpg'), ('Emma Frost', 'Emma_Frost.jpg'), ('Gambit', 'Gambit.jpg'), ('Iceman', 'Iceman.jpg'), ('Jean Grey', 'Jean_Grey.jpg'), ('Jubilee', 'Jubilee.jpg'), ('Kitty Pryde', 'Kitty_Pryde.jpg'), ('Magik', 'Magik.jpg'), ('Nightcrawler', 'Nightcrawler.jpg'), ('Northstar', 'Northstar.jpg'), ('Psylocke', 'Psylocke.jpg'), ('Rogue', 'Rogue.jpg'), ('Storm', 'Storm.jpg'), ('Wolverine', 'Wolverine.jpg'), ('Wolverine X-23', 'Wolverine_X-23.jpg')]}


# Données sous la forme d'une liste de tuples
# (nom, organisation, nomdufichierimage)
liste=[('Black Panther', 'avengers', 'Black_Panther.jpg'), ('Black Widow', 'avengers', 'Black_Widow.jpg'), ('Captain America', 'avengers', 'Captain_America.jpg'), ('Captain Marvel', 'avengers', 'Captain_Marvel.jpg'), ('Falcon', 'avengers', 'Falcon.jpg'), ('Hank Pym', 'avengers', 'Hank_Pym.jpg'), ('Hawkeye', 'avengers', 'Hawkeye.jpg'), ('Hulk', 'avengers', 'Hulk.jpg'), ('Iron Man', 'avengers', 'Iron_Man.jpg'), ('Luke Cage', 'avengers', 'Luke_Cage.jpg'), ('Quicksilver', 'avengers', 'Quicksilver.jpg'), ('Scarlet Witch', 'avengers', 'Scarlet_Witch.jpg'), ('Spider-Woman', 'avengers', 'Spider-Woman.jpg'), ('Thor', 'avengers', 'Thor.jpg'), ('Vision', 'avengers', 'Vision.jpg'), ('Wasp', 'avengers', 'Wasp.jpg'), ('Wonder Man', 'avengers', 'Wonder_Man.jpg'), ('Drax', 'gardians', 'Drax.jpg'), ('Gamora', 'gardians', 'Gamora.jpg'), ('Groot', 'gardians', 'Groot.jpg'), ('Rocket Raccoon', 'gardians', 'Rocket_Raccoon.jpg'), ('Star-Lord', 'gardians', 'Star-Lord.jpg'), ('Ultron', 'bad_guy', 'Ultron.jpg'), ('Loki', 'bad_guy', 'Loki.jpg'), ('Red Skull', 'bad_guy', 'Red_Skull.jpg'), ('Mystique', 'bad_guy', 'Mystique.jpg'), ('Thanos', 'bad_guy', 'Thanos.jpg'), ('Ronan', 'bad_guy', 'Ronan.jpg'), ('Magneto', 'bad_guy', 'Magneto.jpg'), ('Dr. Doom', 'bad_guy', 'Dr._Doom.jpg'), ('Green Goblin', 'bad_guy', 'Green_Goblin.jpg'), ('Black Cat', 'bad_guy', 'Black_Cat.jpg'), ('Angel', 'xmens', 'Angel.jpg'), ('Beast', 'xmens', 'Beast.jpg'), ('Colossus', 'xmens', 'Colossus.jpg'), ('Cyclops', 'xmens', 'Cyclops.jpg'), ('Emma Frost', 'xmens', 'Emma_Frost.jpg'), ('Gambit', 'xmens', 'Gambit.jpg'), ('Iceman', 'xmens', 'Iceman.jpg'), ('Jean Grey', 'xmens', 'Jean_Grey.jpg'), ('Jubilee', 'xmens', 'Jubilee.jpg'), ('Kitty Pryde', 'xmens', 'Kitty_Pryde.jpg'), ('Magik', 'xmens', 'Magik.jpg'), ('Nightcrawler', 'xmens', 'Nightcrawler.jpg'), ('Northstar', 'xmens', 'Northstar.jpg'), ('Psylocke', 'xmens', 'Psylocke.jpg'), ('Rogue', 'xmens', 'Rogue.jpg'), ('Storm', 'xmens', 'Storm.jpg'), ('Wolverine', 'xmens', 'Wolverine.jpg'), ('Wolverine X-23', 'xmens', 'Wolverine_X-23.jpg')]




# Sous la forme de 4 listes (avec les adresses des images sur le site)

avengers=[
("Black Panther", "https://i.annihil.us/u/prod/marvel/i/mg/1/c0/537ba2bfd6bab/standard_xlarge.jpg"),
("Black Widow", "https://i.annihil.us/u/prod/marvel/i/mg/9/10/537ba3f27a6e0/standard_xlarge.jpg"),
("Captain America", "https://i.annihil.us/u/prod/marvel/i/mg/3/50/537ba56d31087/standard_xlarge.jpg"),
("Captain Marvel", "https://i.annihil.us/u/prod/marvel/i/mg/c/10/537ba5ff07aa4/standard_xlarge.jpg"),
("Falcon", "https://i.annihil.us/u/prod/marvel/i/mg/5/b0/537baa6b25323/standard_xlarge.jpg"),
("Hank Pym", "https://i.annihil.us/u/prod/marvel/i/mg/6/50/535ff34c0544d/standard_xlarge.jpg"),
("Hawkeye", "https://i.annihil.us/u/prod/marvel/i/mg/3/60/537bad8219731/standard_xlarge.jpg"),
("Hulk", "https://i.annihil.us/u/prod/marvel/i/mg/5/a0/538615ca33ab0/standard_xlarge.jpg"),
("Iron Man", "https://i.annihil.us/u/prod/marvel/i/mg/6/a0/55b6a25e654e6/standard_xlarge.jpg"),
("Luke Cage", "https://i.annihil.us/u/prod/marvel/i/mg/5/e0/537bb460046bd/standard_xlarge.jpg"),
("Quicksilver", "https://i.annihil.us/u/prod/marvel/i/mg/5/b0/537bc0124d6b3/standard_xlarge.jpg"),
("Scarlet Witch", "https://i.annihil.us/u/prod/marvel/i/mg/8/70/537bc21ab36c0/standard_xlarge.jpg"),
("Spider-Woman", "https://i.annihil.us/u/prod/marvel/i/mg/c/50/537bc4ac6fc72/standard_xlarge.jpg"),
("Thor", "https://i.annihil.us/u/prod/marvel/i/mg/5/a0/537bc7036ab02/standard_xlarge.jpg"),
("Vision", "https://i.annihil.us/u/prod/marvel/i/mg/9/90/537bc9381fd1d/standard_xlarge.jpg"),
("Wasp", "https://i.annihil.us/u/prod/marvel/i/mg/9/c0/5390dfd5ef165/standard_xlarge.jpg"),
("Wonder Man", "https://i.annihil.us/u/prod/marvel/i/mg/5/40/4ce5a205a2322/standard_xlarge.jpg"),
]
gardians=[
("Drax", "https://i.annihil.us/u/prod/marvel/i/mg/e/d0/526032deabbff/standard_xlarge.jpg"),
("Gamora", "https://i.annihil.us/u/prod/marvel/i/mg/9/70/537bab57b84d4/standard_xlarge.jpg"),
("Groot", "https://i.annihil.us/u/prod/marvel/i/mg/7/10/538caf1975d39/standard_xlarge.jpg"),
("Rocket Raccoon", "https://i.annihil.us/u/prod/marvel/i/mg/6/60/537bc14068e5d/standard_xlarge.jpg"),
("Star-Lord", "https://i.annihil.us/u/prod/marvel/i/mg/9/a0/537bc55e8b1f5/standard_xlarge.jpg"),
]
xmens=[
("Angel", "https://i.annihil.us/u/prod/marvel/i/mg/4/c0/537b886f4929f/standard_xlarge.jpg"),
("Beast", "https://i.annihil.us/u/prod/marvel/i/mg/6/40/537ba156b62e6/standard_xlarge.jpg"),
("Colossus", "https://i.annihil.us/u/prod/marvel/i/mg/6/e0/51127cf4b996f/standard_xlarge.jpg"),
("Cyclops", "https://i.annihil.us/u/prod/marvel/i/mg/6/70/526547e2d90ad/standard_xlarge.jpg"),
("Emma Frost", "https://i.annihil.us/u/prod/marvel/i/mg/c/80/537ba9fe1c75a/standard_xlarge.jpg"),
("Gambit", "https://i.annihil.us/u/prod/marvel/i/mg/9/40/537baad144c79/standard_xlarge.jpg"),
("Iceman", "https://i.annihil.us/u/prod/marvel/i/mg/9/60/537bb08ab56d8/standard_xlarge.jpg"),
("Jean Grey", "https://i.annihil.us/u/prod/marvel/i/mg/8/d0/537bb2a5d33f1/standard_xlarge.jpg"),
("Jubilee", "https://i.annihil.us/u/prod/marvel/i/mg/6/c0/4e7a2148b6e59/standard_xlarge.jpg"),
("Kitty Pryde", "https://i.annihil.us/u/prod/marvel/i/mg/1/00/537bb31597487/standard_xlarge.jpg"),
("Magik", "https://i.annihil.us/u/prod/marvel/i/mg/6/b0/52695ca8391cc/standard_xlarge.jpg"),
("Nightcrawler", "http://images6.fanpop.com/image/photos/35800000/Kurt-Wagner-Nightcrawler-nightcrawler-35828345-200-200.jpg"),
("Northstar", "https://i.annihil.us/u/prod/marvel/i/mg/2/c0/4c003d15985a0/standard_xlarge.jpg"),
("Psylocke", "https://i.annihil.us/u/prod/marvel/i/mg/c/00/537bbf150acc9/standard_xlarge.jpg"),
("Rogue", "https://i.annihil.us/u/prod/marvel/i/mg/c/90/537bc196df2fb/standard_xlarge.jpg"),
("Storm", "https://i.annihil.us/u/prod/marvel/i/mg/c/c0/537bc5db7c77d/standard_xlarge.jpg"),
("Wolverine", "https://i.annihil.us/u/prod/marvel/i/mg/2/60/537bcaef0f6cf/standard_xlarge.jpg"),
("Wolverine X-23", "https://i.annihil.us/u/prod/marvel/i/mg/1/d0/537bcb4edd0bc/standard_xlarge.jpg"),
]
bad_guy=[
("Ultron", "https://i.annihil.us/u/prod/marvel/i/mg/2/03/537bc76411307/standard_xlarge.jpg"),
("Loki", "https://i.annihil.us/u/prod/marvel/i/mg/9/50/537bb3780cfd2/standard_xlarge.jpg"),
("Red Skull", "https://i.annihil.us/u/prod/marvel/i/mg/8/c0/59c132da4c1f1/standard_xlarge.jpg"),
("Mystique", "https://i.annihil.us/u/prod/marvel/i/mg/5/03/5390dc2225782/standard_xlarge.jpg"),
("Thanos", "https://i.annihil.us/u/prod/marvel/i/mg/a/10/537bc68747ccf/standard_xlarge.jpg"),
("Ronan", "https://i.annihil.us/u/prod/marvel/i/mg/2/f0/5260363fc40f2/standard_xlarge.jpg"),
("Magneto", "https://i.annihil.us/u/prod/marvel/i/mg/3/b0/5261a7e53f827/standard_xlarge.jpg"),
("Dr. Doom", "https://i.annihil.us/u/prod/marvel/i/mg/3/60/53176bb096d17/standard_xlarge.jpg"),
("Green Goblin", "https://i.annihil.us/u/prod/marvel/i/mg/f/40/538cf0c2acdd9/standard_xlarge.jpg"),
("Black Cat", "https://i.annihil.us/u/prod/marvel/i/mg/e/03/526952357d91c/standard_xlarge.jpg"),
]

def tout_perso(dico1):
    l=[]
    for liste in dico1.values():
        l.extend(liste)
    return l
def avenger(liste1):
    l_aven=[]
    for i in liste1:
        if i[1]=='avengers':
            l_aven.append(i)
    return l_aven
def gardien(liste1):
    l_gard=[]
    for i in liste1:
        if i[1]=='gardians':
            l_gard.append(i)
    return l_gard
def mechant(liste1):
    l_mech=[]
    for i in liste1:
        if i[1]=='bad_guy':
            l_mech.append(i)
    return l_mech
def xmen(liste1):
    l_xme=[]
    for i in liste1:
        if i[1]=='xmens':
            l_xme.append(i)
    return l_xme
def groupe(nom_groupe):
    return nom_groupe
def tt_les_groupes(liste1):
    liste_nom=[]
    for i in liste:
        if i[1] not in liste_nom:
            liste_nom.append(i[1])
    return liste_nom

dico2={'avengers':avengers, 'gardians':gardians, 'xmens':xmens, 'bad_guy':bad_guy }

# dico={}

# for k in dico2:
    # dico[k]=[]
    # for (nom,_) in dico2[k]:
        # image=nom.replace(" ","_")+".jpg"
        # dico[k].append((nom,image))

# liste=[]
# for k in dico:
    # for (nom,image) in dico[k]:
        # liste.append((nom,k,image))
