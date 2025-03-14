def triSelection(a):
    n = len(a)
    for i in range(n-1):
        k = i
        for j in range(i+1,n):
            if a[k]>a[j]:
                k = j
        a[k],a[i] = a[i],a[k]

a = [19,12,15,1,3,20]
triSelection(a)
print(a)
