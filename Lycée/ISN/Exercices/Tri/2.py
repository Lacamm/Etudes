def fusion(l1, l2):
    for n in range (3):
        if l1[n]<l2[n]:
            l3.insert(l1[n])
            l3.insert(l2[n])
        else:
            l3.insert(l1[n])
            l3.insert(l2[n])
    return(l3)

from time import time
l1 = [1,2,4]
l2 = [2,3,8]
l3 = []
n = 0
t = time()
print(fusion(l1, l2))
print((time()-t)/1000, 'ms')
