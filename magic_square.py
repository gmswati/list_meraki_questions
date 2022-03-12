magic_square=[[5,3,7],[1,8,9],[6,4,2]]
i=1
l=len(magic_square)
while i<=l:
    j=1
    sum=0
    b=sum
    while j<=len(magic_square[i-1]):
        sum+=magic_square[i-1][j-1]
        a=sum
        print(a,'*')
    if a==sum:
        a=sum
        print('a')
    else:
        print("magic")
