m = input('Un mot: ')
res = 0

def voyelles(res):
    for n in range (len(m)):
        if m[n] == 'a' or 'e' or 'i' or 'o' or 'u' or 'y':
            res+=1
        else:
            res-=1
        print(res)
    return res

print (voyelles(res))
