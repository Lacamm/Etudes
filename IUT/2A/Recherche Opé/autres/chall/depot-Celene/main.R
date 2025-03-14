# Chargement du modèle et des sources
vocab <- readRDS("vocab.rds")
mat <- readRDS("Mstr.rds")
source("fonctions-kppv.R", encoding = "UTF-8")
source("nettoyage.R",encoding = "UTF-8")

#install.packages("NLP_0.2-1.tar.gz")
#install.packages("tm_0.7-8.tar.gz")

library(tm)

######### Classification

classer <- function(fic) {
  #prepare fic for classification
  newText <- VCorpus(URISource(fic))
  newTextN <- nettoyage(newText)
  newLineForTextN <- DocumentTermMatrix(newTextN,list(dictionary=vocab)) 
  #add the new text as the first line to the matrix, also add the last element as the class (value does not matter)
  newM <- rbind(c(as.vector(newLineForTextN),"3"),mat)
  #on retourne la classe du plus proche voisin de la matrice
  return(classerKPPV(newM[1,], 1, newM))
}


