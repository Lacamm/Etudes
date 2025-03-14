#!/usr/bin/env python3
# -*- coding: utf-8 -
# Auteur : VACHER Antoine , ALLAIN Lucas

import asyncio
import random
from datetime import datetime
import os.path




users = [] # liste des utilisateurs
table_without_name = {} # dictionnaire qui stocke les joueurs en attente, le dictionnaire est de la forme (writer,reader,addr) : NBCOUNT
table_with_name = {} # dictionnaire qui stocke les tables en attente, le dictionnaire est de la forme (writer,reader,nameTable,addr) : NBCOUNT


async def envoi(writer,reader,msg,addr): # message qui permet d'envoyer un message au client
    if msg is not None:
        print(msg)
        writer.write(msg.encode() + b"\r\n")

        fichier = open("/shared/shifumi.log","a")
        fichier.write("\n" + ">>> IP DEST : " + str(addr) + " DATE AND TIME : " + str(datetime.now()) + " MESSAGE : " + str(msg))
        fichier.close()

        await writer.drain()


async def recv(reader,addr) : # fonction qui permet de lire un message envoyé par le client
    data = await reader.readline()

    fichier = open("/shared/shifumi.log","a")
    fichier.write("\n" + "<<< IP SOURCE : " + str(addr) + " DATE AND TIME : " + str(datetime.now()) + " MESSAGE : " + str(data))
    fichier.close()

    return data.decode()

async def waitingRoom(writer,reader,k,addr) : # cette fonction va faire attendre un utilisateur le temps qu'un adversaire soit trouve
    nb_joueurs = 0
    dico = {} # on recréer le dico afin de ne pas perdre la connexion avec la personne dans la waiting room
    if len(table_without_name) != 0 : 
        for user,nb_coups in table_without_name.items():
            dico[(user[0],user[1],user[2])] = nb_coups
    while True : 
        await asyncio.sleep(1)
        for user,nb_coups in dico.items() :
            if user[0] != writer and user[1] != reader and nb_coups == k :
                nb_joueurs += 1
        if nb_joueurs >= 2 :
            nb_joueurs = 1
            await envoi(writer,reader,"201: Debut de la partie",addr)
            for user,nb_coups in table_without_name: # on supprime le dictionnaire temporaire
                del dico[(user[0],user[1],user[2])]
            

async def waitingRoom2(writer,reader,name,addr) : # cette fonction va faire attendre un utilisateur le temps qu'un adversaire rejoingne la table
    nb_joueurs = 0
    dico = {} # on recréer le dico afin de ne pas perdre la connexion avec la personne dans la waiting room
    if len(table_without_name) != 0 : 
        for user,nb_coups in table_without_name.items():
            dico[(user[0],user[1],user[2])] = nb_coups
    while True : 
        await asyncio.sleep(1)
        for user_name,nb_coups in dico.items() : 
            if user_name[0] != writer and user_name[1] != reader and user_name[2] == name : # changer la waiting room, boucle pas bonne
                nb_joueurs += 1
        if nb_joueurs >= 2 :
            await envoi(writer,reader,"201: Debut de la partie",addr)
            for user,nb_coups in table_without_name: # on supprime le dictionnaire temporaire
                del dico[(user[0],user[1],user[2])]

        

def find_key(dico,v): # fonction qui retourne la cle d'un dictionnaire
    for k, val in dico.items(): 
        if v == val: 
            return k 

async def lancement_mode(writer,reader,mode,addr) : # cette fonction va verifier si le nombre de coups est réglementaire et va ensuite lancer le mode passé en paramètre
    k = ""
    while type(k) != int or k == 0: # on verifie que k soit bien un entier  et qu'il soit différent de 0
        data = await recv(reader,addr) 
        try:
            k = int(data[10:])
        except ValueError:
            await envoi(writer,reader,"400: Le nombre de coups n'est pas un int",addr)
        if k == 0 : 
            await envoi(writer,reader,"400: Le nombre de coups est égal à 0",addr)

    # On regarde le mode qui a ete passé en paramètre et on fait les opérations nécessaires
    if(mode == 0) :
        await envoi(writer,reader,f"200: La partie contre un ordinateur en {k} coups va commencer",addr)
        await gamemode_0(writer,reader,k,addr) # lancement de la partie contre l'IA

    if(mode == 1) :
        await envoi(writer,reader,f"200: Recherche d'une table sans nom avec {k} coups",addr)
        table_without_name[(writer,reader,addr)] = k
        for name,aa in table_without_name.items() :
            print(name[2] + " " + str(aa))
        cpt = 0
        for user,nb_coups in table_without_name.items() :
            if nb_coups == k :
                cpt += 1
        if cpt >= 2 :
            await envoi(writer,reader,"201: Debut de la partie",addr) 


        else :
            await envoi(writer,reader,"202: En attente d'un joueur",addr)
            wait = asyncio.create_task(waitingRoom(writer,reader,k,addr)) # on met le joueur en attente
            await wait

        writer1 = find_key(table_without_name,k)[0] 
        reader1 = find_key(table_without_name,k)[1]
        addr1 = find_key(table_without_name,k)[2]
        del table_without_name[(writer1,reader1,addr1)] # on les supprime ensuite du dictionnaire d'attente
        writer2 = find_key(table_without_name,k)[0]
        reader2 = find_key(table_without_name,k)[1]
        addr2 = find_key(table_without_name,k)[2]
        del table_without_name[(writer2,reader2,addr2)] # on les supprime ensuite du dictionnaire d'attente
        
        await gamemode_1(writer1,reader1,writer2,reader2,k,addr1,addr2) # on lance la partie entre les deux joueurs

        # on recupere le writer et le reader des deux premiers joueurs enregistre dans le dico (celui qui attend et celui qui demande à jouer)
        
        
        

