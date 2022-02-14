num1=int(input("enter the number"))
num2=int(input("entercthe number"))
if num1>num2:
	m=num1
else:
	m=num2
while 1:
	if m%num1==0 and m%num2==0:
		print(m)
		break
	m +=1