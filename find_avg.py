L=[23,14,56,12,19,9,15,25,31,42,43]
l=len(L)
i=1
S_E=0
E=0
O=0
S_O=0
while i<=l:
    if L[i-1]%2==0:
        E+=1
        S_E+=L[i-1]
    else:
        O+=1
        S_O+=L[i-1]
    i+=1
print(S_E)
print(E)
print(S_O)
print(O)
print('ave.E=',S_E/E)
print('ave.O=',S_O/O)
