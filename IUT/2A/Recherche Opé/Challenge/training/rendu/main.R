
#chargement des sources et des fichiers de sauvegarde
vocab <- readRDS("vocab.rds")
mat <- readRDS("Mstr.rds")

source("kppv.R", encoding = "UTF-8")
source("nettoyage.R",encoding = "UTF-8")

library(tm)


####################### FONCTION CLASSER #######################

classer<-function(fic){
    corpus <- VCorpus(URISource(fic))
    corpusNettoye <- nettoyage(corpus)
    ligneCorpus <- DocumentTermMatrix(corpusNettoye,list(dictionary=vocab)) 
    matrice <- rbind(c(as.vector(ligneCorpus),"3"),mat)
    return(classerKPPV(matrice[1,], 1, matrice))
}