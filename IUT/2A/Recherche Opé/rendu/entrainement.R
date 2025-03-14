library("tm")
library("e1071")

splash=function(x){
    # res=NULL
    # for (i in x) res=paste(res, i)
    # res
    paste(x, collapse = " ")
}

#Suppression des script s(<script .... </script>)
removeScript=function(t){
    #decoupage de la chaine en utilisant "<split"
    #sp=strsplit(splash(t), "<script")
    sp=strsplit(t, "<script")
    #pour chaque partie du split, le debut (jusqu'a </script> est supprime
    vec=sapply(sp[[1]], gsub, pattern=".*</script>", replace=" ")
    #les elements du split nottoyes sont concatenes
    PlainTextDocument(splash(vec))
}

#Suppression de toutes les balises
removeBalises=function(x){
    t1=gsub("<[^>]*>", " ", x)
    #suppression des occurrences multiples d'espaces (ou de tabulations)
    PlainTextDocument(gsub("[ \t]+"," ",t1))
}

nettoyage = function(corpus) {
  corpus = tm_map(corpus, content_transformer(tolower))
  corpus = tm_map(corpus, content_transformer(splash))
  corpus = tm_map(corpus, content_transformer(removeScript))
  corpus = tm_map(corpus, content_transformer(removeBalises))
  corpus = tm_map(corpus, removeNumbers)
  corpus = tm_map(corpus, removeWords, words=stopwords("en"))
  corpus = tm_map(corpus, stemDocument)
  corpus = tm_map(corpus, removePunctuation, ucp=TRUE)
}


ds <- DirSource("fichierEntrainement/", recursive=TRUE, encoding="UTF-8")
corpus <- VCorpus(ds, readerControl = list(reader = reader(ds), language="en"))
cleaned_corpus = nettoyage(corpus)
dtm = DocumentTermMatrix(cleaned_corpus)
mat <- as.matrix(dtm)

terms = findFreqTerms(dtm, lowfreq = 125)

saveRDS(terms, file = "vocab.rds")

dtm = dtm[, terms]
mat = as.matrix(dtm)
y <- c(rep("accueil",150),rep("blog",150),rep("commerce",150),rep("FAQ",150),rep("home",150),rep("liste",150),rep("recherche",150))

model <- svm(x=mat,y=y,type='C',kernel='linear')

#final_matrix <- cbind(mat,classes)

saveRDS(model, file = "test.rds")

