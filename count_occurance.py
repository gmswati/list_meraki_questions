char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# char_list=[]
i=1
l=len(char_list)
item=[]
count=[]
while i<=l:
    if char_list[i-1] not in item:
        item.append(char_list[i-1])
    i+=1
# print(item)
i=1
while i<=len(item):
    # print(char_list.count(item[i-1]))
    List=list((item[i-1],char_list.count(item[i-1])))
    # print(List)
    count.append(List)
    i+=1
print(count)