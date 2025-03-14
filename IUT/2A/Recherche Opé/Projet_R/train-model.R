library(tm)
library(e1071)
source("nettoyage.R")


data<-VCorpus(DirSource("jeux",recursive=TRUE))

dataN<-nettoyage(data)

mat<-DocumentTermMatrix(dataN)


vocab<-findFreqTerms(mat,300)
mat<-DocumentTermMatrix(dataN,list(dictionary=vocab))

donnees_res <- svm(x=as.matrix(mat), y=c(rep("accueil",150),rep("blog",150),rep("commerce",150),rep("FAQ",150),rep("home",150),rep("liste",150),rep("recherche",150)), type="C", kernel="linear")

#sauvegarde du modèle
saveRDS(vocab, "vocab.rds")
saveRDS(donnees_res, "donnees_res.rds")