#=======================================================================
# Données sur les personnages des films Star Wars
#=======================================================================

"""
'dico_personnages' est un dictionnaire dont les clefs sont le nom de personnages
et les valeur une liste  contenant les titres des épisodes dans les quels le personnage apparaît.
Par exemple :
 - 'Luke Skywalker' est le nom d'un personnage qui apparaît dans 5 films ('The Phantom Menace', 'Attack of the Clones', 'Revenge of the Sith', 'Return of the Jedi' et 'The Force Awakens')
 - 'Lobot' est le nom d'un personnage qui n'apparaît que dans 'Attack of the Clones'
"""
dico_personnages = {
    'Luke Skywalker': ['The Phantom Menace', 'Attack of the Clones', 'Revenge of the Sith', 'Return of the Jedi', 'The Force Awakens'], 
    'C-3PO': ['The Phantom Menace', 'Attack of the Clones', 'Revenge of the Sith', 'A New Hope', 'The Empire Strikes Back', 'Return of the Jedi'],'Anakin Skywalker': ['A New Hope', 'The Empire Strikes Back', 'Return of the Jedi'], 
    'Wilhuff Tarkin': ['The Phantom Menace', 'Return of the Jedi'], 
    'Chewbacca': ['The Phantom Menace', 'Attack of the Clones', 'Revenge of the Sith', 'Return of the Jedi', 'The Force Awakens'], 
    'Han Solo': ['The Phantom Menace', 'Attack of the Clones', 'Revenge of the Sith', 'The Force Awakens'], 
    'Greedo': ['The Phantom Menace'], 
    'Jabba Desilijic Tiure': ['The Phantom Menace', 'Revenge of the Sith', 'A New Hope'], 
    'Wedge Antilles': ['The Phantom Menace', 'Attack of the Clones', 'Revenge of the Sith'], 
    'Jek Tono Porkins': ['The Phantom Menace'], 
    'Yoda': ['Attack of the Clones', 'Revenge of the Sith', 'A New Hope', 'The Empire Strikes Back', 'Return of the Jedi'], 
    'Palpatine': ['Attack of the Clones', 'Revenge of the Sith', 'A New Hope', 'The Empire Strikes Back', 'Return of the Jedi'], 
    'R2-D2': ['The Phantom Menace', 'Attack of the Clones', 'Revenge of the Sith', 'A New Hope', 'The Empire Strikes Back', 'Return of the Jedi', 'The Force Awakens'], 
    'Boba Fett': ['Attack of the Clones', 'Revenge of the Sith', 'The Empire Strikes Back'], 
    'IG-88': ['Attack of the Clones'], 
    'Bossk': ['Attack of the Clones'], 
    'Lando Calrissian': ['Attack of the Clones', 'Revenge of the Sith'], 
    'Lobot': ['Attack of the Clones'], 
    'Ackbar': ['Revenge of the Sith', 'The Force Awakens'], 
    'Mon Mothma': ['Revenge of the Sith'], 
    'Arvel Crynyd': ['Revenge of the Sith'], 
    'Wicket Systri Warrick': ['Revenge of the Sith'], 
    'Nien Nunb': ['Revenge of the Sith'], 
    'Darth Vader': ['The Phantom Menace', 'Attack of the Clones', 'Revenge of the Sith', 'Return of the Jedi'], 
    'Qui-Gon Jinn': ['A New Hope'], 
    'Nute Gunray': ['A New Hope', 'The Empire Strikes Back', 'Return of the Jedi'], 
    'Finis Valorum': ['A New Hope'], 
    'Padmé Amidala': ['A New Hope', 'The Empire Strikes Back', 'Return of the Jedi'], 
    'Jar Jar Binks': ['A New Hope', 'The Empire Strikes Back'], 
    'Roos Tarpals': ['A New Hope'], 
    'Rugor Nass': ['A New Hope'], 
    'Ric Olié': ['A New Hope'], 
    'Watto': ['A New Hope', 'The Empire Strikes Back'], 
    'Sebulba': ['A New Hope'], 
    'Leia Organa': ['The Phantom Menace', 'Attack of the Clones', 'Revenge of the Sith', 'Return of the Jedi', 'The Force Awakens'], 
    'Quarsh Panaka': ['A New Hope'], 
    'Shmi Skywalker': ['A New Hope', 'The Empire Strikes Back'], 
    'Darth Maul': ['A New Hope'], 
    'Bib Fortuna': ['Revenge of the Sith'], 
    'Ayla Secura': ['A New Hope', 'The Empire Strikes Back', 'Return of the Jedi'], 
    'Ratts Tyerell': ['A New Hope'], 
    'Dud Bolt': ['A New Hope'], 
    'Gasgano': ['A New Hope'], 
    'Ben Quadinaros': ['A New Hope'], 
    'Mace Windu': ['A New Hope', 'The Empire Strikes Back', 'Return of the Jedi'], 
    'Owen Lars': ['The Phantom Menace', 'The Empire Strikes Back', 'Return of the Jedi'], 
    'Ki-Adi-Mundi': ['A New Hope', 'The Empire Strikes Back', 'Return of the Jedi'], 
    'Kit Fisto': ['A New Hope', 'The Empire Strikes Back', 'Return of the Jedi'], 
    'Eeth Koth': ['A New Hope', 'Return of the Jedi'], 
    'Adi Gallia': ['A New Hope', 'Return of the Jedi'], 
    'Saesee Tiin': ['A New Hope', 'Return of the Jedi'], 
    'Yarael Poof': ['A New Hope'], 
    'Plo Koon': ['A New Hope', 'The Empire Strikes Back', 'Return of the Jedi'], 
    'Mas Amedda': ['A New Hope', 'The Empire Strikes Back'], 
    'Gregar Typho': ['The Empire Strikes Back'], 
    'Cordé': ['The Empire Strikes Back'], 
    'Beru Whitesun lars': ['The Phantom Menace', 'The Empire Strikes Back', 'Return of the Jedi'], 
    'Cliegg Lars': ['The Empire Strikes Back'], 
    'Poggle the Lesser': ['The Empire Strikes Back', 'Return of the Jedi'], 
    'Luminara Unduli': ['The Empire Strikes Back', 'Return of the Jedi'], 
    'Barriss Offee': ['The Empire Strikes Back'], 
    'Dormé': ['The Empire Strikes Back'], 
    'Dooku': ['The Empire Strikes Back', 'Return of the Jedi'], 
    'Bail Prestor Organa': ['The Empire Strikes Back', 'Return of the Jedi'], 
    'Jango Fett': ['The Empire Strikes Back'], 
    'Zam Wesell': ['The Empire Strikes Back'], 
    'Dexter Jettster': ['The Empire Strikes Back'], 
    'R5-D4': ['The Phantom Menace'], 
    'Lama Su': ['The Empire Strikes Back'], 
    'Taun We': ['The Empire Strikes Back'], 
    'Jocasta Nu': ['The Empire Strikes Back'], 
    'R4-P17': ['The Empire Strikes Back', 'Return of the Jedi'], 
    'Wat Tambor': ['The Empire Strikes Back'], 
    'San Hill': ['The Empire Strikes Back'], 
    'Shaak Ti': ['The Empire Strikes Back', 'Return of the Jedi'], 
    'Grievous': ['Return of the Jedi'], 
    'Tarfful': ['Return of the Jedi'], 
    'Raymus Antilles': ['The Phantom Menace', 'Return of the Jedi'], 
    'Biggs Darklighter': ['The Phantom Menace'], 
    'Sly Moore': ['The Empire Strikes Back', 'Return of the Jedi'], 
    'Tion Medon': ['Return of the Jedi'], 
    'Finn': ['The Force Awakens'], 
    'Rey': ['The Force Awakens'], 
    'Poe Dameron': ['The Force Awakens'], 
    'BB8': ['The Force Awakens'], 
    'Captain Phasma': ['The Force Awakens'], 
    'Obi-Wan Kenobi': ['The Phantom Menace', 'Attack of the Clones', 'Revenge of the Sith', 'A New Hope', 'The Empire Strikes Back', 'Return of the Jedi']}


"""
'logos_des_films' est un dictionnaire dont les clefs sont les titres des épisodes
et les valeur l'image qui correspond au logo de ce film
Par exemple, l'image de l'épisode 'A New Hope' est 'Star_Wars,_épisode_IV_-_Un_nouvel_espoir_logo.jpg'
"""

logos_des_films = {
    'Revenge of the Sith':"Star_Wars,_épisode_III_-_La_Revanche_des_Sith_logo.jpg",
    'The Phantom Menace':"Star_Wars,_épisode_I_-_La_Menace_fantôme_logo.jpg",
    'A New Hope':"Star_Wars,_épisode_IV_-_Un_nouvel_espoir_logo.jpg",
    'Return of the Jedi':"Star_Wars,_épisode_VI_-_Le_Retour_du_Jedi_logo.jpg",
    'The Empire Strikes Back':"Star_Wars,_épisode_V_-_L'Empire_contre-attaque_logo.jpg",
    'Attack of the Clones':"SW_episode_II_L'Attaque_des_clones.jpg",
    'The Force Awakens':"SW_episode_VII.jpg",
    }

    
"""
'repertoire_logos' est le nom du répertoire contenant tous les logos
"""
repertoire_logos = "/pub/1A/DocNum/Eval4_2018/logos/"
