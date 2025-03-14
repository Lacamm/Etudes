def qcm(l):
    res=0
    for i in range(len(l)):
        if i%2==1:
            print(i%2)
            res=res+l[i]
    return res

print(qcm([6,6,2,4,10]))
