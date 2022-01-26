s=list(map(int,input().split()))
a={}
count=0
for i in s:
    if i in a:
        a[i]+=1 
    else:
        a[i]=1 
for key,value in a.items():
    if value>1:
        print(key,end=" ")
