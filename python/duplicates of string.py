s=input()
count=[]
for i in s:
    if s.count(i) > 1:
        if i not in count:
            count.append(i)
print(*count)










***********************************************************************************
s=input()
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