async def lancement_mode2(writer,reader,name,addr) : # cette fonction va verifier si le nombre de coups est reglementaire et gerer le cas d'une partie MODE: 2
    data = await recv(reader,addr) 
    k = int(data[10:])
    if k == 0 :
        data = 0
        while data == 0  :
            await envoi(writer,reader,"400: Le nombre de coup n'est pas un int",addr)
            rcv = await recv(reader)
            data = int(rcv[10:])
        k = data

    table_with_name[(writer,reader,name,addr)] = k
    await envoi(writer,reader,f"202: Table {name} crée, en attente d'un joueur",addr)
    await waitingRoom2(writer,reader,name,addr)

async def check_name_table(writer,reader,addr) : #cette fonction verifie si le nom de la table donne par l'utilisateur est valide
    data = await recv(reader,addr)  # Verification pour savoir le nom de la table
    name = data[7:]
    if name.isspace() : #True si le str est vide ou s'il n'est compose que d'espaces, false sinon
        data = " "
        while data.isspace() : 
            await envoi(writer,reader,"400: Nom de table invalide, réessayez",addr)
            rcv = await recv(reader,addr)
            data = rcv[7:]
        name = data
    await envoi(writer,reader,"200: Combien de coups souhaitez-vous jouer ?",addr)
    await lancement_mode2(writer,reader,name,addr)

async def join_table(writer,reader,addr) : #cette fonction verifie si le nom de la table donne par l'utilisateur est valide
    data = await recv(reader,addr)  # Verification pour récupérer le nom de la table
    name = data[7:]
    find_table = False
    for user_name,nb_coups in table_with_name.items() : 
        if user_name[2] == name : 
            find_table = True # la table a ete trouvée 
            
    
    if find_table : # si une table est trouvée
        await envoi(writer,reader,"201: Table trouvée, la partie va démarrer",addr)
        writer1 = user_name[0]
        reader1 = user_name[1]
        addr1 = user_name[3]
        # on supprime la table et les deux joueurs du dictionnaires
        del table_with_name[(writer1,reader1,name,addr1)]
        # on lance la partie
        await gamemode_1(writer1,reader1,writer,reader,nb_coups,addr1,addr)

    if not find_table : #si une table n'est pas trouvé
        if name.isspace()  : #True si le str est vide ou s'il n'est compose que d'espaces, false sinon
            await envoi(writer,reader,"500: Erreur : le nom que vous avez renseigné n'est pas valide",addr)
        else : 
            await envoi(writer,reader,"500: Erreur : cette table n'existe pas",addr)

        # on ferme la connexion, même si ici, le clientshifumi fourni le fait pour nous
        writer.close()
        
    
    



