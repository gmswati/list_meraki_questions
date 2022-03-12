kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=1
l=len(kitna_paisa_hai)
K=0
L=0
D=0
while i<=l:
    if kitna_paisa_hai[i-1]>=10000000:
        K+=1
    elif kitna_paisa_hai[i-1]>=100000:
        L+=1
    else:
        D+=1
    i+=1
print(K,'crorepati')
print(L,'lakhpati')
print(D,'dilwale')
