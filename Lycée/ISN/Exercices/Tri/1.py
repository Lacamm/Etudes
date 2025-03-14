def triSelection(a):
    return(sorted(a))

from time import time
a = [1,3,2]
t = time()
print(triSelection(a))
print((time()-t),'ms')
