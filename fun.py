def add():
    a=int(input("enetr the number....."))
    b=int(input("enetr the number......."))
    if a<0 or b<0:
        return "invalid number"
    i=1
    c=a
    sum=0
    while i<=b:
        if i%a==0:
            print(i)
            sum=sum+i
        i=i+1
    return "="+str(sum)
print(add())