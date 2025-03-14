#!/usr/bin/python3
# =====================
# NOM : ALLAIN Lucas
# ====================
# ===========
# Les données
# ===========

"""
liste_des_planetes est une liste de planètes
Chaque planète est modélisé par un tuple (nom, localisation, espèces intelligentes)
  - nom : est le nom de la planète (str)
  - localisation : est un str qui précise la zone galactique dans laquelle est située la planète.
  - espèces intelligentes est un ensemble de str qui précise les espèces intelligentes qui vivent sur la planète
Par exemple le tuple ('Glee Anselm', 'Bordure médiane', {'Nautolans', 'Anselmi'}) modélise la planète nommé 'Glee Anselm'.
Cette planète se situe en 'Bordure médiane'
On peut y trouver deux espèces intelligentes : les `Nautolans` et les `Anselmi`
"""
liste_des_planetes=[
    ('Glee Anselm', 'Bordure médiane', {'Nautolans', 'Anselmi'}), 
    ('Endor', 'Bordure extérieure', {'Yuzzum', 'Duloks', 'Ewoks '}), ('Voss', 'Bordure médiane', {'Voss', 'Gormaks '}), ('Hapes', 'Bordure médiane', {'Humains'}), ('Balmora', 'Colonies', {'Humains'}), ('Vjun', 'Bordure extérieure', set()), ('Sullust', 'Bordure extérieure', {'Sullustens'}),     ('Etti 4', 'Bordure extérieure', set()), ('Géonosis', 'Bordure extérieure', {'Géonosiens'}), ('Kiffu', 'Bordure intérieure', {'Kiffars'}), ('Malastare', 'Bordure médiane', {'Dugs'}), ('Ambria', 'Bordure intérieure', set()), ('Brodo Asogi', 'Localisation inconnue', set()), ('Almania', 'Bordure extérieure', set()), ("D'Qar4,2", 'Bordure extérieure', {'Les membres de la Résistance'}), ('Raxus', 'Bordure extérieure', set()), ('Bothawui', 'Bordure médiane', {'Bothans'}), ('Tython', 'Noyau profond', {'Humains'}), ('Alderaan', 'Mondes du Noyau', {'Humains', 'Killiks'}), ('Muunilist', 'Bordure extérieure', {'Muuns'}), ('Deralia', 'Bordure extérieure', {'Humains'}), ('Ziost', 'Bordure extérieure', set()), ('Myrkr', 'Bordure intérieure', {'Netis'}), ('Korriban', 'Bordure extérieure', {'Sith'}), ('Brodo Asogi', 'Localisation inconnue', set()), ('Bothawui', 'Bordure médiane', {'Bothans'}), ('Zonama Sekot', 'Bordure extérieure', {'Yuuzhan Vong'}), ('Duro', 'Mondes du Noyau', {'Duros'}), ('Base Starkiller3', 'Bordure extérieure', {'Les membres du Premier Ordre'}), ('Onderon', 'Bordure intérieure', {'Humains,'}), ('Lothal', 'Bordure extérieure', {'Humains'}), ('Saleucami', 'Bordure extérieure', set()), ('Yavin 4', 'Bordure extérieure', {'Massassi'}), ('Kalarba', 'Bordure médiane', set()), ('Utapau', 'Bordure extérieure', {"Pau'ens ", 'Utais'}), ('Ryloth', 'Bordure extérieure', {"Twi'leks"}), ('Mygeeto', 'Bordure extérieure', {'Lurmens'}), ('Taris', 'Bordure extérieure', {'Rakgoules ', 'Humains', 'Nekgoules'}), ('Dathomir', 'Bordure extérieure', {'Kwa', 'Zabraks'}), ('Ruusan', 'Bordure médiane', {'faune hostile (déserte)'}), ('Kirrek', 'Bordure intérieure', {'Humains'}), ('Ilum', 'Hors de la galaxie', {'Talz'}), ('Ord Mantell', 'Bordure médiane', {'Humains'}), ('Mustafar', 'Bordure extérieure', {'Mustafariens'}), ('Sebbadon', 'Hors de la galaxie', {"Hex (robots dotés d'une intelligence supérieure à la normale)"}), ('Félucia', 'Bordure extérieure', {'Feluciens'}), ('Wayland', 'Bordure extérieure', {'Myneyrshs ', 'Psadens'}), ('Kubindi', 'Bordure extérieure', {'Kubaz'}), ('Bakura', 'Hors de la galaxie', {'Kurtzens'}), ('Kuat', 'Mondes du Noyau', {'Humain'}), ('Jabiim', 'Bordure extérieure', set()), ('Nar Shaddaa', 'Bordure médiane', {'Humains', 'contrebandiers'}), ('Ylesia', 'Bordure extérieure', set()), ('Falleen', 'Bordure médiane', {'Falleens'}), ('Atzerri', 'Bordure intérieure', set()), ('Borleias', 'Colonies', set()), ('Dorin', "Zone d'expansion", {'Kel Dor'}), ('Sulon', 'Bordure extérieure', set()), ('Obroaskai', 'Bordure intérieure', {'Obraens'}), ('Kashyyyk', 'Bordure médiane', {'Wookiees'}), ('Dantooine', 'Bordure extérieure', {'Humains'}), ('AhchTo1', 'Bordure extérieure', set()), ('Sernpidal', 'Bordure extérieure', set()), ('Balmora', 'Colonies', {'Humains'}), ('Selonia', 'Noyau profond', {'Seloniens'}), ('Vortex', 'Bordure médiane', set()), ('Shili', "Zone d'expansion", {'Togrutas'}), ('Jakku4,5,2', 'Bordure extérieure', set()), ('Dac', 'Bordure extérieure', {'Quarrens', 'Mon Calamari '}), ('Yinchorr', "Zone d'expansion", {'Yinchorris'}), ('Bonadan', 'Bordure extérieure', set()), ('Kamino', 'Hors de la galaxie', {'Kaminoens'}), ('Yaga Minor', 'Bordure extérieure', {'Yagas'}), ('Adumar', 'Hors de la galaxie', set()), ('Bastion', 'Bordure extérieure', set()), ('Honoghr', 'Bordure extérieure', {'Noghri'}), ('Hosnian Prime4', 'Mondes du Noyau', {'Humains'}), ('Bespin', 'Bordure extérieure', set()), ('Kothlis', 'Bordure médiane', set()), ('Rodia', 'Bordure médiane', {'Rodiens'}), ('Tralus', 'Mondes du Noyau', {'Humains'}), ('Takodana4', 'Bordure médiane', set()), ('Lehon/Rakata Prime', 'Régions inconnues', {'Rakatas'}), ('Ralltiir', 'Mondes du Noyau', set()), ('Agamar', 'Bordure extérieure', {'Humains'}), ('Brentaal 4', 'Noyau profond', set()), ('Nal Hutta', 'Bordure médiane', {'Evocii'}), ('Umbara', "Zone d'expansion", {'Umbarens'}), ('Bastion', 'Bordure extérieure', set()), ('Hoth', 'Bordure extérieure', set()), ('Bakura', 'Hors de la galaxie', {'Kurtzens'}), ('Eriadu', 'Bordure extérieure', set()), ('Abregadorae', 'Mondes du Noyau', {'Killiks'}), ('Byss', 'Noyau profond', set()), ('Gyndine', "Zone d'expansion", set()), ('Base Starkiller3', 'Bordure extérieure', {'Les membres du Premier Ordre'}), ('Dagobah', 'Bordure extérieure', set()), ('Borleias', 'Colonies', set()), ('Bespin', 'Bordure extérieure', set()), ('Bandomeer', 'Bordure extérieure', {'Meeriens'}), ('Yavin', 'Bordure extérieure', set()), ('Byss', 'Noyau profond', set()), ('Neimodia', 'Mondes du Noyau', {'Neimodien'}), ('Rishi', 'Bordure extérieure', {'Rishii'}), ('Kiffex', 'Bordure intérieure', set()), ('Ossus', 'Bordure extérieure', {'Humains'}), ('Vanqor', 'Bordure extérieure', set()), ('Ithor', 'Bordure médiane', {'Ithoriens'}), ('Bandomeer', 'Bordure extérieure', {'Meeriens'}), ('Polis Massa', 'Bordure extérieure', set()), ('Tatooine', 'Bordure extérieure', {'Kumumgahs ', 'Tuskens', 'Jawas'}), ('Telos 4', 'Bordure extérieure', set()), ('Trandosha', 'Bordure médiane', {'Trandoshans'}), ('Talus', 'Mondes du Noyau', set()), ('Klatooine', 'Bordure extérieure', {'Klatooiniens'}), ('Stewjon', 'Bordure extérieure', set()), ('Naboo', 'Bordure médiane', {'Humains', 'Gungans '}), ('Zygerria', 'Bordure extérieure', {'Zygerriens'}), ('Mandalore', 'Bordure extérieure', {'Humains'}), ('Bonadan', 'Bordure extérieure', set()), ('Fondor', 'Colonies', {'Humains'}), ('Brentaal 4', 'Noyau profond', set()), ('Devaron', 'Colonies', {'Devaroniens'})]


# liste_des_planetes.append(('Alpha du Centaure', 'Mondes du Noyau', {'Humains', 'Anselmi'}),)

# ================================
# Outils de traitement des données
# ================================

def planetes(liste_des_planetes):
  planetes_A = []
  for planete in liste_des_planetes:
    if planete[0][0] == 'A':
      planete_valide = (planete[0],planete[1])
      planetes_A.append(planete_valide)
  return planetes_A

def Humains(liste_des_planetes):
  humains_present = []
  for especes in liste_des_planetes:
    if 'Humains' in especes[2]:
      humains_present.append(especes[0])
  return humains_present

def Noyau(liste_des_planetes):
  noyau = []
  for lieu in liste_des_planetes:
    if 'Mondes du Noyau' in lieu[1]:
      monde = (lieu[0], lieu[1], lieu[2])
      noyau.append(monde)
  return noyau

def Localisation(liste_des_planetes):
  atlas = []
  for lieux in liste_des_planetes:
    if lieux[1] not in atlas:
      atlas.append(lieux[1])
  return atlas