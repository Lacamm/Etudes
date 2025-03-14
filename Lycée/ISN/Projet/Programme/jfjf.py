inventaire_bot = ['BOM','REE','DRL','ADC','DRL']
numero_objet_bot = 0

objet_gene = input('objet_gene = ') # On vérifie de quel objet il s'agit
    # !!! Taper le nom de l'objet SANS PARANTHESES, sinon le programe ne trouvera jamais   #*#

while objet_gene != 'BOM' and objet_gene != 'REE' and objet_gene != 'DRL' and objet_gene != 'ADC' and objet_gene != 'CAS':
  print("Le nom saisit est invalide")
  objet_gene = input('objet_gene = ')



while objet_gene != inventaire_bot[numero_objet_bot]:
    if objet_gene != inventaire_bot[numero_objet_bot]:
        numero_objet_bot += 1
    else: 
      numero_objet_bot =+ 1
      break
    if numero_objet_bot > 4:
      print("Vous ne possédez pas cet objet")
      objet_gene = input('objet_gene = ')
      while objet_gene != 'BOM' and objet_gene != 'REE' and objet_gene != 'DRL' and objet_gene != 'ADC' and objet_gene != 'CAS':
        print("Le nom saisit est invalide")
        objet_gene = input('objet_gene = ')
      numero_objet_bot = 0
        
print(numero_objet_bot)
