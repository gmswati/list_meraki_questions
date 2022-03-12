L=[23,14,56,12,19,9,15,25,31,42,43]
l=len(L)
i=1
S_E=0
S_O=0
while i<=l:
    if L[i-1]%2==0:
        S_E+=L[i-1]
    else:
        S_O+=L[i-1]
    i+=1
print(S_E)
print(S_O)
