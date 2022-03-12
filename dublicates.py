n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
i=1
List=[]
New_List=[]
while i<=len(n):
    if n[i-1] not in New_List:
        New_List.append(n[i-1])
    i+=1
print(New_List)
j=1
while j<=len(New_List):
    Z=n.count(New_List[j-1])
    print(Z)
    if Z>1:
        List.append(New_List[j-1])
    j+=1
print(List)
