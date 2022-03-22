str="aaabbbcccaaabbbccc"
i=0
li=[]
while i<len(str):
    if str[i] not in li:
      li.append(str[i])
    i=i+1
print(li*2)
