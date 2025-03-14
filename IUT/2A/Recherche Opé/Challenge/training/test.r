####################### SCRIPT #######################

source("nettoyage.R")
library(tm)


data<-VCorpus(DirSource("./training",recursive=TRUE))
dataN<-nettoyage(data)
mat<-DocumentTermMatrix(dataN)


# mots apparaissant au moins 300 fois dans le corpus
vocab<-findFreqTerms(mat,400)
mat<-DocumentTermMatrix(dataN,list(dictionary=vocab))


#matrice de classification, 7 classes avec 150 docs
Mstr<-cbind(as.matrix(mat),c(rep("accueil",150),rep("blog",150),rep("commerce",150),rep("FAQ",150),rep("home",150),rep("liste",150),rep("recherche",150)))


#sauvegarde des matrices
saveRDS(vocab, "vocab.rds")
saveRDS(Mstr, "Mstr.rds")
