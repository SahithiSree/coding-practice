n=int(input())
m=int(n/2)
flag=0
for i in range(2,m):
    if (n%i==0):
        flag= 1 
        break
if(flag):
    print("not prime")
else:
    print('prime')
        