async def gamemode_1(writer1,reader1,writer2,reader2,k,addr1,addr2) : # cette fonction gere une partie de shifumi entre deux joueurs
    score_joueur1 = 0
    score_joueur2 = 0
    while k != 0 :
        await envoi(writer1,reader1,str(300 + k) + f": Votre score : {score_joueur1} - Score adversaire : {score_joueur2}",addr1)
        await envoi(writer2,reader2,str(300 + k) + f": Votre score : {score_joueur2} - Score adversaire : {score_joueur1}",addr2)
        data_j1 = await recv(reader1,addr1) # on reçoit les coups envoyés par les deux joueurs
        data_j2 = await recv(reader2,addr2)
        coup_joueur1 = int(data_j1[6]) # on les cast en int
        coup_joueur2 = int(data_j2[6])
        # on regarde si un des deux joueurs gagne le round, dans ce cas on ajoute 1 au score du joueur qui gagne et on décrémente le nombre de tours, on ne fait rien sinon
        if(coup_joueur1 == 0 and coup_joueur2 == 2 or coup_joueur1 == 1 and coup_joueur2 == 0 or coup_joueur1 == 2 and coup_joueur2 == 1) :
            score_joueur1 += 1
            k -= 1
        if(coup_joueur2 == 0 and coup_joueur1 == 2 or coup_joueur2 == 1 and coup_joueur1 == 0 or coup_joueur2 == 2 and coup_joueur1 == 1) :
            score_joueur2 += 1
            k -= 1

    
     # on regarde lequel des joueurs à gagner et on envoi les messages au deux joueurs
    if(score_joueur1 > score_joueur2) :
        await envoi(writer1,reader1,f"300: Bien joué, vous avez gagné ! Votre score : {score_joueur1} - Score adversaire : {score_joueur2}",addr1)
        await envoi(writer2,reader2,f"300: Dommage, vous avez perdu ... Votre score : {score_joueur2} - Score adversaire : {score_joueur1}",addr2)
    if(score_joueur1 < score_joueur2) :
        await envoi(writer1,reader1,f"300: Dommage, vous avez perdu ... Votre score : {score_joueur1} - Score adversaire : {score_joueur2}",addr1)
        await envoi(writer2,reader2,f"300: Bien joué, vous avez gagné ! Votre score : {score_joueur2} - Score adversaire : {score_joueur1}",addr2)
    if(score_joueur1 == score_joueur2) :
        await envoi(writer1,reader1,f"300: C'est un match nul ! Votre score : {score_joueur1} - Score adversaire : {score_joueur2}",addr1)
        await envoi(writer2,reader2,f"300: C'est un match nul ! Votre score : {score_joueur2} - Score adversaire : {score_joueur1}",addr2)
    
    # on ferme la connexion, même si ici, le clientshifumi fourni le fait pour nous
    writer1.close()
    writer2.close()



async def gamemode_0(writer,reader,k,addr) : # cette fonction gere une partie de shifumi entre un joueur et une IA
    score_IA = 0
    score_joueur = 0
    while k != 0 :
        await envoi(writer,reader,str(300 + k) + f": Votre score : {score_joueur} - Score IA : {score_IA}",addr)
        data = await recv(reader,addr) # on reçoit le coup du joueur
        coup_joueur = int(data[6]) # on le cast en int
        coup_IA = random.randint(0,3) # on joue le coup de l'ordinateur (avec la module random)

        # on regarde si le joueur ou l'IA gagne le round, dans ce cas on ajoute 1 au score du joueur ou de l'IA en fonction de qui gagne et on décrémente le nombre de tours, on ne fait rien sinon
        if(coup_joueur == 0 and coup_IA == 2 or coup_joueur == 1 and coup_IA == 0 or coup_joueur == 2 and coup_IA == 1) :
            score_joueur += 1
            k -= 1
        if(coup_IA == 0 and coup_joueur == 2 or coup_IA == 1 and coup_joueur == 0 or coup_IA == 2 and coup_joueur == 1) :
            score_IA += 1
            k -= 1

    # on regarde qui de l'IA ou du joueur a gagné et on envoie le message du résultat au joueur
    if(score_joueur > score_IA) :
        await envoi(writer,reader,f"300: Bien joué, vous avez gagné ! Votre score : {score_joueur} - Score IA : {score_IA}",addr)
    if(score_joueur < score_IA) :
        await envoi(writer,reader,f"300: Dommage, vous avez perdu ... Votre score : {score_joueur} - Score IA : {score_IA}",addr)
    if(score_joueur == score_IA) :
        await envoi(writer,reader,f"300: C'est un match nul ! Votre score : {score_joueur} - Score IA : {score_IA}",addr)

    # on ferme la connexion, même si ici, le clientshifumi fourni le fait pour nous
    writer.close()



async def handle_request(reader, writer): # on gere les requetes clients
    addr = writer.get_extra_info('peername')[0] #on recupere les clients
    users.append(writer)


    await envoi(writer,reader,f"200: Le joueur {addr} est connecté",addr) # message à la connexion d'un utilisateur


    ask_mod = await recv(reader,addr) # on recupere la commande MODE envoye par le client
    # on verifie ensuite quel mode le client a choisi
    if(ask_mod == "MODE: 0\r\n") :
        await envoi(writer,reader,"200: Combien de coups souhaitez-vous jouer ?",addr)
        await lancement_mode(writer,reader,0,addr)

    if(ask_mod == "MODE: 1\r\n") :
        await envoi(writer,reader,"200: Combien de coups souhaitez-vous jouer ?",addr)
        await lancement_mode(writer,reader,1,addr)

    if(ask_mod == "MODE: 2\r\n") :
        await envoi(writer,reader,"200: Quel est le nom de la table que vous souhaitez créer ?",addr)
        await check_name_table(writer,reader,addr)

    if(ask_mod == "MODE: 3\r\n") :
        await envoi(writer,reader,"200: Quel est le nom de la table que vous souhaitez rejoindre ?",addr)
        await join_table(writer,reader,addr)
    
    
            



async def server_shifumi(): #lance le server
    server = await asyncio.start_server(handle_request, '0.0.0.0', 999) #gere les requetes
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')
    async with server:
        await server.serve_forever() # handle requests for ever


if __name__ == '__main__':
    asyncio.run(server_shifumi())
