distance<-function(x,y){
    return(sqrt(sum((as.numeric(x)-as.numeric(y))^2)))
}

dist.voisins<-function(vecteur,data){
    return(apply(data,1,distance,x=vecteur))
}

kppv<-function(vecteur,k,data){
    v<-dist.voisins(vecteur,data)
    return(order(v)[2:(k+1)])
}

classerKPPV<-function(vecteur,k,data){
	x<-kppv(vecteur[1:(length(vecteur)-1)],k,data[,-ncol(data)])
    c<-table(data[x,ncol(data)])
    indices<-names(c)[which.max(c)]
    return(indices)
}

erreurKPPV<-function(k,data){
    res<-sapply(1:nrow(data),function(i) return(classerKPPV(data[i,],k,data)))
    sum(res!=data[,ncol(data)])/nrow(data)
}

bonneClassifKPPV<-function(k,data){
    res<-sapply(1:nrow(data),function(i) return(classerKPPV(data[i,],k,data)))
    sum(res==data[,ncol(data)])/nrow(data)
}