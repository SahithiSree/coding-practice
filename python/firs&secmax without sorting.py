s=list(map(int,input().split()))
first=0
sec=0
for i in s:
    if first<i:
        sec=first
       first=i 
        
print(first,sec)
