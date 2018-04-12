a=int(input("enter a number"))
b=int(input("enter a number"))
l=[]
for i in range(1,a+1):
    l.append(i)
if(a>b):
    l=l[:b]
    sum=sum(l)
    print(sum)

