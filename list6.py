user1=input("enter the name1...")
user2=input("enter the name2...")
user3=input("enter the name3...")
i=0
b=""
while i<len(user1) and i<len(user2):
    if user1[i]==user1[0] and user2[i]==user2[0]:
        cap=user1[i].upper()
        cap1=user2[i].upper()
        b+=cap+"." +cap1
    i=i+1
print(b+"."+user3)