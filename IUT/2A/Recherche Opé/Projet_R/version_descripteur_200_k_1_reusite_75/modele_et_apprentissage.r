#vide l'environnement de travail
remove(list = ls())

#un texte peut parfois etre considere comme un vecteur ou une liste de lignes.
#La fonction suivante concatene toutes les lignes du texte en parametre et retourne
#une unique chaine de caracteres
merge<-function(t){
  PlainTextDocument(paste(t,collapse=""))
}

#Suppression des script s(<script .... </script>)
removeScript<-function(t){
  #découpage de la chaine en utilisant "<split"
  sp<-strsplit(as.character(t), "<script")[[1]]
  #pour chaque partie du split, le début (jusqu'a </script>) est supprimé
  vec<-sapply(1:length(sp),function(i) gsub(sp[i], pattern=".*</script>", replace=" "))
  #les élements du split nettoyés sont concaténés
  PlainTextDocument(paste(vec,collapse=""))
}

#Suppression de toutes les balises
removeBalises<-function(t){
  t1<-gsub("<[^>]*>", " ", t)
  #suppression des occurrences multiples d'espaces (ou de tabulations)
  PlainTextDocument(gsub("[ \t]+"," ",t1))
}

#Fonction de nettoyage permettant de récupérer uniquement le contenu textuel d'une page HTML
nettoyage<-function(corpus){
  corpus<-tm_map(corpus,merge)
  corpus<-tm_map(corpus,content_transformer(tolower))
  #on utilise content_tranformer pour forcer le traitement via tolower à renvoyer un PlainTextDocument
  corpus<-tm_map(corpus,removeScript)
  corpus<-tm_map(corpus,removeBalises)
  corpus<-tm_map(corpus,removeWords,words=stopwords('en'))
  corpus<-tm_map(corpus,stemDocument,language='en')
  corpus<-tm_map(corpus,removePunctuation)
  corpus<-tm_map(corpus,removeNumbers)
}

#on charge la librairie tm
library(tm)
#on recupere les données d'entrainnement
donnees<-VCorpus(DirSource("./training/training",recursive=TRUE))
#on nettoie les donnés d'entrainnement
donneesN<-nettoyage(donnees)
#on transforme les donnees en un document-term matrix
mat<-DocumentTermMatrix(donneesN)
#on cree vocab, qui contient les mots apparaisent plus de 152 fois dans les données nettoyés
vocab<-findFreqTerms(mat,200)
#a partir de vocabe et de mat on crée un matrice, chaque ligne correspondeant à un document, et chaque colone à un mot, les valuers étant le nombre doccurance des mots dans le documents
M<-as.matrix(DocumentTermMatrix(donneesN,list(dictionary=vocab)))
#On crée les 7 classes pour les 1050 documents
classes<-c(rep("accueil",150),rep("blog",150),rep("commerce",150),rep("FAQ",150),rep("home",150),rep("liste",150),rep("recherche",150))
#On ajoute dans la matrice la classe de chaque document
M<-cbind(M,classes)

# retourne la distance euclidienne entre deux vecteurs x et y.
distance<-function(x,y){
  x<-as.integer(x)
  y<-as.integer(y)
  return(sum((x-y)^2))
}

# calcule le vecteur des distances entre *vecteur* et chacun des objets de *data*.
dist.voisins<-function(vecteur,data){
  return(apply(data,1,distance,x=vecteur))
}

# retourne le vecteur des indices des k plus proches voisins de l’objet *vecteur* dans *data* (en cas d’égalité, on retourne arbitrairement l’un des indices des objets équidistants).
kppv<-function(vecteur,k,data){
  v<-dist.voisins(vecteur,data)
  return(order(v)[1:k])
}

# retourne la classe majoritaire parmi les k plus proches voisins de *vecteur* dans *data* (en cas d’égalité, on retourne arbitrairement l’une des classes majoritaires)
classerKPPV<-function(vecteur,k,data){
  x<-kppv(vecteur,k,data[,-ncol(data)])
  c<-table(data[x,ncol(data)])
  ind<-names(c)[which.max(c)]
  return(ind)
}

# calcule l’erreur d'“apprentissage” pour le classifieur des k-PPV sur *data*.
erreurkPPV<-function(k,data){
  res<-sapply(1:nrow(data),function(i) return(classerKPPV(data[i,-ncol(data)],k,data[-i,])))
  sum(res!=data[,ncol(data)])/nrow(data)
}

# affiche un graphique pour mettre en évidence le meilleur k possible pour cet échantillon
testK<-function(data){
  res<-sapply(1:5,erreurkPPV,data=data)
  print(res)
  plot(res,type="l")
}

#Tests du modéle:
  #-recherche de k
  if(FALSE){
    T1<-Sys.time()
    testK(M)
    T2<-Sys.time()
    print(difftime(T2, T1)) 
  }
  #-calcul du pourcentage de réussite avec erreurkPPV
  if(FALSE){
    T1<-Sys.time()
    print(1-erreurkPPV(1,M))
    T2<-Sys.time()
    print(difftime(T2, T1)) 
  }

#sauvegarde le modele
save(M,vocab,classerKPPV,dist.voisins,distance,erreurkPPV,kppv,merge,nettoyage,removeBalises,removeScript,file = "modele.RData")