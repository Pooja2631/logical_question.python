list1=['deepti','chauhan']
i=0
capital=list1[i]
while i<len(list1):
    j=0
    while j<len(list1[i]):
        if list1[i][j]==0:
            capital=list1[i][j].upper()
        j=j+1
    i=i+1
    print(capital)