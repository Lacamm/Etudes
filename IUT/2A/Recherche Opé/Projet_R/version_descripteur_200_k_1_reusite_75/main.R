#on charge la librairie tm
library(tm)
#on verifie si le workspace contenant le modéle existe, si il existe on le charge, si il n'existe pas, on affiche un message d'erreur
ifelse(file.exists("./modele.RData"), load("./modele.RData"),print("Modéle non trouvé"))

classer<-function(fic) {
  # charher le fichier
  corpus<-VCorpus(URISource(fic))
  # nettoyage
  corpusN<-nettoyage(corpus)
  # DocumentTermMatrix
  mat_corp<-as.matrix(DocumentTermMatrix(corpusN,list(dictionary=vocab)))
  # Classification par kppv
  return(classerKPPV(mat_corp,1,M))
}

#test de la fonction classer
#on utilise if(FALSE) pour "commenter" plusieurs lignes
if(FALSE){
  #On enregistre le moment avant l'execution
  T1<-Sys.time()
  classe <- classer("./training/training/accueil/front_page01_02_02_iht.htm")
  #On enregistre le moment aprés l'execution
  T2<-Sys.time()
  #On fait la différence entre T2 et T1 pour avoir la durée d'execution
  Tdiff<-difftime(T2, T1)
  #affichage
  print(classe)
  print(Tdiff)
}
