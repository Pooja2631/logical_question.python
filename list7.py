# a=[34,27,6,4,7,3] 
# i=0
# j=1
# d=[]
# while i<len(a):
#     sub=a[i]-a[j]
#     d.append(sub)
#     i=i+2
#     j=j+2
# print(d)

list1=[[2],[12,3,4],[4,5,6,7,8,9],[0]]
i=0
max=0
while i<len(list1):
    j=0
    co=0
    while j<len(list1[i]):
        if co>max:
            co=co+list1[i]
            max=list1[i]
        j=j+1
    i=i+1
print(max)




