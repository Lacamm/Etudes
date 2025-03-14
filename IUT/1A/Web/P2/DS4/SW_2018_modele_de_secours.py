from SW_2018_donnees import dico_personnages, logos_des_films, repertoire_logos

########################################################################
# MODELE DE SECOURS
########################################################################


personnages_par_episode = {
    'The Phantom Menace': {'R2-D2', 'Leia Organa', 'Luke Skywalker', 'Biggs Darklighter', 'Raymus Antilles', 'Obi-Wan Kenobi', 'R5-D4', 'Wedge Antilles', 'Jabba Desilijic Tiure', 'Greedo', 'Beru Whitesun lars', 'Owen Lars', 'Jek Tono Porkins', 'Darth Vader', 'Wilhuff Tarkin', 'Han Solo', 'C-3PO', 'Chewbacca'}, 
    
    'Attack of the Clones': {'Lobot', 'R2-D2', 'Leia Organa', 'Luke Skywalker', 'IG-88', 'Wedge Antilles', 'Lando Calrissian', 'Palpatine', 'Bossk', 'Darth Vader', 'Obi-Wan Kenobi', 'Yoda', 'Boba Fett', 'Han Solo', 'C-3PO', 'Chewbacca'}, 
    
    'Revenge of the Sith': {'R2-D2', 'Leia Organa', 'Luke Skywalker', 'Bib Fortuna', 'Wicket Systri Warrick', 'Wedge Antilles', 'Lando Calrissian', 'Palpatine', 'Ackbar', 'Jabba Desilijic Tiure', 'Arvel Crynyd', 'Nien Nunb', 'Darth Vader', 'Obi-Wan Kenobi', 'Yoda', 'Mon Mothma', 'Boba Fett', 'Han Solo', 'C-3PO', 'Chewbacca'}, 
    
    'Return of the Jedi': {'Leia Organa', 'Luke Skywalker', 'Tarfful', 'Grievous', 'Palpatine', 'Padmé Amidala', 'Adi Gallia', 'Darth Vader', 'Yoda', 'Wilhuff Tarkin', 'Plo Koon', 'Luminara Unduli', 'Chewbacca', 'R4-P17', 'Mace Windu', 'Eeth Koth', 'Shaak Ti', 'Sly Moore', 'Bail Prestor Organa', 'Dooku', 'Poggle the Lesser', 'Ayla Secura', 'Raymus Antilles', 'Ki-Adi-Mundi', 'Obi-Wan Kenobi', 'Saesee Tiin', 'Anakin Skywalker', 'Tion Medon', 'Nute Gunray', 'Beru Whitesun lars', 'Owen Lars', 'R2-D2', 'C-3PO', 'Kit Fisto'}, 
    
    'The Force Awakens': {'Leia Organa', 'Luke Skywalker', 'BB8', 'Captain Phasma', 'Ackbar', 'Finn', 'Han Solo', 'Rey', 'Poe Dameron', 'R2-D2', 'Chewbacca'}, 
    
    'A New Hope': {'Jar Jar Binks', 'Gasgano', 'Finis Valorum', 'Rugor Nass', 'Ratts Tyerell', 'Palpatine', 'Padmé Amidala', 'Adi Gallia', 'Quarsh Panaka', 'Yoda', 'Plo Koon', 'Mace Windu', 'Eeth Koth', 'Yarael Poof', 'Watto', 'Ayla Secura', 'Ben Quadinaros', 'Ki-Adi-Mundi', 'Obi-Wan Kenobi', 'Saesee Tiin', 'Anakin Skywalker', 'Dud Bolt', 'Ric Olié', 'Nute Gunray', 'Shmi Skywalker', 'Darth Maul', 'Mas Amedda', 'Qui-Gon Jinn', 'Jabba Desilijic Tiure', 'Roos Tarpals', 'Sebulba', 'R2-D2', 'C-3PO', 'Kit Fisto'}, 
    
    'The Empire Strikes Back': {'Jar Jar Binks', 'Wat Tambor', 'Palpatine', 'Gregar Typho', 'Padmé Amidala', 'Yoda', 'Boba Fett', 'Plo Koon', 'Barriss Offee', 'Luminara Unduli', 'Cliegg Lars', 'Lama Su', 'R4-P17', 'Taun We', 'Cordé', 'Mace Windu', 'Shaak Ti', 'Jango Fett', 'Sly Moore', 'Bail Prestor Organa', 'Dooku', 'Watto', 'Poggle the Lesser', 'Ayla Secura', 'Ki-Adi-Mundi', 'Obi-Wan Kenobi', 'Zam Wesell', 'Anakin Skywalker', 'San Hill', 'Shmi Skywalker', 'Nute Gunray', 'Mas Amedda', 'Jocasta Nu', 'Beru Whitesun lars', 'Owen Lars', 'Dexter Jettster', 'Dormé', 'R2-D2', 'C-3PO', 'Kit Fisto'}
}
def liste_films(dico):
    liste = []
    for film in dico.keys():
        liste.append(film)
    return liste

def listeDesPersonnages(dico):
    newDico = dict()
    listePerso = []
    newDico['The Force Awakens']=dico['The Force Awakens']
    for cle,(perso) in newDico.items():
        listePerso.append(perso)
    return listePerso

listeP = ['Leia Organa', 'Luke Skywalker', 'BB8', 'Captain Phasma', 'Ackbar', 'Finn', 'Han Solo', 'Rey', 'Poe Dameron', 'R2-D2', 'Chewbacca']

#listeDesPersonnages(personnages_par_episode)


listeFilm = liste_films(personnages_par_episode)

image_profil = repertoire_logos+"personnage_important.png"
logoFilm = repertoire_logos+logos_des_films['The Force Awakens']
nom_film = 'The Force Awakens'
