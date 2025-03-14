#Syntaxe

#from time import time
#t = time()
#print((time()-t),'s')


from time import time

n = 0
t = time()

while n < 1000000:
    n += 0.1
print((time()-t), 's')
