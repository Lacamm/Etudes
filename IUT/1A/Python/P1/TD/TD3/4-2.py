def position(listeNbr,listeInd):
            res = []
            for n in range(len(listeNbr)):
                        res.append(0)
            for i in range(len(listeInd)):
                        del res[listeInd[i]]
                        res.insert(listeInd[i], listeNbr[i])            
            return res

listeNbr = [45,85,96,32,741,4]
listeInd = [3,2,5,1,0,4]
print(position(listeNbr,listeInd))