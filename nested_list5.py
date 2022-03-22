i=1
l=[]
while i<=100:
    j=2
    count=0
    while j<i:
        if i%j==0:
            count=count+1
        j=j+1
    if count==0:
        if i>=13:
            l2=[]
            l2.append(i)
            a=str(i)
            x=a[::-1]
            l2.append(int(x))
            l.append(l2)
    i+=1
print(l)