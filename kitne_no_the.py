L=[23,14,56,12,19,9,15,25,31,42,43]
l=len(L)
i=1
E=0
O=0
while i<=l:
    if L[i-1]%2==0:
        E+=1
    else:
        O+=1
    i+=1
print(E)
print(O)
