n=int(input())
l=len(str(n))
n=str(n)
sum=0
for i in n:
    sum=sum+int(i)**l
if(sum==int(n)):
    print("valid",sum)
else:
    print("not valid",sum)
    
